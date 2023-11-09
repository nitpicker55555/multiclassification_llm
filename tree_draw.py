import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# 定义节点、边和相关函数
G = nx.DiGraph()
root = "Root"
children_data = {
    'Industrial Accidents': 3,
    'Chemical Leakage Accidents': 1,
    'Aviation Accidents': 2,
    'Traffic Accidents': 60,
    'Fire Accidents': 1,
    'Public Accidents': 7,
    'Natural Disasters': 3,
    'Waste of resources': 3,
    'Discrimination': 11,
    'Invasion of Citizens Privacy': 18,
    'Family accident': 1
}

#分类数字不能求和是因为  有的父节点是判断出来的标签，有的父节点是后期再分类出来的标签

#第一个列表代表第一层节点，第一层列表的每个字典代表每个上级节点的子节点
G.add_node(root)
discrimination={ 'Nationality discrimination': 2,
    'Racial discrimination': 8,
    'Sex discrimination': 1,}
dict_length = {'Traffic Accidents':{
    'Technical Issues': {
        'Decision and Control': {
            'AI decision-making flaw': 52,
            'Control and execution issues': 43,
            'Route planning problem': 35
        },
        'Hardware and Integration': {
            'Sensor or data input error': 27,
            'System integration and hardware issues': 2,
            'Hardware or software failure': 9
        },
        'Data and Processing': {
            'Data processing error': 14,
            'Training data and validation issues': 2
        },
        'System Robustness and Fault Tolerance': {
            'System robustness and fault tolerance issues': 46
        }
    },
    'Human-Computer Interaction Issues': {
        'Human-computer interaction problem': 16,
        'Driver distraction due to over-reliance on technology': 34,
        'Human factors other than the driver': 3,
        'Insufficient feedback mechanism': 11,
        'Communication and interaction issues': 8,
        'Transparency and interpretability issues': 2
    },
    'Safety Issues': {
        'Causing safety threats to others other than passengers': 34,
        'Emergency response issues': 30,
        'Threat to passenger safety': 37
    },
    'Data Issues': {
        'Inaccurate or incomplete data': 18
    },
    'Human Operational Issues': {
        'Driver operation problem': 10
    }
},'Discrimination':{'Nationality discrimination': 2,
    'Racial discrimination': 8,
    'Sex discrimination': 1}}

# first_dict = {}
# second_dict={}
# third_dict={}
# for key,value in dict_length.items():
#     if isinstance(list(value.values())[0],dict):
#         # print(key)
#         third_dict=dict_length[key]
#         second_dict[key]={}
#         first_dict[key]=0
#         for key2,value2 in value.items():
#             # print(value2)
#             first_dict[key] +=sum(value2.values())
#             second_dict[key][key2]=sum(value2.values())
#
#
#         # print(first_dict)
#     else:
#         first_dict[key] = sum(value.values())
# print(first_dict)
# print(second_dict)
# print(third_dict)
result_list={}
def sum_dict(dict_sample,sum_value=0):
    # print(dict_sample)
    for key, value in dict_sample.items():
        if isinstance(list(value.values())[0], dict):
            sum_value+=sum_dict(dict_sample[key], sum_value)
        else:

            sum_value+=sum(value.values())
    return sum_value

def check_dict(depth,result_list,dict_sample,parent="Root"):
    merged_dict = {}
    depth += 1
    if depth==2:
        print(depth)
    if depth not in result_list:
        result_list[depth] = {}
    for key, value in dict_sample.items():
        if isinstance((value), dict):
            merged_dict[key] = sum_dict({key:dict_sample[key]})

            check_dict(depth,result_list,dict_sample[key],key)
        else:
            merged_dict[key]=dict_sample[key]

    result_list[depth].update({parent:merged_dict})

    return result_list
