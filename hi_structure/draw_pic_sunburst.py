import plotly.express as px
import plotly.io as pio
def draw_pic(nested_dict,value_dict,name,mode="total"):
    def find_indices(lst, element):
        """Find all indices of `element` in the list `lst`."""
        return [i for i, x in enumerate(lst) if x == element]
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
    if mode=="total":
        branchvalues="total"
        level_dict={}
        for num,i in  enumerate(parents):
            if i not in level_dict:
                level_dict[i]=0
            level_dict[i]+=value_dict[character[num]]
        for num, i in enumerate(parents):
            if i!="":
                value_dict[character[num]]= value_dict[i]*((value_dict[character[num]]/level_dict[i]))
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

    data = dict(
        character=character,
        parent=parents,
        value=value,

    )

    fig = px.sunburst(
        data,
        names='character',
        parents='parent',
        values='value',
        branchvalues=branchvalues
    )
    # fig.show()
    pio.write_html(fig, file='tem_file\\sunburst_%s.html'%name)
