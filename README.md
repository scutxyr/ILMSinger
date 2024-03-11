# 歌王ILM —— 基于InternLM-7b的歌词创作大模型
歌王ILM是一个集成了多种语言说唱歌词的大语言模型。该模型使用截止至2023年的音乐平台说唱歌曲歌词作为数据集，基于 InternLM2-Math-7B 模型，通过 xtuner 微调，实现根据不同需求创造歌词的功能。  
<div align=center>
<img src=https://github.com/scutxyr/ILMSinger/blob/main/pic/title1.jpg width=280 height=180 />
</div>

# 简介
| 模型基座 | 微调方法 | 技术库 | 数据集来源 | 硬件支持
|:--------:| :-------------:|:-------------:|:-------------:|:-------------:|
| InternLM-Chat-7b / InternLM2-Chat-7b | QLoRA | Xtuner | 音乐平台公开歌词数据集+InternLM2 理解输出的主题 | (1/2) A100 |

# 模型实现
## 模型下载与环境配置
1. 下载InternLM-Chat-7b/InternLM2-Chat-7b模型，具体可见https://github.com/InternLM/InternLM
2. 配置xunter，标准配置方法如下：
```
git clone https://github.com/InternLM/xtuner.git
cd xtuner
pip install -e '.[all]'
```
## 数据集的获取与处理
1. 通过网易云平台爬取歌词。
网易云提供了歌词接口`http://music.163.com/api/song/lyric?id=song_id&lv=1&kv=1&tv=-1.`我们只需获取一个歌单内或歌手的歌曲id，即可快速爬取歌词。通过requests方法读取网页div标签文件，找到歌曲id关键字后通过python程序进行网页爬取，具体方法见`get_lyrics.py`与`get_ids.py`
2. 通过向InternLM2进行询问，得到对于每首歌歌词的内容总结和情感判断。
   格式化为"请创作一首{主题}，来表达{情感}"或"请创作一首表达{主题}"的文本，作为后续训练的问题输入。
   
