import pandas as pd

def jsonl_to_xlsx(jsonl_path, xlsx_path):
    # 读取.jsonl文件
    df = pd.read_json(jsonl_path, lines=True)

    # 对于每个缺失的键，填充False值
    for column in df.columns:
        df[column] = df[column].where(pd.notna(df[column]), False)

    # 保存为.xlsx文件
    with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

# 使用示例
jsonl_to_xlsx(r"C:\Users\Morning\Desktop\hiwi\heart\paper\output_final_dict_t.jsonl", "output_final_dict_t.xlsx")
