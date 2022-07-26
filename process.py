import os
import re

path = 'E:\Career\数据结构与算法\StudyAlgorithm\explain'
# for filepath,dirnames,filenames in os.walk(path):
#     for filename in filenames:
#         print(filename)

filenames=os.listdir(path)
print(filenames)

data = []
for filename in filenames:
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(path,filename)
    with open(filepath, encoding='utf-8') as f:
        tags = ''
        nd = ''
        for line in f.readlines():
            if '标签' in line:
                tags = re.findall('\[(.*?)\]', line)
                tags = ','.join(tags)
            elif '难度' in line:
                nd = re.findall('简单|中等|困难', line)
                nd = nd[0] if len(nd) > 0 else ''
            if tags and nd:
                break
    tmp = ['['+filename.strip('.md')+'](explain/'+filename+')', nd, tags]
    print(tmp)
    data.append(tmp)