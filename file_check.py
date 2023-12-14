input_str = "这里是你的长字符串.assssssssssssssssssssssssssssssssssssssssssssssssssssss....."

# 计算字符串的长度
length = len(input_str)

# 以每次100个字符遍历字符串
for i in range(0, length, 10):
    # 获取当前位置到下一个100个字符的子字符串
    substring = input_str[i:i+10]
    # 在这里处理子字符串，例如打印它
    print(substring)
