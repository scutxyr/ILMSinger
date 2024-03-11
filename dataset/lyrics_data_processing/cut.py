import json
import re

# 假设你的JSON文件名为'lyrics.json'
file_name = 'lyric_train2try2.json'

# 读取JSON文件
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 定义正则表达式模式，用于匹配英文字母
pattern = re.compile(r'[a-zA-Z]')

# 处理每段歌词
for i, lyrics in enumerate(data):
    # 使用正则表达式替换英文字母为空字符串
    data[i] = pattern.sub('', lyrics)

# 将修改后的数据写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("所有歌词中的英文字母已被删除。")