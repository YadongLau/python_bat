#coding=utf-8

import os
import json
def change_label(filedir,name):
    #获取目标文件夹的路径

    #获取文件夹中的文件名称列表
    filenames = []
    for i in os.listdir(filedir):
        if i.endswith('.json'):
            filenames.append(i)
    #遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
        print(filepath)

        after = []
        # 打开文件取出数据并修改，然后存入变量
        with open(filepath, 'rb') as f:
            data = json.load(f)
            print(type(data))

            shapes = data["shapes"]
            for j in shapes:
                j["label"] = name

            after = data
            json_str = json.dumps(after, ensure_ascii=False, indent=4)

        # 打开文件并覆盖写入修改后内容
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(json_str)

if __name__ == '__main__':
    print("-----------------------------")
    print("此脚本用来修改json文件中标签的名字")
    print("-----------------------------")
    root_path = input("请输入要修改的json文件的路径:")
    input_name= input("请输入要修改的文件的名字：")
    name = input_name
    change_label(root_path,name=name)