total_dict=check_dict(0,result_list,dict_length)
# total_dict={1: {'Root': {'Traffic Accidents': 433, 'Discrimination': 11}}, 2: {'Traffic Accidents': {'Technical Issues': 230, 'Human-Computer Interaction Issues': 74, 'Safety Issues': 101, 'Data Issues': 18, 'Human Operational Issues': 10}, 'Discrimination': {'Nationality discrimination': 2, 'Racial discrimination': 8, 'Sex discrimination': 1}}, 3: {'Technical Issues': {'Decision and Control': 130, 'Hardware and Integration': 38, 'Data and Processing': 16, 'System Robustness and Fault Tolerance': 46}, 'Human-Computer Interaction Issues': {'Human-computer interaction problem': 16, 'Driver distraction due to over-reliance on technology': 34, 'Human factors other than the driver': 3, 'Insufficient feedback mechanism': 11, 'Communication and interaction issues': 8, 'Transparency and interpretability issues': 2}, 'Safety Issues': {'Causing safety threats to others other than passengers': 34, 'Emergency response issues': 30, 'Threat to passenger safety': 37}, 'Data Issues': {'Inaccurate or incomplete data': 18}, 'Human Operational Issues': {'Driver operation problem': 10}}, 4: {'Decision and Control': {'AI decision-making flaw': 52, 'Control and execution issues': 43, 'Path planning problem': 35}, 'Hardware and Integration': {'Sensor or data input error': 27, 'System integration and hardware issues': 2, 'Hardware or software failure': 9}, 'Data and Processing': {'Data processing error': 14, 'Training data and validation issues': 2}, 'System Robustness and Fault Tolerance': {'System robustness and fault tolerance issues': 46}}}

# total_list=[first_dict,second_dict,third_dict]
sum_dict_var={}

second_child_data=total_dict[2]

def iteration_func(node,depth,total_list):

    if node in total_list[depth].keys():
        for third, t_value in total_list[depth][node].items():
            G.add_edge(node, third)
            sum_dict_var.update({third:t_value})
            if depth<=3:
                iteration_func(third,depth+1,total_list)
def build_tree(total_list):
    sum_dict_var.update(children_data)
    # sum_dict.update(total_list[0])
    for child, value in children_data.items():
        G.add_edge(root, child)
        iteration_func(child,2,total_list)
        #
        # if child == 'Traffic Accidents':
        #     for second, s_value in total_list[0].items():
        #         G.add_edge(child, second)
        #         iteration_func(second, 1, total_list)

build_tree(total_dict)
print(sum_dict_var)
def get_edge_color_new(value, cmap_name="viridis_r", vmin=1, vmax=230):
    cmap = plt.get_cmap(cmap_name)
    return cmap((value - vmin) / (vmax - vmin))


edge_colors = [get_edge_color_new(sum_dict_var[target])
               for _, target in G.edges()]

# 定义布局
# level_1_y = 2
# level_2_y = 1
# level_3_y = 0
#
# # 为根节点、子节点和孙子节点定义明确的位置，确保它们在不同的层次上
# fixed_positions = {root: (0, level_1_y)}
#
# for i, child in enumerate(children_data.keys()):
#     fixed_positions[child] = (i, level_2_y)
#
# for j, grandchild in enumerate(second_child_data.keys()):
#     fixed_positions[grandchild] = (j + len(children_data.keys()) / 2 - len(second_child_data) / 2, level_3_y)
def get_fixed_positions(root, *layers):
    """
    Generate fixed positions for nodes in a tree-like structure.

    Parameters:
    - root: The name of the root node.
    - *layers: A series of dictionaries, each representing a layer.

    Returns:
    - A dictionary containing fixed positions for the nodes.
    """
    fixed_positions = {root: (0, len(layers))}

    for layer_idx, layer in enumerate(layers):
        num_nodes_in_layer = len(layer)

        # Adjust positions based on the number of nodes in the layer
        for node_idx, node in enumerate(layer.keys()):
            x_pos = 30*(node_idx - num_nodes_in_layer / 2)

            y_pos = len(layers) - layer_idx - 1
            fixed_positions[node] = (x_pos, y_pos)
    print(fixed_positions)
    return fixed_positions
