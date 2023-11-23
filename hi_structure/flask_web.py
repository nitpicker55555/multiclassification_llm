from flask import Flask, render_template, jsonify,session
from bbb_clean_and_alignment import get_cluster
from bbb_clean_and_alignment import  get_clean_word
from flask import request
from flask_sqlalchemy import SQLAlchemy
import numpy as np
from sklearn.neighbors import NearestNeighbors
# import numpy as np

from flask_session import Session
import pickle
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  #


app.config["SESSION_TYPE"] = "filesystem"  # 或 "redis", "sqlalchemy"
Session(app)
db = SQLAlchemy(app)
# 定义数据库模型
class DbModel(db.Model):
    ip = db.Column(db.Integer, primary_key=True)
    clean_word = db.Column(db.Integer, nullable=False)
    sentence_emb= db.Column(db.Integer, nullable=False)
    # speak = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<DbModel {self.id}>'
# 创建数据库表
with app.app_context():
    db.create_all()
@app.route('/')
def index():
    user_ip = request.headers.get('X-Real-IP') or request.headers.get('X-Forwarded-For') or request.remote_addr

    print(user_ip, "user_ip")
    session['ip']=user_ip

    return render_template('index.html')

@app.route('/get_data')
def get_data():
    # 创建一个字典作为示例

    # sentence_emb,clean_word = get_clean_word(r"C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2021-1-1_2021-12-31_without_profile_labels.jsonl")
    sentence_emb,clean_word,_ = get_clean_word(r"C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\Geo-AI ethics cases_labels.jsonl")
    session['clean_word']=clean_word
    session['sentence_emb'] = sentence_emb
    # optimal_eps = find_optimal_eps_func(2)
    result_dict=get_cluster(clean_word,sentence_emb,0.5,2)
    return jsonify(result_dict)
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


    result_dict=get_cluster(session['clean_word'],session['sentence_emb'],slider_eps,slider_min)
    print(len(result_dict),"result_dict")
    return jsonify(result_dict)
@app.route('/new_page_tree')
def new_page_tree():
    return render_template('index_tree.html')

@app.route('/get_node_data')
def get_node_data():
    nodeValuesText=session['nodeValuesText']
    nodeStructureText=session['nodeStructureText']
    return jsonify({'nodeValuesText': nodeValuesText,'nodeStructureText':nodeStructureText})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
