import matplotlib.pyplot as plt

# 示例数据
sizes = [30, 10, 15, 45]
labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
wedges, texts = ax.pie(sizes, labels=labels)

# 找到并移动特定标签（例如"B"）
for text, label in zip(texts, labels):
    if label == 'B':
        # 获取当前位置
        x, y = text.get_position()
        # 左移5个像素（这里的单位是数据单位，具体的效果可能需要根据图表的尺寸调整）
        text.set_position((x - 25/72, y))

plt.show()
