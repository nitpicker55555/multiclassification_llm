import pandas as pd
import json
# Load the Excel file into a DataFrame
file_path = 'semantic_combine.csv'
df = pd.read_csv(file_path)
def boolean_to_semantic():
    severity_columns = []
    binary_columns = []
    for col in df.columns:
        unique_values = df[col].dropna().unique()

        if len(unique_values) > 2 and len(unique_values) < 8 and col != "Newsroom":
            severity_columns.append(col)
        elif len(unique_values) == 2 and col != "Newsroom":
            binary_columns.append(col)
    for col in severity_columns:
        df[col] = df[col].replace({0: "Potential hazard with zero or negligible risk", 2: "some potential damage",
                                   3: "Routine or Significant Potential Damage", 4: "serious potential Damage",
                                   5: "Unsustainable Potential Damage"})
    for coll in binary_columns:
        df[coll] = df[coll].replace({0: "False", 1: "True"})
    """
    • Class 1 Potential hazard with zero or negligible risk
    • Level 2 some potential damage,
    • Class 3 Routine or Significant Potential Hazard
    • Class 4 serious potential hazard
    • Level 5 Unsustainable Potential Damage
    """
    print(binary_columns)
    print(severity_columns)
    df.to_csv("semantic_combine.csv")
    # print(binary_columns)
def csv_to_json():
    cate="Risk to Human Rights	instances with privacy violations	privacy sensitivity	privacy violations severity	instances with injustice to rights	Severity of injustice	instances involving vulnerable groups	emotional and psychological harm	vulnerable groups affected	cases where harm is reversible	affected by challenges to self-identity and values	Severity of emotional and psychological harm	instances where the harm persists	Physical harm	Severity of Physical harm 	instances where the physical harm persists	cases where the physical harm is reversible	instances where the harm is easily detectable	Economic loss	instances where economic losses persist	the severity of economic impact	extent of impact is fixed	affected individuals	affected local population	global implications	Whether humans can be replaced	Whether there is a law to regulate	AI-based specificity	cases affected by untimely data training and maintenance	cases affected by opaque and recurring weak capacities	cases affected due to limitations of traditional supervisory methods	lifecycle time period-planning and design	lifecycle time period-collection and processing data	lifecycle time period-building usage model	lifecycle time period-verification and verification	lifecycle time period-deployment 	lifecycle time period-Operation and Monitoring	lifecycle time period-End User Use and Impact	Geographical Attributes-Timeliness	Geographical Attributes-Accuracy	Data Production Process -Acquisition	Data Production Process-Preprocessing	Data Production Process-Integration	Data Production Process-Storage and Management	Data Production Process-Analysis and Processing	Data Production Process-Application Communication"
    cate='"'+cate.replace("\t",'","')+'"'
    labels_=cate.split("\t")
    # print(cate)

    sum_dict_={}

    system_dict={'role':'system','content':'Given a news text, provide the following fields in a JSON dict, where applicable:'+str(cate)}
    user_dict={'role':'user','content':''}
    assistant_dict={'role':'assistant','content':''}
    # print(system_dict)


#df.shape[0]
    for i in range(1):
        short_str=df['Description'][i]
        long_str=df['Detailed Description'][i]
        if pd.isna(long_str):
            long_str=""
        user_dict['content']=short_str+long_str

        # print('{"messages": [{"role": "system", "content": "Given a news text, provide the following fields in a JSON dict, where applicable:')
        subset_df = df.loc[i, 'Risk to Human Rights':].to_dict()
        assistant_dict['content'] = str(subset_df)
        sum_dict_['messages']=[system_dict,user_dict,assistant_dict]
        # with open('data.jsonl', 'a') as json_file:
        #     json.dump(sum_dict_, json_file)
        #     json_file.write('\n')  # 在每个字典后面添加换行符
        print(subset_df)

        # print(df['Description'][0],df['Detailed Description'][0])
csv_to_json()