def flatten_dict(dict_sample):
    merged_dict={}

    for key in dict_sample:
        if isinstance(dict_sample[key],dict):
            merged_dict.update(dict_sample[key])
        else:
            merged_dict.update(dict_sample)
    return merged_dict
fixed_positions = get_fixed_positions('Root', flatten_dict(children_data), flatten_dict(total_dict[2]), flatten_dict(total_dict[3]),flatten_dict(total_dict[4]))
print(len(children_data),len(total_dict[2]),len(total_dict[3]),len(total_dict[4]))
# 绘制图
# fig, ax = plt.subplots(figsize=(20, 12))
# nx.draw(G, pos=fixed_positions, with_labels=True, node_color="lightgray", edge_color=edge_colors, width=2, ax=ax)
#
# 添加颜色条
# sm = plt.cm.ScalarMappable(cmap=plt.get_cmap("viridis_r"), norm=plt.Normalize(vmin=1, vmax=230))
# sm.set_array([])
# cbar = plt.colorbar(sm, ax=ax)
# cbar.set_label('Values of Nodes')

def split_label(label):
    """将长标签分为多行"""
    words = label.split()
    lines = []
    current_line = []
    for word in words:
        if len(" ".join(current_line + [word])) > 15:  # 限制每行的字符数
            lines.append(" ".join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    lines.append(" ".join(current_line))
    return "\n".join(lines)

# 为每个节点生成带数值的标签
labels_with_values = {node: split_label(node) + ("\n" + str(value) if node in sum_dict_var or node in sum_dict_var else "")
                      for node, value in sum_dict_var.items()}
labels_with_values.update({'Root':'Root'})
print(labels_with_values)
all_values = list(sum_dict_var.values())

# 计算分位数边界
quantiles = [np.percentile(all_values, p) for p in [25, 50, 75, 100]]

print(len(sum_dict_var))
# 定义一个函数来根据分位数映射获取颜色
def get_quantile_edge_color(value, cmap_name="viridis_r"):
    # 确定数值属于哪个分位数区间
    if value <= quantiles[0]:
        quantile_idx = 0
    elif value <= quantiles[1]:
        quantile_idx = 1
    elif value <= quantiles[2]:
        quantile_idx = 2
    else:
        quantile_idx = 3

    # 根据分位数区间获取颜色
    cmap = plt.get_cmap(cmap_name)
    return cmap(quantile_idx / 3)  # 3是因为我们有4个区间


# 更新每个边的颜色
edge_colors = [
    get_quantile_edge_color(sum_dict_var[target])
    for _, target in G.edges()]

# 重新绘制图，同时调整标签位置

fig, ax = plt.subplots(figsize=(60, 80))
plt.subplots_adjust(top=0.95, bottom=0.05, left=0, right=0.99, hspace=0.2, wspace=0.2)

nx.draw(G, pos=fixed_positions, with_labels=False, node_color="lightgray", edge_color=edge_colors, width=5, ax=ax,node_size=25000)
nx.draw_networkx_labels(G, pos=fixed_positions, labels=labels_with_values, verticalalignment="center", ax=ax,font_size=25)

# 添加颜色条
sm = plt.cm.ScalarMappable(cmap=plt.get_cmap("viridis_r"), norm=plt.Normalize(vmin=0, vmax=3))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, ticks=[0, 1, 2, 3])
cbar.set_label('Quantiles of Node Values', fontsize=40)

cbar.set_ticklabels(['0-25%', '25-50%', '50-75%', '75-100%'])
cbar.ax.tick_params(labelsize=25)

# 设置标题
plt.title("Multilabel classification for accidents in Ai-Cases",fontsize=50, fontweight='bold')
plt.text(-200.5, -0.5, "Total labels: 43\nLabels in first level:11\nLabels in second level:8\nLabels in third level:15\nLabels in forth level:9", fontsize=40,  fontweight='bold',ha='left',va='bottom')

plt.savefig('tree.png')

plt.show()
