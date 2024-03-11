# import json
#
# # 假设你的JSON文件名为'lyrics.json'
# file_name = 'lyric_train2.json'
#
# # 读取JSON文件
# with open(file_name, 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# # 替换换行符为逗号
# for i, line in enumerate(data):
#     data[i] = line.replace('\n', ',')
#
# # 将修改后的数据写回文件
# with open(file_name, 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)
#
# print("换行符已替换为逗号。")

import json
import re

# 假设你的JSON文件名为'lyrics.json'
file_name = 'lyric_train2_f.json'

# 读取JSON文件
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 定义正则表达式模式，用于匹配连续的逗号
pattern = re.compile(r',+')

# 处理每段歌词
for i, lyrics in enumerate(data):
    # 使用正则表达式替换连续的逗号为单个逗号
    data[i] = pattern.sub(',', lyrics)

# 将修改后的数据写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("连续的逗号已被替换为单个逗号。")