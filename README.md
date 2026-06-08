# 易易的作业

## 环境配置

### 1. 创建 Conda 虚拟环境

```bash
conda create -n ai-python-study python=3.12 -y
```

### 2. 激活环境并安装依赖

```bash
conda activate ai-python-study
pip install numpy pandas
```

### 3. 在 PyCharm 中配置解释器

打开 PyCharm，进入 **Settings → Project → Python Interpreter**，选择已存在的 Conda 环境 `ai-python-study`。

> 如果 PyCharm 没有自动识别该环境，可以手动添加：
> 点击齿轮图标 → **Add** → **Conda Environment** → **Existing environment** →
> 选择 conda 安装目录下 `envs/ai-python-study/bin/python`。

### 各题目依赖说明

| 题目 | 依赖库 |
|------|--------|
| 第1题 | 无（Python 标准库） |
| 第2题 | 无（Python 标准库） |
| 第3题 | 无（Python 标准库） |
| 第4题 | numpy, pandas |
| 第5题 | pandas |

---

### 4. 运行测试

本项目使用 pytest 进行单元测试。

```bash
# 安装测试依赖
pip install -r requirements.txt

# 运行所有测试
python -m pytest tests/ -v

# 运行单个题目的测试
python -m pytest tests/test_1_count_char.py -v
```

测试覆盖了每道题目的核心逻辑，包括边界情况和错误处理。

---

## 1. 题目
1.给定一个字符串 s1，找到里面出现 c的次数(忽略大小写），并利用字符串的格式化，打印出：”
c出现了× 次”打印出来(其中，×为出现的次数）。

 
`st =welcome to China. China is a great country. Chinese people love to buy china!`
`#输出应为：”c出现了 6次”`

## 2. 题目：生成列表 listl = ［2,3,5,7,9，［2,4,6,8］］，请基于list1完成以下操作：
 1）. 获取5这个值 
 
 2）.获取切片［4,6,8］

## 3. 题目： 函数和字符串练习：写一个函数使得给一个超过5位的字符串s，其长度是奇数时打印中间3位数，其长度是偶数时打印中间两位数。请利用函数实现(字符串为函数的参数输入）。

 举例：

 `Sr'abadefg 时的输出为："cde"# s-'abodef'时的输出为："cd""`
 
## 4.  题目：利用以下代码生成一个 DataFrame，列名分别为 A,B,C,D。其中，A列为从2开始的15个连续偶数(246,8..），B列为符合标准正态分布的15个随机数，C列为10-100之间的15个随机数，
D列为符合50为均值，10为方差的15个随机数。

`dict = 'A':n.arange/2,32,2), B:p.random.rand(15), 'C:np.random.randint(10,101,15), D':np.ra
ndom.normal (50,10,1 5)} df=pd.DataFrame(dict1)
`

    完成以下操作：

1） 获取第4行的数据

2） 提取第3行、第5行与列B,D的交叉部分

3） 删除A 列值为16的那一行记录

## 5.  题目：利用上传的银行客户数据(BankCustomer Data.csv），完成下列操作。

1）查看有哪些变量

2） 查看所有变量的数据类型

3） 在原 DataFrame 中，删除job为 unknown 的行

4）新生成一列year，赋值为字符串格式的“2025”

5） 连接 year，month 2 个变量生成新的变量ym，为字符串格式，用-符号链接。

    例： 
    `2025-aug(字符串和字符串的连接可以用+）`

6） 利用 loc 命令提取出 age大于60且 job 为 retired 的记录，放入到一个名为 group1 的 DataFrame 中。