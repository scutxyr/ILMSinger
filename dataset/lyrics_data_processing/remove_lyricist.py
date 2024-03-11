import json
import re

# 假设你的JSON文件名为'lyrics.json'
file_name = 'lyric_train2_2.json'

# 定义正则表达式模式，用于匹配作词和作曲信息
pattern = re.compile(r'^(作词 : .*?, 作曲 : .*?,)')

# 读取JSON文件
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 处理每段歌词
for i, lyrics in enumerate(data):
    # 分割歌词为行
    lines = lyrics.split('\n')

    # 初始化新的歌词列表
    new_lines = []

    # 遍历每一行
    for line in lines:
        # 使用正则表达式匹配并删除作词和作曲信息
        new_line = pattern.sub('', line)
        # 如果行不为空，则添加到新的歌词列表中
        if new_line:
            new_lines.append(new_line)

    # 更新JSON数据中的歌词
    data[i] = '\n'.join(new_lines)

# 将修改后的数据写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("作词和作曲信息已从歌词的每一行中删除。")