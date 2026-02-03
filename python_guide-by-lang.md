# Python入门指南（面向C/Java/JS开发者）

> 作者：Lang  
> 目标读者：有C/Java/JavaScript开发经验的工程师  
> 重点：突出Python的特别之处，以及与其他语言的对比

---

## 目录

- [第0章：开始之前 - 环境准备](#第0章开始之前---环境准备)
  - [Python虚拟环境管理](#python虚拟环境管理)
- [第1章：Entry Level - 必须掌握](#第1章entry-level---必须掌握)
- [第2章：Middle Level - 最佳实践](#第2章middle-level---最佳实践)
- [第3章：Advanced Level - 进阶技巧](#第3章advanced-level---进阶技巧)
- [专题：*args和**kwargs详解](#专题args和kwargs详解)
- [附录](#附录)

---

## 第0章：开始之前 - 环境准备

开始**可先跳过**，只要安装python 3.10+版本，从第一章开始，等有多个项目，不同环境要求再回来看这章。

### Python虚拟环境管理

#### 为什么需要虚拟环境？

**问题场景**（你会理解的类比）：
- **Java**: 不同项目用不同版本的Spring Boot → 用Maven/Gradle隔离
- **Node.js**: 不同项目用不同版本的React → 每个项目有自己的node_modules
- **Python**: 不同项目用不同版本的Django → **需要虚拟环境**

```python
# 没有虚拟环境的问题
项目A需要: Django 3.2
项目B需要: Django 4.2
全局只能装一个版本 ❌

# 虚拟环境的解决方案
项目A的虚拟环境: Django 3.2 ✅
项目B的虚拟环境: Django 4.2 ✅
```

---

#### Entry Level - 必须掌握

##### 1. venv（Python内置，推荐新手）

```bash
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
# Windows:
myenv\Scripts\activate

# Mac/Linux:
source myenv/bin/activate

# 确认已激活（命令行前面会显示环境名）
(myenv) $ 

# 安装包（只在当前虚拟环境中）
pip install requests

# 退出虚拟环境
deactivate
```

**关键概念**：
- 虚拟环境就是一个独立的Python副本
- 激活后，`pip install` 只影响当前环境
- 不同项目用不同的虚拟环境文件夹

##### 2. 基本工作流

```bash
# 典型的项目开始流程
cd my_project
python -m venv venv          # 创建
source venv/bin/activate     # 激活（Mac/Linux）
pip install -r requirements.txt  # 安装依赖

# 开发...

deactivate  # 结束工作
```

##### 3. requirements.txt（依赖管理）

```bash
# 导出当前环境的依赖
pip freeze > requirements.txt

# requirements.txt内容示例：
# requests==2.31.0
# numpy==1.24.3
# pandas==2.0.2

# 在新环境中安装相同依赖
pip install -r requirements.txt
```

**对比其他语言**：
- Node.js: `package.json` + `npm install`
- Java: `pom.xml` / `build.gradle`
- Python: `requirements.txt` + `pip install`

---

#### Middle Level - 推荐掌握

##### 4. 更现代的工具：Poetry

```bash
# 安装Poetry（全局安装一次）
curl -sSL https://install.python-poetry.org | python3 -

# 创建新项目
poetry new my_project
cd my_project

# 添加依赖（自动管理虚拟环境）
poetry add requests
poetry add pytest --group dev  # 开发依赖

# 安装所有依赖
poetry install

# 运行命令（自动使用虚拟环境）
poetry run python main.py

# 导出requirements.txt（兼容性）
poetry export -f requirements.txt --output requirements.txt
```

**Poetry的优势**：
- 自动管理虚拟环境，不需要手动激活
- `pyproject.toml` 类似 `package.json`，更现代
- 依赖解析更智能

**对比**：
```
venv + pip:          Poetry:
手动创建venv         自动创建
手动激活            自动使用
requirements.txt    pyproject.toml（更丰富）
```

##### 5. 多Python版本管理：pyenv

```bash
# 安装pyenv（Mac）
brew install pyenv

# 安装不同版本的Python
pyenv install 3.10.13
pyenv install 3.11.5

# 为项目设置特定版本
cd my_project
pyenv local 3.10.13

# 配合venv使用
python -m venv venv  # 使用3.10.13创建
```

**类比**：
- Node.js: `nvm`（Node Version Manager）
- Python: `pyenv`

---

#### Advanced Level - 了解即可

##### 6. 其他工具对比

| 工具 | 适用场景 | 学习曲线 |
|------|---------|---------|
| venv | 简单项目，新手 | 低 |
| virtualenv | venv的加强版，老项目 | 低 |
| Poetry | 现代项目，团队协作 | 中 |
| pipenv | 曾经流行，现在较少用 | 中 |
| conda | 数据科学，非Python依赖多 | 高 |

##### 7. Docker中的虚拟环境

```dockerfile
# Dockerfile中不需要虚拟环境
FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt  # 直接全局安装

COPY . .
CMD ["python", "main.py"]
```

**原因**：Docker容器本身已经是隔离环境

##### 8. uv

uv 是目前最新，最流行的python 包安装和虚拟环境管理工具。2026可以跳过上面其他工具，直接了解、使用uv

但有这么多工具完成类似的任务也从另一个侧面说明 Python虚拟环境管理处在一个相对“混乱”的局面

---

#### 实践建议

**第一天**：
- 学会创建venv
- 学会激活/退出
- 理解 `requirements.txt`

**第一周后**：
- 尝试Poetry（如果团队使用）
- 了解pyenv（如果需要多版本）
- 或者直接尝试最新的 uv

**遇到问题时**：
- `.gitignore` 要忽略虚拟环境文件夹（通常是 `venv/`, `env/`）
- IDE（VS Code, PyCharm）要配置使用虚拟环境的Python解释器

---

#### 常见问题

**Q: 虚拟环境要提交到Git吗？**  
A: ❌ 不要！只提交 `requirements.txt` 或 `pyproject.toml`

**Q: 每个项目都要新建虚拟环境吗？**  
A: ✅ 是的，保持隔离

**Q: 虚拟环境在哪里？**  
A: 通常在项目根目录的 `venv/` 或 `env/` 文件夹

**Q: 忘记激活虚拟环境就 `pip install` 了？**  
A: 包会装到全局，可能污染系统Python。最好重新在虚拟环境中装一次

---

## 第1章：Entry Level - 必须掌握

> 这些是你必须立即掌握的内容，否则无法写Python代码
>
> 注意，缩进定义代码块；单行注释用 # ；布尔值（True/False）这些最基本的语法假定已经知晓

### 1. 没有传统for循环，使用for-in遍历

```python
# ❌ C/Java/JS 风格（Python不支持）
# for (i=0; i<n; i++)

# ✅ Python 风格
for i in range(n):
    print(i)

# 只为重复 n 遍，不关心索引的值   
for _ in range(n):
    print("执行操作")

# 遍历列表
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# 需要索引时
for i, name in enumerate(names):
    print(f"{i}: {name}")
    
# 参见 19. zip 同时遍历n个列表
```

---

### 2. 没有do-while，用while配合海象运算符

没有do-while ，需要至少执行一次，用 `:=` 运算符 (3.8+)

```python
# ❌ C/Java 风格（Python不支持）
# do {
#     line = input();
# } while (line != "quit");

# ✅ Python 3.8+ 海象运算符
while (line := input("Enter command: ")) != "quit":
    print(f"You entered: {line}")

# 传统写法（仍然常用）
line = input("Enter command: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter command: ")
```
---

### 3. list（列表）和 tuple（元组）的区别

```python
# list（列表）- 可变的动态数组
numbers = [1, 2, 3, 4]
numbers.append(5)        # 可以添加
numbers[0] = 10          # 可以修改
numbers.pop()            # 可以删除
print(numbers)           # [10, 2, 3, 4]

# tuple（元组）- 不可变的序列
coordinates = (10, 20, 30)
# coordinates[0] = 5     # ❌ TypeError: 'tuple' object does not support item assignment
# coordinates.append(4)  # ❌ AttributeError: 'tuple' object has no attribute 'append'
print(coordinates[0])    # ✅ 可以读取: 10

# 创建tuple的注意事项，Python解释器判断是否是tuple的唯一标准是逗号，不是括号！
single = (1,)            # ✅ 单元素tuple(one-element tuple)，习惯写法：带逗号
not_tuple = (1)          # ❌ 这只是整数1，不是tuple（括号只是分组）
result = (1 + 2) * 3     # 括号用于改变运算优先级
x = (5)                  # 括号没有任何作用，x就是5
also_tuple = 1,          # ✅ 技术上也是tuple，但可读性差
empty = ()               # 空tuple（基础用法见Middle Level）

# 什么时候用list，什么时候用tuple？
user_list = ["Alice", "Bob", "Charlie"]  # 同类数据的集合，可能增删
user_info = ("Lang", 25, "Beijing")      # 固定结构的数据，像一条记录

# tuple可以作为字典的key（因为不可变）
locations = {
    (0, 0): "原点",
    (1, 2): "坐标A"
}
# list不能作为字典的key
# bad_dict = {[1, 2]: "value"}  # ❌ TypeError: unhashable type: 'list'
```

**对比其他语言**：

| 概念 | Java | JavaScript | C | Python |
|------|------|-----------|---|--------|
| 动态数组 | `ArrayList<T>` | `Array` | - | `list` |
| 不可变序列 | - | - | - | `tuple` |
| 固定数组 | `T[]` | - | `T[]` | - |

**关键区别**：
- **list**: 可变，用`[]`，类似Java的`ArrayList`或JS的`Array`
- **tuple**: 不可变，用`()`，类似只读数组，但其他语言没有直接对应物
- **逗号定义tuple**: `(1,)` 是tuple，`(1)` 只是整数1
- **性能**: tuple略快且占用内存更少（因为不可变）
- **用途**: list用于同质集合，tuple用于异构记录

```python
# 典型用法示例

# list - 收集同类数据
scores = [85, 92, 78, 95]
scores.append(88)  # 可以动态添加

# tuple - 表示固定结构（像数据库的一行）
person = ("Lang", 25, "Beijing", "Engineer")
name, age, city, job = person  # 解包

# 函数返回“多个值”，实际上返回的是tuple
def get_user():
    return "Lang", 25, "Beijing"  # 实际返回 ("Lang", 25, "Beijing")

name, age, city = get_user()  # 解包tuple
```
**列表赋值是引用传递，而非值拷贝**

```python
# 陷阱示例
list1 = [1, 2, 3]
list2 = list1  # list2 和 list1 指向同一个对象！

list2.append(4)
print(list1)  # [1, 2, 3, 4] - list1 也被修改了！
print(list2)  # [1, 2, 3, 4]
print(list1 is list2)  # True - 它们是同一个对象

# 函数可以修改传入的列表
def add_item(my_list, item):
    my_list.append(item)  # 修改原列表！
    return my_list

original = [1, 2, 3]
result = add_item(original, 4)

# 复制list的正确做法
list1 = [1, 2, 3]
list2 = list1[:]  # 创建副本
# 或者
list2 = list(list1)  # 创建副本

# len()函数，获取长度（通用）
len("hello")        # 5
len([1, 2, 3])      # 3
len((1, 2))         # 2
len({"a": 1})       # 1
```

---

### 4. 字典（dict）是核心数据结构

```python
# 字典（类似Java的HashMap，JS的Object）
user = {"name": "Lang", "age": 25}
print(user["name"])
print(user.get("city", "Unknown"))  # 带默认值，不存在时不报错

# 添加/修改
user["job"] = "Engineer"
user["age"] = 26

# 删除
del user["age"]
# 或者
user.pop("job", None)  # 带默认值，不存在时不报错

# 检查key是否存在
if "name" in user:
    print(user["name"])

# 遍历
for key in user:
    print(key, user[key])

# 更Pythonic的遍历方式
for key, value in user.items():
    print(f"{key}: {value}")
```

**对比其他语言**：
- **Java**: `HashMap<K,V>` - 需要导入，泛型声明
- **JavaScript**: `Object` 或 `Map` - Object的key只能是字符串
- **Python**: `dict` - 内置类型，key可以是任何不可变类型（字符串、数字、tuple）

```python
# Python dict的灵活性
mixed_keys = {
    "string_key": 1,
    42: "integer_key",
    (1, 2): "tuple_key",
    # [1, 2]: "error"  # ❌ list不能作为key（可变）
}
```
---

### 5. 切片和负索引

切片语法 `[start:stop:step]`， 切片不仅 `list` 和 `tuple`，Python 中所有**序列类型**（`str`、`bytes`、`range` 等）都支持切片和负索引，这是**序列协议（Sequence Protocol）** 的一部分。

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr[2:5]      # [2, 3, 4] - 不包含结束索引
arr[:3]       # [0, 1, 2] - 从开头
arr[7:]       # [7, 8, 9] - 到结尾
arr[::2]      # [0, 2, 4, 6, 8] - 步长为2
arr[-1]       # 9 - 最后一个元素
arr[-3:]      # [7, 8, 9] - 最后三个
arr[::-1]     # 反转列表
```

---

### 6. 多重赋值和解包

```python
# 交换变量（无需临时变量）
a, b = b, a

# 多重赋值
x, y, z = 1, 2, 3

# 解包
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

# 函数返回多个值
def get_user():
    return "Lang", 25, "Beijing"

name, age, city = get_user()
```

---

### 7. 动态类型但强类型，无隐式转换，提供类型转换函数

```python
# ❌ 会报错（不像JS）
result = "3" + 5  # TypeError

# ✅ 需要显式转换
result = "3" + str(5)  # "35"
result = int("3") + 5  # 8


# 基本类型转换
int("123")      # 123
int("3.14")     # ValueError（不能直接转）
int(3.14)       # 3（向下取整）
float("3.14")   # 3.14
str(123)        # "123"
bool(0)         # False
bool(1)         # True
bool("")        # False
bool("hello")   # True

# 容器转换
list("abc")         # ['a', 'b', 'c']
tuple([1, 2, 3])    # (1, 2, 3)
set([1, 2, 2, 3])   # {1, 2, 3}（去重）
dict([("a", 1)])    # {"a": 1}
```

---

### 8. 为什么计数应该从0开始

这个知识点是我的个人喜好。 C/Java/js/python都是 zero-indexing. 

#### 半开区间表示序列更好

最经典的解释还是 https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD831.html Dijkstra 1982年的短文。

但是我个人觉得他的解释有些拗口和啰嗦，尤其最小的自然数是 1 ，但是他的文章说 "And the moral of the story is that we had better regard —after all those centuries!— **zero as a most natural number**" 但他的例子能说明问题：

为了表示 2... 12 这一组数字，有四种记录方法

```
1. 2 ≤ i < 13
2. 1 < i ≤ 12
3. 2 ≤ i ≤ 12
4. 1 < i < 13
```

1 & 2 （**半开区间**）好处是 元素的个数可以用上下边界值相减 (`13-2` 或者 `12-1`)  半开区间的第二个好处是把这个区间拆分成相邻的两个区间，这个前一个区间的上边界值等于后一个区间的下边界值，不需要额外处理。但是在论述下边界(lower bound)  该用 `≤` 而上边界（higher bound）该用 `<` 我觉得有点啰嗦。

1 & 3 好处 从0 开始的区间不需要起始下标为负数（用从1 开始的区间不需要用0），Dijkstra的话是 2和4会 forces for a subsequence starting at the smallest natural number the lower bound as mentioned into the realm of the unnatural numbers. (很拗口)，所以这两条就能让我们选 `[a,b)` 这种半开区间形式，即下边界(lower bound)  该用 `≤` 

Dijkstra 进一步论述 1 & 4 好处是起始下标为0的**空区间**，上边界不需要是负数；也就是说上边界（higher bound）用`≤` 的2 & 3 情况，当表示起始下标为0的**空区间**的时候就需要用负数。 所以 上边界（higher bound）该用 `<` ， Dijkstra 基于以上三条理由选择第一种形式。

注意"左闭右开区间"常见的 one - off bug，比如取字符串的最后一个字母的下标是 [length-1]; 但这不是 0-indexed 的缺陷。

#### 0-based 

他解释了半开区间的选择后再进一步解释为什么是 0 based （我也觉得不是那么好懂）。基于以上讨论，记录 N 个数的序列形式可以是 `[0,N)` 或者 `[1,N+1)`   用 [0,N)的好处是，序列中第[x] 元素表示，前面有x个值 (index = offset from start). 所以跳过前面N个数就可以直接从 [N] 开始，比如2023 年入学，大三是从2025开始而不是2026.

为什么 0-based 更好可以有这些补充解释：

1. 0-based **上边界值就是区间长度**: `[0, length)` 长度是 length. 
2. 表示空区间 [0,0) 比 [1,1) 既然是空区间，为什么从1开始？
3. 上面讨论半开区间好处之一是把这个区间拆分成相邻的两个区间，前一个区间长度是M：如果用 0-based, 可以直接处理为 `[0, M)` 和 `[M,N)` 但是如果1-based  需要额外处理  `[1, M+1)` 和 `[M+1,N)`   0-based 让区间运算方便

#### python 解决办法

1. `for i in range(n)`  range(n) # 不需要关心是 0-9 还是 1-10
2. 负索引 `s[-1]` 访问最后一个元素
3. `arr[2:5]`   注意是 `[2,5`

---

### 9. 逻辑运算

#### 1. 逻辑运算符是单词

```python
# ❌ C/Java/JS 风格
# if (x > 0 && x < 10 || !found)

# ✅ Python 风格
if x > 0 and x < 10 or not found:
    pass

# 链式比较（Python特有）
if 0 < x < 10:  # 等同于 x > 0 and x < 10
    pass
```


#### 2. 三元运算符 (Ternary Operator)

Python 的三元运算符（也称条件表达式）

```python
# ❌ C/Java/JS 风格
result = condition ? value_if_true : value_if_false
# ✅ Python 风格
result = value_if_true if condition else value_if_false

# 等价的 if-else 写法
if condition:
    result = value_if_true
else:
    result = value_if_false

# 示例
number = 7
parity = "奇数" if number % 2 != 0 else "偶数"
print(parity)  # 奇数

# 比较大小
a, b = 10, 20
max_value = a if a > b else b
print(max_value)  # 20

# 判断成绩等级
score = 85
grade = "及格" if score >= 60 else "不及格"
```

#### 3. in and not in 成员检测运算符，比手动循环更 Pythonic。

```
# 基础用法（支持 list, tuple, set, dict, str）
if "error" in log_text: ...           # 子串检测
if user_id in active_users: ...       # 存在于集合
if key not in config: ...             # 不存在判断

# 没有 in 操作符的替代方案（丑陋但可行）
found = False
for item in container:                # 手动遍历（C 语言风格）
    if item == target:
        found = True
        break
```

#### 4. is vs ==

```
# == 比较值是否相等
# is 比较是否是同一个对象（内存地址是否相同）

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - 值相等
print(a is b)  # False - 不是同一个对象
```

**None的判断用is而非==**

| **语言**   | **空值关键字**                                | **推荐判断方式**                  |
| ---------- | --------------------------------------------- | --------------------------------- |
| **Python** | `None` 是单例，用 is 更快更安全               | `if x is None:`                   |
| **Java**   | `null`  最常见的错误就是 NullPointerException | `if (x == null)`                  |
| **JS**     | `null / undefined` 存在两种空值               | `if (x === null)`                 |
| **C**      | `NULL` 本质上通常是 `0`                       | `if (x == NULL)` 或者 `if (!ptr)` |

```python
# ✅ 推荐
if value is None:
    print("No value")

if value is not None:
    print("Has value")

# ❌ 可以工作但不符合惯例
if value == None:
    pass
```

---

### 10. 字符串不可变（immutable）

```python
# ⚠️ 字符串是不可变的，任何修改都会创建新字符串

# ❌ 不能修改字符串中的字符
text = "hello"
# text[0] = "H"  # TypeError: 'str' object does not support item assignment

# ✅ 修改字符串会创建新对象
text = "hello"
text = text.upper()  # 创建新字符串 "HELLO"
text = text + " world"  # 创建新字符串 "HELLO world"

# 性能影响：大量拼接时效率低
# ❌ 低效（每次循环都创建新字符串）
result = ""
for i in range(1000):
    result += str(i)  # 创建1000个临时字符串对象

# ✅ 高效（用列表收集，最后join）
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)  # 只创建一次最终字符串

# 也可以用生成器表达式
result = "".join(str(i) for i in range(1000))
```

**对比其他语言**：
- **Java**: `String`不可变，`StringBuilder`可变
- **C**: 字符数组可变
- **JavaScript**: 字符串不可变（与Python相同）
- **Python**: 字符串不可变，没有专门的可变字符串类型（用list代替）

#### 字符串常用方法举例

```
text = "  Hello, Python World  "

# 清理
text.strip()            # "Hello, Python World"（去两端空白）
text.lstrip()           # 去左边
text.rstrip()           # 去右边

# 分割与连接（对比其他语言很方便）
words = text.split()    # ["Hello,", "Python", "World"]（默认按空白分割）
csv = "a,b,c".split(",") # ["a", "b", "c"]

# 连接
"-".join(["2024", "01", "30"])  # "2024-01-30"

# 检查（比正则表达式简单场景更好用）
text.startswith("Hello")
text.endswith("World")
"Python" in text        # 成员检测（任何序列类型都支持）

# 大小写
text.lower()
text.upper()
text.title()            # "Hello World"（每个单词首字母大写）

# 替换（不是原地修改，返回新字符串！）
new_text = text.replace("Python", "Java")  # 原 text 不变
```
#### 长字符串的生成方式

```
 s = ("this is a very"
      "long string too"
      "for sure ..."
     )
 # 但下面这样可避免 query == "SELECT fooFROM barWHERE baz" 
 query = ' '.join((  # note double parens, join() takes an iterable
    "SELECT foo",
    "FROM bar",
    "WHERE baz",
  ))
```

---

## 第2章：Middle Level - 最佳实践

> 这些特性显著提升代码质量和效率。
>
> 注意，有很多写法属于语法糖 syntax sugar ，让代码更有 python 味道 (Pyhonic), 但是用“很笨”写法也能实现相同的功能

### 11. `if __name__ == "__main__"`模式

对于**一次性、确定性、不会被导入**的脚本，可以省略忽略这样写法 （**"main guard"**），但它仍然上一个好习惯，你将**脚本逻辑**和**模块逻辑**分离：

```python
# my_module.py
def useful_function():
    return "I can be imported"

# 这部分只在直接运行时执行，被导入时不执行
if __name__ == "__main__":
    print("Running as script")
    result = useful_function()
    print(result)
```

---

### 12. 列表/字典推导式 List Comprehension

```python
# 列表推导
squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# 等价的传统写法
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# 字典推导
word_lengths = {word: len(word) for word in ['cat', 'dog', 'elephant']}
# {'cat': 3, 'dog': 3, 'elephant': 8}

# walrus运算符的高级用法， 列表推导中避免重复计算
results = [y for x in data if (y := expensive_function(x)) is not None]

# 等价但效率较低的写法
results = [expensive_function(x) for x in data if expensive_function(x) is not None]

```

---

### 13. f-string格式化（Python 3.6+）

```python
name = "Lang"
age = 25

# ✅ f-string（推荐）
message = f"My name is {name}, I'm {age} years old"

# 表达式和格式化
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # "Pi is approximately 3.14"

# 老式方法（了解即可）
message = "My name is %s, I'm %d years old" % (name, age)
message = "My name is {}, I'm {} years old".format(name, age)
```

---

### 14. 函数参数的灵活性

```python
# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Lang")               # "Hello, Lang!"
greet("Lang", "Hi")         # "Hi, Lang!"
greet("Lang", greeting="Hey")  # 关键字参数

# *args 和 **kwargs（详见专题章节）
def log(level, *messages, **metadata):
    print(f"[{level}]", " ".join(messages))
    for key, value in metadata.items():
        print(f"  {key}: {value}")

log("INFO", "User", "logged", "in", user_id=123, ip="192.168.1.1")
# [INFO] User logged in
#   user_id: 123
#   ip: 192.168.1.1
```

---

### 15. with语句（上下文管理器）

为什么用 with？

1.  自动清理资源（文件、网络连接、锁等）
2. 即使出现异常也能正确关闭
3. **with + try-except** - 相当于 java/js 的 `try catch finally `

| 概念     | JavaScript       | Python             | 备注          |
| -------- | ---------------- | ------------------ | ------------- |
| 异常处理 | try-catch        | try-except         | 语法几乎相同  |
| 资源管理 | finally 手动清理 | with 语句 自动关闭 | ⭐ Python 优势 |
| 文件操作 | 需要手动 close   | with 语句 自动关闭 | ⭐ Python 优势 |

```python
# ✅ Python风格 - 自动关闭文件
with open("data.txt", "r") as f:
    content = f.read()
# 文件在这里已自动关闭

# ❌ C/Java风格（可以但不推荐）
f = open("data.txt", "r")
content = f.read()
f.close()

# 多个资源
with open("input.txt") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read())
    
# 结合异常处理
try:
    with open("config.json") as f:
        data = f.read()
except FileNotFoundError:
    data = get_default_config()
```

finally 仍然很有用，但用途和 with 不同：

1. with: 管理资源（文件、连接、锁）→ 90% 的清理场景
2. finally: 恢复状态、记录日志、清理标志位 → 10% 的场景

---

### 16. match-case（Python 3.10+）

match-case vs switch case

1. match-case 匹配后自动退出， 对比 JavaScript/C/Java 默认穿透, 需要对每个case 添加break.
2. 其他语言利用穿透(Fall through) 行为相反的惯用法（故意不写 break），对比 match-case 用 OR 模式

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403:  # 多个值
            return "Authentication error"
        case _:  # 默认情况
            return "Unknown error"

# 等价的传统Python写法（3.10之前）
def process_command_old(status):
    if status == 400:
        return "Bad request"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Unknown error"
      
# ❌ 不适合用 match-case（用 if-elif 更好）：
# 1. 范围判断
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
# match无法直接表达范围

# 2. 复杂的布尔条件
if user.is_authenticated and user.is_admin:
    # ...
elif user.is_authenticated:
    # ...
```

---

### 17. Lambdas

lambdas 是一行的匿名函数， Lambdas are one-line anonymous functions. 

`lambda` 是**表达式**（Expression），而 `def` 是**语句**（Statement）。这意味着 lambda 可以出现在任何需要值的地方，而 def 不行

```python
# ✅ Lambda 作为表达式，可以内联
result = sorted(users, key=lambda x: x['age'])

# ❌ Def 不能内联，必须预先定义
sorted(users, key=def get_age(x): return x['age'])  # SyntaxError

# 使用lamda 排序
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
top_scorers = sorted(students, key=lambda x: x[1], reverse=True)

# 不使用lamda 实现同样功能的代码
def score_func(student):
    return student[1]
top_scorers = sorted(students, key=score_func, reverse=True)
```
回调函数， 比如GUI 响应代码用lamda简化代码

```
button.on_click(lambda: print("Button clicked!"))

#不用 lamdba
def on_button_click():
    print("Button clicked!")
button.on_click(on_button_click)
```

| 特性        | Lambda              | Def           |
| --------- | ------------------- | ------------- |
| **多行逻辑**  | ❌ 只能单一表达式           | ✅ 任意语句块       |
| **类型注解**  | ❌ 不支持               | ✅ 支持          |
| **文档字符串** | ❌ 无 `__doc__`       | ✅ 有 docstring |
| **复杂控制流** | ❌ 无 if-else 表达式外的控制 | ✅ 可包含循环、try 等 |
| **调试**    | ❌ 堆栈显示 `<lambda>`   | ✅ 显示函数名       |


---

### 18. 生成器和yield（内存高效）

```python
# 普通函数 - 占用大量内存
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# 生成器 - 惰性计算
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2

# 使用
for square in get_squares_gen(1000000):  # 不会一次性创建100万个数
    if square > 100:
        break
```

---

### 19. zip() 同时遍历两个列表

```python
# zip同时遍历
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
    
# 没有zip 必须假设两列表等长，且需要维护索引
for i in range(len(names)):  # 或 min(len(names), len(ages))
    name = names[i]
    age = ages[i]
    print(f"{name} is {age} years old")
 
# 生成新的list
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

pairs = list(zip(names, scores))
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# 生成字典
keys = ["id", "name", "email"]
values = [1, "Alice", "alice@example.com"]

user = dict(zip(keys, values))
# {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}

# 没有zip
user = {}
for i in range(len(keys)):
    user[keys[i]] = values[i]

# 或字典推导式（仍依赖索引）
user = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
```

矩阵运算

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

transposed = list(zip(*matrix))
# [(1, 4), (2, 5), (3, 6)]
```

`zip()` 还可以实现unzip的功能，当需要"把**成对数据**拆成两列传给不同函数"的需求时，可以用到。

---


### 20. @property装饰器（使用篇）

```python
# @property让方法可以像属性一样访问，类似Java的getter/setter但更简洁

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """getter - 读取属性"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """setter - 设置属性时可以验证"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """只读属性 - 计算得出，不能直接设置"""
        return self._celsius * 9/5 + 32

# 使用时像属性，不像方法
temp = Temperature(25)
print(temp.celsius)      # 25（不需要括号）
print(temp.fahrenheit)   # 77.0
temp.celsius = 30        # 调用setter
# temp.fahrenheit = 100  # ❌ AttributeError: can't set attribute
```

**对比Java**：
```java
// Java需要显式的getter/setter
public class Temperature {
    private double celsius;
    
    public double getCelsius() {
        return celsius;
    }
    
    public void setCelsius(double value) {
        if (value < -273.15) {
            throw new IllegalArgumentException("...");
        }
        celsius = value;
    }
}

// 使用
temp.setCelsius(30);
double c = temp.getCelsius();
```

```python
# Python用@property更简洁
temp.celsius = 30
c = temp.celsius
```

**关键点**：
- 你现在只需要**会用** `@property`，不需要理解装饰器原理
- 用 `@property` 把方法伪装成属性，提供更好的API
- 类似Java的getter/setter，但语法更优雅
- **装饰器的原理和自己创建装饰器在Advanced Level（第19节）讲解**
- 现在就把 `@property` 当作"Python提供的语法糖"来使用即可

---

### 21. set 集合

set 在去重和成员检测上性能是 O(1)。

```
# 创建（注意 {} 默认是 dict，不是 set！）
unique_ids = {1, 2, 3, 3, 3}  # {1, 2, 3}，自动去重
empty_set = set()             # ✅ 空集合必须用 set()，{} 会被认为是 dict

# 核心操作（对比其他语言）
# Java: HashSet<T>  |  JS: Set  |  C: 无原生支持
tags = {"python", "coding"}

# O(1) 成员检测（比 list 的 O(n) 快得多）
if "python" in tags:
    print("Found")

# 集合运算（SQL-like 的简洁语法）
a = {1, 2, 3}
b = {3, 4, 5}
a & b  # 交集: {3}      （Java: a.retainAll(b)）
a | b  # 并集: {1,2,3,4,5} （Java: a.addAll(b)）
a - b  # 差集: {1, 2}

# 实用场景：快速去重
numbers = [1, 2, 2, 3, 3, 3]
unique = list(set(numbers))  # [1, 2, 3]，虽然丢失顺序但极快
```

### 22. 空tuple `()` 的实用场景

```python
# ✅ 安全：空tuple作为默认参数（不可变）
def process_items(data, filters=()):
    """
    data: 输入数据
    filters: 要应用的过滤器函数列表
    """
    result = data
    for f in filters:  # 如果filters是()，循环不执行
        result = f(result)
    return result

# 调用
process_items(data)                             # 不应用过滤器
process_items(data, (remove_noise, normalize))  # 应用过滤器

# 对比：❌ 危险：list作为默认值（可变，有陷阱）
def bad_process(items=[]):
    items.append("new")  # 所有调用共享同一个list！
    return items

print(bad_process())  # ['new']
print(bad_process())  # ['new', 'new']  ← 意外！

# 空tuple的其他常见用法

# 1. 表示"无数据"但保持类型一致
def get_coordinates(has_location):
    if has_location:
        return (10, 20, 30)
    else:
        return ()  # 仍返回tuple类型

coords = get_coordinates(False)
if coords:  # 空tuple是falsy
    x, y, z = coords
else:
    print("No location")

# 2. 序列操作的边界情况
result = () + (1, 2, 3)      # (1, 2, 3)
result = (1, 2) + ()         # (1, 2)

# 3. 安全的遍历（不会报错）
for item in ():  # 不执行，但不报错
    print(item)
```

**关键点**：
- 用 `()` 而不是 `[]` 作为默认参数，避免可变默认参数陷阱
- 空tuple可以安全地遍历（不执行但不报错）
- 空tuple是falsy（`if ()` 为False），可以用于条件判断
- 最常见用途：作为函数的默认参数

---

### 23. Python 和 JavaScript 的真值规则有关键差异

关键差异是 **空数组、空字典**

#### Python 的 Falsy 值（9个）

```python
bool(False)      # False - 布尔值
bool(None)       # False - 空值
bool(0)          # False - 整数0
bool(0.0)        # False - 浮点0
bool(0j)         # False - 复数0
bool("")         # False - 空字符串
bool([])         # False - 空列表
bool(())         # False - 空元组
bool({})         # False - 空字典/集合
```

#### JavaScript 的 Falsy 值（7个）

```javascript
Boolean(false)     // false - 布尔值
Boolean(null)      // false - 空值
Boolean(undefined) // false - 未定义
Boolean(0)         // false - 数字0
Boolean(NaN)       // false - 非数字
Boolean("")        // false - 空字符串
Boolean(0n)        // false - BigInt 0
```

-------

## 第3章：Advanced Level - 进阶技巧

> 这些是进阶技巧，不影响日常开发，遇到时再深入学习
>
> Python 最常见的三个应用场景 Data Science/Web Development/Scripting 分别有各自的进阶技巧，所以这里提到内容是不完整的

### 24. Docstring（文档字符串）

- **Java**: Javadoc 注释 `/** ... */`，独立在函数体外部
- **JavaScript**: JSDoc `/** ... */`，同样在外部
- **C**: 通常用 `/* ... */` 或 `//` 在函数前

**Python 的不同**：Docstring 是**字符串字面量**（string literal），放在函数/类/模块的**第一行**，作为 `__doc__` 属性存在，不是注释。

```
def calculate_total(price, tax=0.08):
    """Calculate total price including tax.
    
    Args:
        price (float): Original price
        tax (float): Tax rate, default 0.08 (8%)
    
    Returns:
        float: Total amount after adding tax
        
    Example:
        >>> calculate_total(100)
        108.0
        >>> calculate_total(100, 0.1)
        110.0
    """
    return price * (1 + tax)

# 运行时访问（Python特有）
print(calculate_total.__doc__)  # 输出完整的文档字符串
help(calculate_total)           # 终端格式化显示文档

# 与注释的区别
def func():
    """这是docstring，会被编译进字节码，可通过__doc__访问"""
    # 这是注释， purely for source code reading，运行时不可见
    pass
```

Docstring 的核心价值在于它是**运行时可见的对象属性**，而不仅是给人类阅读的注释，比如在交互式开发中的使用场景（REPL 驱动），而且Docstring和工具链的深度集成。

```
# REPL 例如 ipython/python shell 使用场景
# 你在命令行里探索第三方库时：
import requests

# 忘记参数？直接问对象，不需要跳到浏览器查文档
help(requests.get)
```

---

### 25. 装饰器（创建篇）

```python
# 装饰器的本质：函数接受函数，返回函数
# Middle Level的@property就是装饰器的一个应用，这里学习如何自己创建装饰器

import time

def timing_decorator(func):
    """
    装饰器函数：
    1. 接收一个函数作为参数
    2. 返回一个新函数（包装了原函数）
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

# 使用@语法糖
@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

# 等价于：
# slow_function = timing_decorator(slow_function)

slow_function()  # "slow_function took 1.00s"

# 带参数的装饰器（更高级）
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Lang")
# Hello, Lang!
# Hello, Lang!
# Hello, Lang!
```

**理解装饰器的关键**：
- 装饰器是**高阶函数**（函数接受函数，返回函数）
- `@decorator` 只是语法糖，让代码更简洁
- Middle Level的 `@property` 就是Python内置的装饰器
- 你需要理解闭包和函数是一等公民的概念

**Middle Level vs Advanced Level 的区别**：
- **Middle Level** (`@property`): **使用**现成的装饰器，像使用Java的getter/setter
  ```python
  @property  # 使用Python提供的装饰器
  def celsius(self):
      return self._celsius
  ```
- **Advanced Level** (本节): **创建**自己的装饰器，理解其原理
  ```python
  def timing_decorator(func):  # 创建自己的装饰器
      def wrapper(*args, **kwargs):
          # 自定义逻辑
          return func(*args, **kwargs)
      return wrapper
  ```

**类比理解**：
- 使用 `@property` = 使用车（会开就行）
- 创建装饰器 = 造车（需要懂原理）

**实用装饰器示例**：
```python
# 缓存装饰器
def cache(func):
    cached = {}
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 日志装饰器
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

---

### 26. 魔法方法（dunder methods）

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return 2

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # 调用 __add__
print(v3)     # 调用 __str__: "Vector(4, 6)"
```

---

### 27. 类型提示（Type Hints，Python 3.5+）

```python
from typing import List, Dict, Optional

def process_names(names: List[str], max_length: int = 10) -> Dict[str, int]:
    return {name: len(name) for name in names if len(name) <= max_length}

def find_user(user_id: int) -> Optional[str]:
    # Optional[str] 表示可能返回str或None
    if user_id == 1:
        return "Lang"
    return None

# 类型提示不强制执行，但IDE和mypy等工具会检查
```

---


---

### 28. `dataclass`装饰器（Python 3.7+）

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    city: str = "Beijing"  # 默认值
    
    def is_adult(self) -> bool:
        return self.age >= 18

# 自动生成 __init__, __repr__, __eq__ 等方法
user = User("Lang", 25)
print(user)  # User(name='Lang', age=25, city='Beijing')
```

---

### 29. 空tuple `()` 的高级用法

```python
# 1. 作为字典的key（占位符/哨兵值）
cache = {
    (): "default value",           # 空tuple作为key
    (1,): "single item",
    (1, 2): "two items"
}

print(cache[()])  # "default value"

# 2. 类型注解中表示"无参数"
from typing import Callable

def register(callback: Callable[[], None]):
    """接受一个无参数、无返回值的函数"""
    callback()

def my_callback():
    print("Called")

register(my_callback)

# 3. 用于reduce等函数的初始值
from functools import reduce

# 虽然不常见，但技术上可行
data = [(1, 2), (3, 4), (5, 6)]
result = reduce(lambda x, y: x + y, data, ())
print(result)  # (1, 2, 3, 4, 5, 6)

# 4. 作为占位符表示"未初始化"状态
class DataProcessor:
    def __init__(self):
        self._cache = ()  # 明确表示"空"而非None
    
    def has_cache(self):
        return bool(self._cache)  # 空tuple是falsy

# 5. 在类型系统中的应用（Python 3.11+）
def no_return() -> tuple[()]:
    """明确返回空tuple"""
    return ()
```

**使用场景**：
- 作为字典key的占位符
- 类型注解中表示无参数
- 函数式编程中的初始值
- 明确区分"空集合"和"未初始化"（None）

**注意**：这些用法较少见，日常开发中最常用的还是作为默认参数（Middle Level）

---

### 30. EAFP vs LBYL

EAFP = Easier to Ask for Forgiveness than Permission

LBYL = Look Before You Leap 

这两种编程风格 python 更倾向与 EAFP

```
# LBYL 风格
def get_user_age(user_dict):
    if 'age' in user_dict:
        if isinstance(user_dict['age'], int):
            if user_dict['age'] > 0:
                return user_dict['age']
    return None

# 文件操作
import os
if os.path.exists('config.json'):
    if os.access('config.json', os.R_OK):
        with open('config.json') as f:
            data = f.read()
```

**LBYL 问题：**

- 检查和使用之间存在**竞态条件**（TOCTTOU - Time Of Check To Time Of Use）
- 文件可能在检查后、打开前被删除
- 代码冗长，嵌套深

**EAFP 风格, 先做再说，出错就处理**

```
#EAFP 
def get_user_age(user_dict):
    try:
        age = user_dict['age']
        if age > 0:
            return age
    except (KeyError, TypeError):
        pass
    return None

# 文件操作
try:
    with open('config.json') as f:
        data = f.read()
except FileNotFoundError:
    data = get_default_config()
except PermissionError:
    logging.error("No permission to read config")
    
    
# 字典访问的例子对比
if 'name' in user and user['name'] is not None:
    print(user['name'].upper())

# EAFP - Python 推荐
try:
    print(user['name'].upper())
except (KeyError, AttributeError):
    print("Name not available")
    
# 系统函数 get()
value = dict_obj.get("key", default)

# 等价于：
try:
    value = dict_obj["key"]
except KeyError:
    value = default
```

往往需要结合使用

```
def process_data(data):
    # 使用LBYL 前置条件检查（业务逻辑）
    if not data:
        raise ValueError("Data cannot be empty")
    
    # 使用 EAFP 处理技术细节
    try:
        result = complex_operation(data)
        return result['output']
    except KeyError:
        logging.error("Missing 'output' field")
        return default_output()
    except Exception as e:
        logging.exception("Unexpected error")
        raise
```



## 专题：*args和**kwargs详解

> 这是Python函数参数系统中最灵活的部分，也是初学者经常困惑的地方

### Entry Level - 必须掌握的基础

#### 1. 理解 `*args` 是什么

```python
# 概念：*args 可以接收任意数量的位置参数，它是一个tuple

def sum_all(*args):
    """接收任意数量的数字并求和"""
    print(f"收到的参数: {args}")  # args 是一个 tuple
    
    total = 0
    for num in args:
        total += num
    return total

# 调用方式
print(sum_all(1, 2, 3))           # 收到: (1, 2, 3), 返回 6
print(sum_all(10, 20))            # 收到: (10, 20), 返回 30
print(sum_all(5))                 # 收到: (5,), 返回 5
```

**关键点**：
- `*args` 把多个参数收集成一个tuple
- 可以传0个、1个或多个参数
- 在函数内部，`args` 就是普通的tuple，可以用for循环遍历

---

#### 2. 理解 `**kwargs` 是什么

```python
# 概念：**kwargs 可以接收任意数量的关键字参数，它是一个dict

def print_info(**kwargs):
    """打印用户信息"""
    print(f"收到的参数: {kwargs}")  # kwargs 是一个 dict
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用方式
print_info(name="Lang", age=25, city="Beijing")
# 收到: {'name': 'Lang', 'age': 25, 'city': 'Beijing'}
# 输出:
# name: Lang
# age: 25
# city: Beijing

print_info(job="Engineer")
# 收到: {'job': 'Engineer'}
# 输出:
# job: Engineer
```

**关键点**：
- `**kwargs` 把多个关键字参数收集成一个dict
- 必须用 `key=value` 的形式传参
- 在函数内部，`kwargs` 就是普通的dict

---

#### 3. 最简单的混合使用

```python
def greet(greeting, *names):
    """
    greeting: 必需的普通参数
    *names: 可变数量的名字
    """
    for name in names:
        print(f"{greeting}, {name}!")

# 第一个参数是greeting，后面都被收集到names中
greet("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

greet("Hi", "Lang")
# Hi, Lang!
```

**关键点**：
- 普通参数必须在 `*args` 之前
- 调用时第一个参数给greeting，其余的自动进入names

---

### Middle Level - 提高代码灵活性

#### 4. 使用 `*` 解包列表/元组

```python
# 场景：你有一个列表，想把它的元素作为多个参数传递

def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]

# ❌ 这样不行
# result = multiply(numbers)  # TypeError

# ✅ 使用 * 解包
result = multiply(*numbers)  # 相当于 multiply(2, 3, 4)
print(result)  # 24

# 实用例子：找最大值
scores = [85, 92, 78, 95, 88]
highest = max(*scores)  # 相当于 max(85, 92, 78, 95, 88)
print(highest)  # 95
```

---

#### 5. 使用 `**` 解包字典

```python
# 场景：你有一个字典，想把它的键值对作为关键字参数传递

def create_user(name, email, age):
    return {
        "name": name,
        "email": email,
        "age": age
    }

user_data = {
    "name": "Lang",
    "email": "lang@example.com",
    "age": 25
}

# ✅ 使用 ** 解包
user = create_user(**user_data)
# 相当于 create_user(name="Lang", email="lang@example.com", age=25)
print(user)
```

---

#### 6. `*args` 和 `**kwargs` 一起使用

```python
def create_user(username, email, **extra_info):
    """
    username, email: 必需参数
    **extra_info: 可选的额外信息
    """
    user = {
        "username": username,
        "email": email
    }
    
    # 把额外信息添加进去
    user.update(extra_info)
    return user

# 必需参数 + 任意可选参数
user1 = create_user("lang", "lang@example.com")
# {'username': 'lang', 'email': 'lang@example.com'}

user2 = create_user("lang", "lang@example.com", 
                    age=25, city="Beijing", job="Engineer")
# {'username': 'lang', 'email': 'lang@example.com', 
#  'age': 25, 'city': 'Beijing', 'job': 'Engineer'}
```

---

#### 7. 实用案例：日志函数

```python
def log(*messages, level="INFO"):
    """
    *messages: 任意数量的消息片段
    level: 日志级别（关键字参数，有默认值）
    """
    text = " ".join(str(msg) for msg in messages)
    print(f"[{level}] {text}")

# 灵活调用
log("User", "logged", "in")
# [INFO] User logged in

log("Database", "connection", "failed", level="ERROR")
# [ERROR] Database connection failed

log("Processing", 100, "records", level="DEBUG")
# [DEBUG] Processing 100 records
```

---

### Advanced Level - 高级技巧

#### 8. 完整的参数顺序规则

```python
def complex_function(
    pos1, pos2,              # 1. 必需的位置参数
    *args,                   # 2. 可变位置参数
    key1,                    # 3. 必需的关键字参数（*args后面的）
    key2="default",          # 4. 可选的关键字参数
    **kwargs                 # 5. 可变关键字参数
):
    print(f"位置参数: {pos1}, {pos2}")
    print(f"额外位置参数: {args}")
    print(f"关键字参数: {key1}, {key2}")
    print(f"额外关键字参数: {kwargs}")

# 调用示例
complex_function(
    1, 2,                    # pos1=1, pos2=2
    3, 4,                    # args=(3, 4)
    key1="required",         # key1="required"
    key2="custom",           # key2="custom"
    extra1="a",              # kwargs={'extra1': 'a', 'extra2': 'b'}
    extra2="b"
)
```

**记忆技巧**：参数顺序是 **普通 → *args → 关键字 → **kwargs**

---

#### 9. 装饰器中的应用

```python
import time

def timing_decorator(func):
    """
    装饰器需要处理被装饰函数的任意参数
    所以必须用 *args, **kwargs 来转发
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        
        # 原样传递所有参数给原函数
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"{func.__name__} 耗时 {end-start:.2f}秒")
        return result
    return wrapper

@timing_decorator
def slow_function(n, verbose=False):
    time.sleep(n)
    if verbose:
        print(f"Slept for {n} seconds")
    return "Done"

# 装饰器能正确处理任何调用方式
slow_function(1)
slow_function(0.5, verbose=True)
slow_function(n=2, verbose=False)
```

---

#### 10. 仅位置参数和仅关键字参数（Python 3.8+）

```python
def advanced_function(
    pos_only, /,           # / 之前的只能按位置传递
    normal,                # 既可以位置也可以关键字
    *,                     # * 之后的只能按关键字传递
    kw_only
):
    print(f"{pos_only}, {normal}, {kw_only}")

# ✅ 正确
advanced_function(1, 2, kw_only=3)
advanced_function(1, normal=2, kw_only=3)

# ❌ 错误
# advanced_function(pos_only=1, normal=2, kw_only=3)  # pos_only不能用关键字
# advanced_function(1, 2, 3)  # kw_only必须用关键字
```

**应用场景**：API设计中强制参数传递方式，提高代码可读性

---

#### 11. 转发和合并参数

```python
def api_wrapper(endpoint, *args, **kwargs):
    """
    包装第三方API调用
    转发所有参数到实际的API函数
    """
    # 添加默认配置
    default_config = {
        "timeout": 30,
        "retry": 3
    }
    
    # 合并配置（用户的kwargs会覆盖默认值）
    final_config = {**default_config, **kwargs}
    
    print(f"调用 {endpoint}")
    print(f"位置参数: {args}")
    print(f"配置: {final_config}")
    
    # 这里会调用真实的API
    # return real_api_call(endpoint, *args, **final_config)

# 使用
api_wrapper("users/create", "lang", "lang@example.com", 
            timeout=60, auth_token="xyz")
# 调用 users/create
# 位置参数: ('lang', 'lang@example.com')
# 配置: {'timeout': 60, 'retry': 3, 'auth_token': 'xyz'}
```

---

#### 12. 常见陷阱：可变默认参数

```python
# ⚠️ 危险写法
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

# 所有调用共享同一个列表！
list1 = add_to_list("a")  # ['a']
list2 = add_to_list("b")  # ['a', 'b']  ← 意外！

# ✅ 正确写法
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# 现在每次调用都是独立的列表
list1 = add_to_list("a")  # ['a']
list2 = add_to_list("b")  # ['b']  ← 正确！
```

---

### *args/**kwargs 学习建议

#### Entry Level（第1-2周）
- 会用 `*args` 接收多个位置参数
- 会用 `**kwargs` 接收多个关键字参数
- 理解它们在函数内部就是tuple和dict

#### Middle Level（第3-4周）
- 会用 `*` 解包列表
- 会用 `**` 解包字典
- 能在实际项目中灵活组合使用

#### Advanced Level（遇到再学）
- 理解完整的参数顺序规则
- 能写通用的装饰器和包装函数
- 避开可变默认参数等陷阱

---

## 附录

### A. 学习路线建议

**第一周：Entry Level**
- 只掌握Entry Level，能写基本代码
- 设置好虚拟环境
- 每天写一些小练习

**第二-三周：Middle Level**
- 逐步引入Middle Level特性
- 重构第一周的代码，使用新学的特性
- 开始小项目实践

**之后：Advanced Level**
- 在实际项目中遇到时再学
- 阅读优秀的开源项目代码
- 深入理解Python的设计哲学

参考 https://roadmap.sh/python 

---

### B. 从Java到Python对照表

| 概念 | Java | Python |
|------|------|--------|
| 循环 | `for(int i=0; i<n; i++)` | `for i in range(n):` |
| 类型声明 | `String name = "Lang";` | `name = "Lang"` |
| 动态数组 | `ArrayList<String>` | `list` (内置) |
| 不可变序列 | - | `tuple` (Python特有) |
| 字典/映射 | `HashMap<K,V>` | `dict` (内置) |
| 空值 | `null` | `None` (用`is`判断) |
| 逻辑与 | `&&` | `and` |
| 逻辑或 | `||` | `or` |
| 逻辑非 | `!` | `not` |
| 字符串 | `String`不可变 | `str`不可变 |
| 字符串拼接 | `StringBuilder` | `"".join()` |
| 私有变量 | `private` | `_variable` (约定) |
| 接口 | `interface` | 鸭子类型/ABC |
| 包管理 | Maven/Gradle | pip/Poetry |
| 虚拟环境 | Maven依赖隔离 | venv/virtualenv |

---

### C. 从JavaScript到Python对照表

| 概念 | JavaScript | Python |
|------|-----------|--------|
| 变量声明 | `let x = 1;` | `x = 1` |
| 常量 | `const PI = 3.14;` | `PI = 3.14` (约定大写) |
| 动态数组 | `Array` | `list` |
| 不可变序列 | - | `tuple` (Python特有) |
| 字符串模板 | `` `Hello ${name}` `` | `f"Hello {name}"` |
| 字符串 | 不可变 | 不可变 |
| 字符串拼接 | `arr.join()` | `"".join()` |
| 解构赋值 | `const [a, b] = arr;` | `a, b = arr` |
| 展开运算符 | `...arr` | `*arr` |
| 对象展开 | `{...obj}` | `**obj` |
| 箭头函数 | `x => x * 2` | `lambda x: x * 2` |
| 数组方法 | `.map()`, `.filter()` | 列表推导式 |
| Promise | `async/await` | `asyncio` |
| 包管理 | npm/yarn | pip/Poetry |
| 虚拟环境 | `node_modules` | venv |

---

### D. 常见陷阱和解决方案

#### 1. 可变默认参数
```python
# ❌ 错误
def append_to(element, to=[]):
    to.append(element)
    return to

# ✅ 正确
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```

#### 2. 循环变量泄漏
```python
# Python中循环变量会"泄漏"到外层作用域
for i in range(5):
    pass
print(i)  # 4 (变量i仍然存在)

# 如果不想要这个行为，使用列表推导
_ = [process(x) for x in items]  # 不会创建i变量
```

#### 3. 整数除法
```python
# Python 2 vs Python 3
print(5 / 2)   # Python 3: 2.5 (float)
print(5 // 2)  # 2 (整除)

# 确保除法行为一致，使用 // 或显式转换
```

#### 4. 字符串拼接性能（字符串不可变）
```python
# Python字符串是不可变的，每次修改都创建新对象

# ❌ 低效（每次都创建新字符串）
result = ""
for s in strings:
    result += s  # 每次循环创建新字符串，O(n²)复杂度

# 对比Java
# Java也有类似问题：String是不可变的
# String result = "";
# for (String s : strings) {
#     result += s;  // 低效，应该用StringBuilder
# }

# ✅ 高效（Python推荐方式）
result = "".join(strings)  # O(n)复杂度

# ✅ 使用f-string或format（适合少量拼接）
name = "Lang"
age = 25
message = f"{name} is {age} years old"  # 高效且可读

# 理解不可变性
s1 = "hello"
s2 = s1.upper()  # 创建新字符串
print(id(s1), id(s2))  # 不同的内存地址
```

**关键点**：
- 字符串不可变，类似Java的`String`
- 大量拼接用`join()`，类似Java用`StringBuilder`
- 少量拼接直接用`+`或f-string即可

#### 5. 列表复制（可变类型陷阱）
```python
# ❌ 浅拷贝（两个变量指向同一个对象）
list2 = list1
list2.append(4)  # list1也会改变

# ✅ 深拷贝
list2 = list1.copy()  # 或 list1[:]
list2.append(4)  # list1不受影响

# 对比不可变类型（如字符串、tuple）
s1 = "hello"
s2 = s1
s2 = s2.upper()  # s1不受影响，因为字符串不可变
```

**Python可变与不可变类型总结**：

| 类型 | 可变性 | 赋值行为 | 类似语言 |
|------|--------|----------|----------|
| `int`, `float`, `bool` | 不可变 | 创建新对象 | 所有语言 |
| `str` | 不可变 | 创建新对象 | Java String, JS string |
| `tuple` | 不可变 | 创建新对象 | Python特有 |
| `list` | **可变** | 共享引用 | Java ArrayList, JS Array |
| `dict` | **可变** | 共享引用 | Java HashMap, JS Object |
| `set` | **可变** | 共享引用 | Java HashSet |

```python
# 理解可变与不可变
# 不可变类型
a = 10
b = a
b = 20  # a仍然是10，因为int不可变

# 可变类型
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)  # list_a变成了[1, 2, 3, 4]，因为list可变

# 这就是为什么需要copy()
list_c = list_a.copy()
list_c.append(5)  # list_a不受影响
```

---

### E. 推荐资源

**官方文档**：
- [Python官方教程](https://docs.python.org/3/tutorial/)
- [Python标准库](https://docs.python.org/3/library/)

**进阶阅读**：
- 《Fluent Python》（流畅的Python）
- 《Effective Python》（高效Python）
- [Real Python](https://realpython.com/)

**代码风格**：
- [PEP 8 -- Style Guide for Python Code](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

**在线练习**：
- [LeetCode](https://leetcode.com/) - 算法练习
- [Python Koans](https://github.com/gregmalcolm/python_koans) - 通过测试学习
- [Exercism](https://exercism.org/tracks/python) - 有导师反馈

---

## 结语

这份指南专门为有C/Java/JS经验的开发者设计，重点突出Python的特别之处。记住：

1. **不要急于求成** - 先掌握Entry Level，再逐步进阶
2. **多写代码** - 理论再多不如实践一次
3. **阅读优秀代码** - GitHub上有大量高质量Python项目
4. **拥抱Python哲学** - "简单优于复杂，明确优于隐晦"

祝你的Python之旅顺利！

---

**文档版本**: 1.1  
**最后更新**: 2026-02-03  
**反馈**: 如有问题或建议，欢迎提出
