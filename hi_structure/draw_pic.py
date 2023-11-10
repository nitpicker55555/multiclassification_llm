import matplotlib.pyplot as plt
import networkx as nx
def draw_pic_func(data="",num_data=''):
    # 构建数据结构
    # data = {
    #     "Technology and Innovation": {
    #         "Big Data": {
    #             "Data Analysis": 0,
    #             "Cloud Computing": 0,
    #             "Data Privacy": 0
    #         },
    #         "Artificial Intelligence": {
    #             "Machine Learning": {
    #                 "Deep Learning": 0,
    #                 "Algorithms": 10,
    #                 "Natural Language Processing": 0
    #             },
    #             "Responsible AI": {
    #                 "AI Governance": 0,
    #                 "AI Ethics": 0,
    #                 "AI Law": 0
    #             }
    #         },
    #         "Digital Technologies": {
    #             "Internet of Things": 20,
    #             "Robotics": 0,
    #             "Digital Transformation": 0
    #         }
    #     },
    #     "Industry Applications": {
    #         "FinTech": {
    #             "Blockchain": 0,
    #             "Cryptocurrency": 30,
    #             "Financial Services":40
    #         },
    #         "Healthcare": {
    #             "Telemedicine": 0,
    #             "Health Data Analysis": 0,
    #             "Medical Robotics": 0
    #         },
    #         "Automation and Transportation": {
    #             "Self-driving Cars": 0,
    #             "Drone Technology": 0,
    #             "Intelligent Transportation Systems": 0
    #         }
    #     },
    #     "Society and Policy": {
    #         "Privacy and Security": {
    #             "Cybersecurity": 0,
    #             "Data Protection": 0,
    #             "Privacy Regulations": 0
    #         },
    #         "Ethics and Responsibility": {
    #             "Technology Ethics": 0,
    #             "Diversity and Inclusivity": 0,
    #             "Social Impact": 0
    #         },
    #         "Education and Development": {
    #             "Programming Education": 0,
    #             "Technology Innovation": 0,
    #             "Educational Technology": 0
    #         },
    #         "Legislation": {
    #             "Policy Development": 0,
    #             "Regulatory Frameworks": 0,
    #             "Legal Compliance": 0
    #         }
    #     }
    # }

    # 创建图和添加节点
    G = nx.DiGraph()

    # 我们需要重新构建图，并且添加正确的边
    G = nx.DiGraph()
    node_positions = {}  # 用于存储节点位置
    level_width = {}  # 用于存储每层的宽度
    # G = nx.DiGraph()
    # node_positions = {}  # 用于存储节点位置
    # level_width = {}  # 用于存储每层的宽度
    parent_nodes = {}  # 存储节点及其父节点

    # 重构图表，使得只在有数字键值的标签显示键值，没有数字键值的标签只显示标签
    def add_nodes_edges_and_positions(graph, data, random_dict, level=0, path=[]):

        for key, value in data.items():
            node = key  # 仅使用key作为节点名称
            node_label = "{} ({})".format(node, random_dict.get(node, ''))
            full_node_path = ' -> '.join(path + [node])  # 完整的节点路径
            graph.add_node(node_label)
            if level not in level_width:
                level_width[level] = 0
            node_positions[node_label] = (level_width[level], -level)
            level_width[level] += 1
            if path:
                parent = path[-1]
                parent_label = "{} ({})".format(parent, random_dict.get(parent, ''))
                graph.add_edge(parent_label, node_label)
            if isinstance(value, dict):
                add_nodes_edges_and_positions(graph, value, random_dict, level + 1, path + [key])

    add_nodes_edges_and_positions(G, data, num_data)
    # 调整每层的节点位置，使其居中对齐
    max_width = max(level_width.values())
    for node, (x, y) in node_positions.items():
        node_positions[node] = ((x - level_width[-y] / 2 + max_width / 2), y)

    # 绘制图表
    plt.figure(figsize=(14, 10))
    nx.draw(G, node_positions, with_labels=False, arrows=False, node_size=3000, node_color='skyblue', font_size=8)

    # 为每个节点添加标签
    for node, (x, y) in node_positions.items():
        label = G.nodes[node].get('label', node)
        plt.text(x, y, label, fontsize=8, ha='center', va='center', rotation=45)

    plt.title("Technology and Innovation Hierarchy Tree with Selective Labels", fontsize=15)
    plt.show()
# draw_pic_func()
    # plt.savefig("tree.png")