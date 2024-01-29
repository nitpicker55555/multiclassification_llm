import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
def draw_pic(nested_dict,value_dict,name,mode="total"):
    def find_indices(lst, element):
        """Find all indices of `element` in the list `lst`."""
        return [i for i, x in enumerate(lst) if x == element]
    def order_dict_keys(list1,dict2):

        ordered_dict2 = {key: dict2[key] for key in list1}
        return ordered_dict2

    def extract_elements_and_parents(nested_dict, parent="", elements=None, parents=None):

            # 初始化元素和父级列表
            if elements is None:
                elements = []
            if parents is None:
                parents = []

            # 遍历嵌套字典
            for key, value in nested_dict.items():
                # 添加键及其父级
                elements.append(key)
                parents.append(parent)

                # 如果值是字典，则递归调用函数
                if isinstance(value, dict):
                    extract_elements_and_parents(value, parent=key, elements=elements, parents=parents)
                # 如果值是集合，则添加集合中的元素及其父键
                elif isinstance(value, set):
                    for item in value:
                        elements.append(item)
                        parents.append(key)

            return elements, parents


    character,parents=extract_elements_and_parents( {"root": nested_dict})
    print(character)
    print(parents)
    root_value=2000
    value_dict['root']=root_value
    percentage_label={"root":1.0}

    if mode=="total":
        branchvalues="total"
        level_dict={}
        for num,i in  enumerate(parents):
            if i not in level_dict:
                level_dict[i]=0
            level_dict[i]+=value_dict[character[num]]

        for num, i in enumerate(parents):
            if i!="":
                #character[num] element label
                #value_dict[i] parent value
                #level_dict[i] level value sum
                #value_dict[character[num]] element value

                value_dict[character[num]]= value_dict[i]*((value_dict[character[num]]/level_dict[i]))
                percentage_label[character[num]]=value_dict[character[num]]/level_dict[i]
        level_dict={}
        for num,i in  enumerate(parents):
            if i not in level_dict:
                level_dict[i]=0
            level_dict[i]+=value_dict[character[num]]
        processed_num=[]
        for num, i in enumerate(parents):
            if i != "" and num not in processed_num:
                processed_num.append(num)
                sum_level=0
                index_list= find_indices(parents,i)
                for index_ in index_list:
                    sum_level+=value_dict[character[index_]]
                print(i,sum_level,value_dict[i],value_dict[i]-sum_level)
                value_dict[character[index_list[-1]]]+=(value_dict[i]-sum_level)
    else:
        branchvalues="reminder"

    print({k: v for k, v in zip(character, parents)})
    value=[value_dict[i] for i in character]

    orderd_percentage_dict=list(order_dict_keys(character,percentage_label).values())

    # data = dict(
    #     character=character,
    #     parent=parents,
    #     value=value,
    #     additional_info= orderd_percentage_dict
    # )

    # fig = px.sunburst(
    #     data,
    #     names='character',
    #     parents='parent',
    #     values='value',
    #     branchvalues=branchvalues,
    # )
    data = pd.DataFrame({
        'id': character,
        'parent': parents,
        'value': value,
        'additional_info': orderd_percentage_dict
    })
    data['additional_info'] = data.apply(lambda row: f"Info: {row['additional_info']}", axis=1)
    fig = go.Figure(go.Sunburst(
        ids=data['character'],
    labels=data['character'],
        parents=data['parent'],
        values=data['value'],
        branchvalues=branchvalues,
        text=data['additional_info'],  # 使用额外信息作为文本
        textinfo='label+text'  # 显示标签、文本和百分比
    ))

    fig.show()
    # pio.write_html(fig, file='tem_file\\sunburst_%s.html'%name)
