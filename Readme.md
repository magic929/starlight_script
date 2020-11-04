# starlight relive 脚本
## 事前准备
- 下载代码（已安装git）
```bash
git clone https://github.com/magic929/starlight_script.git
```

没有安装的话，下载zip文件后解压
- 下载python3
```bash
brew install python
```

windows的话网上搜一下怎么下载
- 准备虚拟环境
使用vscode的情况  

安装虚拟环境
```bash
python3 -m venv .venv
```

进入虚拟环境
```bash
. .venv/bin/activate
```

安装依赖包
```bash
pip3 install -r rquirements.txt
```

准备活动结束
## 工具介绍
### 工会排刀顺序
执行
```python
python sort.py [json_file_name]
```

json_file_name: 输入boss血量和成员伤害的文件，形式如下

```json
{
    "boss": 血量,
    "team": [
        {
            "id": 成员名字,
            "damage": 成员伤害
        },
        {
            "id": ,
            "damage":
        },
        ...
    ]
}
```

使用注意：输入为万单位的整数
