import json

MAX_LEN = 250

# 假设你的JSON文件名为'lyrics.json'
file_name = 'lyric_train2_cut.json'

# 读取JSON文件
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 处理每段歌词
for i, lyrics in enumerate(data):
    # 如果歌词长度超过MAX_LEN个字符
    if len(lyrics) > MAX_LEN:
        # 查找第一个逗号的位置
        comma_index = lyrics.find(',', MAX_LEN)  # 从第MAX_LEN个字符开始查找逗号
        # 如果找到了逗号，截断歌词
        if comma_index != -1:
            data[i] = lyrics[:comma_index + 1]  # 保留逗号

# 将修改后的数据写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("超过MAX_LEN字符的歌词已被截断。")