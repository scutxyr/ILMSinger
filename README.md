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
网易云提供了歌词接口`http://music.163.com/api/song/lyric?id=song_id&lv=1&kv=1&tv=-1.`。所以我们只需获取一个歌单内或歌手的歌曲id，即可快速爬取歌词。通过requests方法读取网页div标签文件，找到歌曲id关键字后通过python程序进行网页爬取，具体方法见`get_lyrics.py`与`get_ids.py`
2. 进行数据的清洗与标准化。`lyric_data_processing`文件夹中包含了数据处理的相关文件，包括
3. 通过向InternLM2进行询问，得到对于每首歌歌词的内容总结和情感判断。
   格式化为"请创作一首{主题}，来表达{情感}"或"请创作一首表达{主题}"的文本，作为后续训练的问题输入。
<div align=center>
<img src=https://github.com/scutxyr/ILMSinger/blob/main/pic/process.png width=80% />
</div>

这样设计思路的目的与好处是：由于歌词语料是非对话语料，如何获得input内容是处理训练数据的一大难点。而让基座模型自行阅读歌词并给出输出，避免了人工标记（设计提问）的繁琐与可能导致的误差，确保input中的歌词主题与InternLM的内在逻辑所理解的主题相符，将更多的注意力集中在学习歌词本身上。  
　　从结果来看，这样的数据集输入在大多数提问之下可以实现可接受的微调效果。  
　　格式化训练集形如：  
<div align=center>
<img src=https://github.com/scutxyr/ILMSinger/blob/main/pic/data1.png width=90% />
</div>

## 微调设置
具体启动文件设置以及参数见`internlm_7b_qlora_lyricqa1_e3.py`
执行微调命令：
```
xtuner train ./internlm_chat_7b_qlora_lyricqa1_e3_copy.py  --deepspeed deepspeed_zero2
# 多卡
NPROC_PER_NODE=${GPU_NUM} xtuner train ./internlm_chat_7b_qlora_lyricqa1_e3.py
```
训练完成之后，转换参数为 HuggingFace 格式:
```
mkdir hf
export MKL_SERVICE_FORCE_INTEL=1
export MKL_THREADING_LAYER=GNU
xtuner convert pth_to_hf ./internlm_chat_7b_qlora_oasst1_e3_copy.py ./work_dirs/internlm_chat_7b_qlora_oasst1_e3_copy/epoch_1.pth ./hf
```
## 部署
合并模型：
`xtuner convert merge ./internlm-chat-7b ./hf ./merged --max-shard-size 2GB`
运行测试：
`xtuner chat ./merged --prompt-template internlm_chat`
几个重要参数：
```
--prompt-template # 若为InternLM2，需要更改对应参数，也可自定义
--temperature  # 对于生成歌词任务而言，温度值应适当调高，否则歌词过于保守重复
```
