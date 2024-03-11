import json
import re

# 假设你的JSON文件名为'lyrics.json'
file_name = 'lyric_train2_f1.json'

# 读取JSON文件
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 定义正则表达式模式，用于匹配并删除作曲信息
# 这个模式会匹配"作曲:"后的所有内容，直到下一个逗号或行尾
pattern = re.compile(r'混音.*?,')

# 处理每段歌词
for i, lyrics in enumerate(data):
    # 使用正则表达式替换作曲信息
    data[i] = pattern.sub('', lyrics)

# 将修改后的数据写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("作曲信息已从每段歌词中删除。")