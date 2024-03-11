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
2. 配置xunter,标准配置方法如下：
```
git clone https://github.com/InternLM/xtuner.git
cd xtuner
pip install -e '.[all]'
```
