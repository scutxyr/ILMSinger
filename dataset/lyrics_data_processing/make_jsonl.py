import json

# 读取原始JSON文件
with open('lyric_train2_cut.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化输出列表
output_data = []

# 遍历data列表，创建新的对话对象
for item in data:
    conversation = {
        "conversation": [
            {
                "system": "你是一名说唱歌手，请按照要求创作说唱歌词",
                "input": "",
                "output": item
            }
        ]
    }
    output_data.append(conversation)

# 将结果写入新的JSON文件
with open('lyric_train2_line.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)

print("New JSON file created successfully.")