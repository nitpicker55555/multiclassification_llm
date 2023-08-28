# 定义数据
layer_1_data = {
    'Root': {
        'Technical Issues': 230, 
        'Human-Computer Interaction Issues': 74, 
        'Safety Issues': 101, 
        'Data Issues': 18, 
        'Human Operational Issues': 10
    }
}

layer_2_data = {
    'Technical Issues': {
        'Decision and Control': 130, 
        'Hardware and Integration': 38, 
        'Data and Processing': 16, 
        'System Robustness and Fault Tolerance': 46
    }
}

layer_3_data = {
    'Decision and Control': {
        'AI decision-making flaw': 52, 
        'Control and execution issues': 43, 
        'Path planning problem': 35
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
}

# 使用函数生成位置
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
            x_pos = node_idx - num_nodes_in_layer / 2
            y_pos = len(layers) - layer_idx - 1
            fixed_positions[node] = (x_pos, y_pos)

    return fixed_positions


# Test the function with the provided data
positions = get_fixed_positions('Root', layer_1_data['Root'], layer_2_data['Technical Issues'], layer_3_data['Decision and Control'])
print(positions)
# Test the function with the provided data

def flatten_dict(dict_sample):
    merged_dict={}
    for key in dict_sample:
        merged_dict.update(dict_sample[key])
    return merged_dict
positions = get_fixed_positions('Root', flatten_dict(layer_1_data), flatten_dict(layer_2_data), flatten_dict(layer_3_data))
print(positions)