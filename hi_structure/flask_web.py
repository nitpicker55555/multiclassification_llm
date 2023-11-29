from flask import Flask, render_template, jsonify,session

from flask import request
# from flask_sqlalchemy import SQLAlchemy
import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
import json
from werkzeug.utils import secure_filename
from flask_session import Session
from fff_sentiment_analyse import sentiment_model
from eee_calculate_and_draw import calculate_and_draw_func
from ddd_map_words_to_dicts import map_words_2_dicts
from ccc_get_structure import get_structure
from bbb_clean_and_alignment import get_clean_word
from bbb_clean_and_alignment import get_cluster
from bbb_clean_and_alignment import make_alignment
from aaa_gpt_set_label import main
from aaa_model_set_label import main_model
import pickle
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  #

app.config['UPLOAD_FOLDER']='uploads'
app.config["SESSION_TYPE"] = "filesystem"  # 或 "redis", "sqlalchemy"
Session(app)

# 定义数据库模型

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            if filename.endswith('.xlsx'):
                df = pd.read_excel(file_path)
                jsonl_path = os.path.join(app.config['UPLOAD_FOLDER'], filename.replace(".xlsx",".jsonl"))
                df.to_json(jsonl_path, orient='records', lines=True)
                file_path = jsonl_path

                session['filename'] = (file_path.replace(".xlsx",'jsonl'))
                print(session['filename'])
            else:
                session['filename'] = (file_path)
                print(session['filename'])
            with open(file_path, 'r') as file:
                first_line = file.readline()
                keys = list(json.loads(first_line).keys())
                return jsonify(keys)



    return render_template('index_upload.html')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['xlsx', 'jsonl']
@app.route('/set_labels_gpt', methods=['POST'])
def set_labels_gpt():
    # 创建一个字典作为示例
    data = request.json
    col_name = data['col_name']
    print("col_name:", col_name)
    main(session['filename'], col_name)



    return jsonify({'status': 'success'})
@app.route('/set_labels_model', methods=['POST'])
def set_labels_model():
    # 创建一个字典作为示例
    data = request.json
    col_name = data['col_name']
    print("col_name:", col_name)
    main_model(session['filename'], col_name)



    return jsonify({'status': 'success'})
@app.route('/get_data')
def get_data():
    # 创建一个字典作为示例

    # sentence_emb,clean_word = get_clean_word(r"C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2021-1-1_2021-12-31_without_profile_labels.jsonl")
    json_labels_name=session['filename'].replace(".jsonl","_labels.jsonl")
    sentence_embeddings,sum_WithoutDuplicate,sum_WithDuplicate_words=get_clean_word(json_labels_name)

    pca_result_dict=get_cluster(sum_WithoutDuplicate,sentence_embeddings,0.7,2)

    sorted_sum_list,_=make_alignment(pca_result_dict,sum_WithDuplicate_words)
    # sentence_emb,clean_word,_ = get_clean_word(json_labels_name)
    session['clean_word']=sum_WithoutDuplicate
    session['sentence_emb'] = sentence_embeddings
    session['sorted_sum_list'] = sorted_sum_list
    # optimal_eps = find_optimal_eps_func(2)

    # result_dict=get_cluster(clean_word,sentence_emb,0.5,2)
    return jsonify(pca_result_dict)
def find_optimal_eps_func(min_samples):
    data=session['sentence_emb']
    # min_samples = request.args.get('slider_min', type=int)
    k = min_samples - 1
    neigh = NearestNeighbors(n_neighbors=k)
    neigh.fit(data)
    distances, indices = neigh.kneighbors(data)

    # 对距离进行排序
    sorted_distances = np.sort(distances[:, k-1], axis=0)

    # 计算距离的差分（斜率）
    diffs = np.diff(sorted_distances)

    # 找到斜率变化最大的点
    optimal_index = np.argmax(diffs)
    optimal_eps = sorted_distances[optimal_index]

    print(optimal_eps,"optimal_eps")
    return optimal_eps
@app.route('/find_optimal_eps', methods=['POST'])
def find_optimal_eps():
    """
    自动计算最佳eps值。

    :param data: 数据集，形状为 (n_samples, n_features) 的 NumPy 数组。
    :param min_samples: 用于DBSCAN的min_samples参数。
    :return: 计算出的最佳eps值。
    """
    # 计算每个点到其第k个最近邻的距离
    # data=session['sentence_emb']
    min_samples = request.args.get('slider_min', type=int)
    optimal_eps=find_optimal_eps_func(min_samples)
    return jsonify({'message': optimal_eps})

@app.route('/set_values', methods=['POST'])
def set_values():
    slider_eps = request.args.get('slider_eps', type=float)
    slider_min = (request.args.get('slider_min', type=int))


    pca_result_dict=get_cluster(session['clean_word'],session['sentence_emb'],slider_eps,slider_min)
    print(len(pca_result_dict),"pca_result_dict")
    session['pca_result_dict']=pca_result_dict
    return jsonify(pca_result_dict)
@app.route('/new_page_tree')
def new_page_tree():
    return render_template('index_tree.html')
@app.route('/new_page_pca')
def new_page_pca():
    return render_template('index_pca.html')
@app.route('/new_page_sentiment')
def new_page_sentiment():
    return render_template('index_sentiment.html')
@app.route('/get_node_data')
def get_node_data():
    sorted_sum_list=session['sorted_sum_list']
    filename=session['filename']
    json_structure=get_structure(sorted_sum_list,filename.replace(".jsonl",""))

    mapped_dicts=map_words_2_dicts(json_structure,sorted_sum_list,filename.replace(".jsonl",""))


    print("json_structure",json_structure)
    print("mapped_dicts",mapped_dicts)

    all_num_keys=calculate_and_draw_func(json_structure,mapped_dicts,filename)
    nodeValuesText=all_num_keys
    nodeStructureText=json_structure
    print({'nodeValuesText': nodeValuesText,'nodeStructureText':nodeStructureText})
    return jsonify({'nodeValuesText': nodeValuesText,'nodeStructureText':nodeStructureText})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
