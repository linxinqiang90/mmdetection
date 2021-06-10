import json
import os


exist_files = []
with open('/home/git/mmdetection/demo/jewelry_all_labels_my-project-name_2021-06-09-03-58-22.json','r',encoding='utf-8') as fp:
    json_data = json.load(fp)
    print(json_data['images'])
    files = []
    for item in json_data['images']:
        print(item)
        exist_files.append(item['file_name'])

print(len(exist_files))
files = os.listdir("/home/linxinqiang/Desktop/dataset/jewelry_all/")
for exist_file in exist_files:
    files.remove(exist_file)

print(len(files))
for file in  files:
    os.rename("/home/linxinqiang/Desktop/dataset/jewelry_all/"+file,file)

