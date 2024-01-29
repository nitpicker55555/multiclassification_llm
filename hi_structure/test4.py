import plotly.graph_objects as go
import pandas as pd

# 假设这是你的层级数据，包含额外信息
data = pd.DataFrame({
    'id': ['A', 'B', 'C', 'D', 'E', 'F'],
    'parent': ['', 'A', 'A', 'B', 'B', 'C'],
    'value': [100, 50, 50, 25, 25, 50],
    'additional_info': ['info A', 'info B', 'info C', 'info D', 'info E', 'info F']
})

# 计算百分比，同前面的例子
# ...

# 格式化标签文本
data['label_text'] = data.apply(lambda row: f"Info: {row['additional_info']}", axis=1)

# 创建Sunburst图
fig = go.Figure(go.Sunburst(
    ids=data['id'],
    labels=data['id'],
    parents=data['parent'],
    values=data['value'],
    branchvalues='total',
    text=data['label_text'],  # 使用格式化后的标签文本
    textinfo='label+text+percent parent'  # 显示标签、文本和百分比
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()
