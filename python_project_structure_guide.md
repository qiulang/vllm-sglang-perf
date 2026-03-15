# Python 项目目录结构整理指南

## 背景

随着项目文件增多，把所有文件 (核心代码，测试代码，资源文件) 放在根目录下变得难以维护，需要按职责分目录：

### 整理前
```
.
├── module_a.py
├── module_b.py
├── main_script.py
├── test_a.py
├── test_b.py
├── .env
├── config.yaml
└── data.txt
```

### 整理后
```
.
├── main.py              # 程序入口
├── config.yaml
├── .env
├── src/                 # 核心代码/业务代码
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   └── main_script.py
├── tests/               # 测试代码
│   ├── __init__.py
│   ├── test_a.py
│   └── test_b.py
└── assets/              # 静态资源
    └── data.txt
```

---

## 整理方案分三步进行

### 第一步 （方案 0）：迁移成本最低（推荐作为起点）

**只做一件事：把核心代码挪到 `src/`，测试代码挪到 `tests/`，其他全部不动。**

```
.
├── config.yaml          ← 不动
├── data.txt             ← 不动，留在根目录
├── .env
├── src/
│   ├── module_a.py      ← 从根目录移过来
│   ├── module_b.py      ← 从根目录移过来
│   ├── main_script.py   ← 从根目录移过来
│   └── ...
└── tests/
    ├── test_a.py        ← 从根目录移过来
    └── ...
```

import 代码、文件路径代码、资源文件，**全部不改、不动。**

在根目录下运行命令：

```bash
# 跑程序 （Windows/macOS/Linux）
python src/main_script.py

# 跑测试 （macOS/Linux）
PYTHONPATH=src python tests/test_a.py

# Windows CMD
set PYTHONPATH=src && python tests/test_a.py

# Windows PowerShell
$env:PYTHONPATH="src"; python tests/test_a.py
```

**为什么能工作：**
- `python src/main_script.py` 把 `src/` 加入 `sys.path`，`src`里的python文件里，`from module_a import ...` 能找到 `src/` 下的同级文件 ✅
- `PYTHONPATH=src` 同样把 `src/` 加入 `sys.path`，测试代码里的 import 也能找到 ✅
- 资源文件留在根目录，`open("data.txt")` 基于当前工作目录（根目录）依然有效 ✅

**限制：**

- Windows/macOS/Linux 注意 `/` 和 `\` 不同，Windows 的路径分隔符是 `\`，但 Python 解释器本身接受 `/` 作为路径分隔符，CMD 和 PowerShell 也都支持。所以这一行三个平台写法一样。
- 跑测试每次都要记得加 `PYTHONPATH=src`
- 不符合标准 package 结构

---

### 第二步（方案 A）：资源文件挪到 assets/

在方案 0 的基础上，把资源文件从根目录挪到 `assets/`，同时把文件路径读取代码改为绝对路径。import 代码不改，运行方式不变。

文件路径建议使用 pathlib 库， Windows/macOS/Linux  都使用 `/` 路径分隔符，`pathlib` 会自动根据当前操作系统选择正确的分隔符。

```python
# src/main_script.py
from module_a import func_a    # 不改

# 文件路径改为绝对路径
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent   # 指向项目根目录
data_file = BASE_DIR / "assets" / "data.txt"   # 稳定
```

| 运行程序 | 运行测试 |
|---|---|
| `python src/main_script.py` | `PYTHONPATH=src python tests/test_a.py` |

import 不用改，测试代码也不用改，只改了读取文件的路径代码。

#### 文件路径问题

目录整理后，原来硬编码的相对路径会失效：

```python
# 原来在根目录，直接写文件名
open("data.txt")          # ✅ 原来正常

# 文件挪到 assets/ 后
open("assets/data.txt")   # 看起来对，但依赖当前工作目录，不稳定
```

#### 推荐做法：用绝对路径

在 `config.yaml` 里配置路径 (.env 同样道理)：
```yaml
assets:
  data: "assets/data.txt"
```

代码里用 `BASE_DIR` 拼接绝对路径：
```python
# main.py
from pathlib import Path
from src.main_script import main

if __name__ == "__main__":
    main(base_dir=Path(__file__).parent)   # 把根目录传进去
```

```python
# src/main_script.py
def main(base_dir=None):
    from pathlib import Path
    base_dir = base_dir or Path(__file__).parent.parent #注意要往上推两级 (src->project root)
    data_file = base_dir / config["assets"]["data"]   # 绝对路径，稳定
```


---

### 第三步 （方案 B）：src/ 内相对导入，标准做法

**为项目后续增长打好基础**：随着项目文件增多，想进一步拆子目录（比如 `src/utils/`、`src/models/`），方案B为项目后续增长留好了扩展路径。同时方案 0/A 每次跑测试都要加 `PYTHONPATH=src`，在 Windows/macOS/Linux 上写法还不一样，容易出错。方案 B 做了几处改动，换来的结果是：

```bash
python main.py          # 跑程序
python -m tests.test_a  # 跑测试，不需要任何环境变量，Windows/macOS/Linux 完全一致。
```

在方案 A 的基础上：

1. `src/` 内所有 import 改为相对导入（`from .module_a import ...`）

```python
# src/main_script.py
from .module_a import func_a   # 相对导入
```
2. 测试代码 import 改为 `from src.module_a import ...`

因为当用 `python -m tests.test_a` 运行时，sys.path[0] = 项目根目录，所以 `from module_a import func` 会去根目录找 module_a.py（找不到，因为它在 src/ 下）。**必须改成** `from src.module_a import func` 才能正常。

```python
# tests/test_a.py
from src.module_a import func_a   # 测试代码改这一行
```
3. 新增 `src/__init__.py`、`tests/__init__.py`
4. 运行测试代码不需要 `PYTHONPATH=src` 直接`python -m tests.test_a`


| 运行程序 | 运行测试 |
|---|---|
| `python main.py` | `python -m tests.test_a` |

不需要环境变量，是标准 Python 项目做法。但是熟悉两个概念

### 核心概念：sys.path

Python 找模块的方式是遍历 `sys.path` 列表，**第一个元素** `sys.path[0]` 由运行方式决定：

| 运行方式 | sys.path[0] |
|---|---|
| `python src/module_a.py` | `src/` 目录 |
| `python tests/test_a.py` | `tests/` 目录 |
| `python main.py` | 项目根目录 |
| `python -m src.module_a` | 项目根目录 |
| `python -m tests.test_a` | 项目根目录 |

这是所有路径问题的根源。

---

#### import 的两种写法

##### 绝对导入
```python
# src/main_script.py
from module_a import func_a       # 在 sys.path 里找 module_a
from src.module_a import func_a   # 在 sys.path 里找 src/module_a
```

##### 相对导入
```python
# src/main_script.py
from .module_a import func_a      # 在当前 package 内找 module_a
```

相对导入只有当文件作为 **package 的一部分**被加载时才有效，直接当脚本运行会报错：
```
ImportError: attempted relative import with no known parent package
```

---

### 两种运行方式的本质区别

#### 方式一：直接运行脚本（`python 文件路径`）

`sys.path[0]` = **脚本所在目录**

```bash
python src/main_script.py   # sys.path[0] = src/
python tests/test_a.py      # sys.path[0] = tests/
```

Python 把文件当成独立脚本，以文件所在目录为起点找模块：

```python
# python src/main_script.py 时
from module_a import func_a    # ✅ module_a.py 在 src/ 下，能找到
from .module_a import func_a   # ❌ 相对导入报错，不是 package 模式

# python tests/test_a.py 时
from module_a import func_a      # ❌ module_a 不在 tests/ 里
from src.module_a import func_a  # ❌ src/ 也不在 tests/ 里
```

---

#### 方式二：模块方式运行（`python -m` 或 `python main.py`）

`sys.path[0]` = **当前工作目录**（即项目根目录）

在根目录下增加  main.py 作为程序入口，代码很简单，但是前提是 module_a 有 main 入口

```
# main.py at project root
from src.module_a import main

if __name__ == "__main__":
    main()
```

在根目录下执行

```bash
python main.py              # sys.path[0] = 项目根目录
python -m tests.test_a      # sys.path[0] = 项目根目录
```

`python main.py` 本质上和 `python -m src.main_script` 效果一样，只是 `main.py` 放在根目录，写起来更简洁，是标准的项目入口写法。

以根目录为起点找模块：

```python
# src/main_script.py 被作为 package 的一部分加载
from .module_a import func_a       # ✅ 相对导入正常
from src.module_a import func_a    # ✅ 绝对导入也正常

# tests/test_a.py
from src.module_a import func_a    # ✅ 能找到
from module_a import func_a        # ❌ 找不到，module_a 不在根目录
```

python -m 的另一个好处是：运行标准库/第三方模块的快捷方式，比如大多数不会记住库的文件名，比如 `http.server`的文件名，但是会知道有这个模块。所以我们就可以用 `python -m` 执行

```
python -m http.server
python -m json.tool data.json
python -m venv .venv
```


## 迁移方案需要新增的文件

| 文件 | 作用 |
|---|---|
| `main.py` | 程序唯一入口，替代原来的 `python src/main_script.py` |
| `src/__init__.py` | 让 `src/` 成为 package，空文件即可 |
| `tests/__init__.py` | 让 `tests/` 成为 package，`python -m` 运行测试时必须有 |
| `.gitignore` | 忽略 `__pycache__/`、`*.pyc`、生成的临时文件 |

---


## 总结对比

| | 方案 0（迁移成本最低） | 方案 A | 方案 B（最规范） |
|---|---|---|---|
| 资源文件位置 | 根目录（不动） | `assets/` | `assets/` |
| src/ 内导入 | 绝对导入（不改） | 绝对导入（不改） | 相对导入（要改） |
| 测试代码导入 | 不改 | 不改 | 改成 `from src.xxx import` |
| 文件路径代码 | 不改 | 改用 `BASE_DIR` | 改用 `BASE_DIR` |
| 运行程序 | `python src/main_script.py` | `python src/main_script.py` | `python main.py` |
| 运行测试 | `PYTHONPATH=src python tests/test_a.py` | `PYTHONPATH=src python tests/test_a.py` | `python -m tests.test_a` |
| 代码改动量 | 零 | 文件路径部分 | import + 文件路径 |
| 规范程度 | 低 | 中 | 标准做法 |

---

## 附录一：方案 C —— src-layout（打包发布标准）

方案 B 里 `src/` 有 `__init__.py`，`src` 本身是一个可导入的 package，导入时要写 `from src.module_a import ...`。这在应用程序项目里没有问题，但如果将来要**打包发布到 PyPI**，这个结构有一个根本性的缺陷：

开发时写 `from src.module_a import ...`，发布安装后包名是 `src`，所有用户也得写 `from src.module_a import ...` ——`src` 这个名字毫无意义，而且极易和别人的包冲突。

src-layout 的解法是：**`src/` 不放 `__init__.py`，真正的 package 放在 `src/` 里面一层**：

```
.
├── main.py
├── pyproject.toml
├── src/
│   └── my_project/          ← 这才是 package，有 __init__.py
│       ├── __init__.py
│       ├── module_a.py
│       └── module_b.py
└── tests/
    ├── __init__.py
    └── test_a.py
```

导入写法变为：

```python
from my_project.module_a import func_a
```

开发阶段和安装后的导入方式完全一致，package 名字有实际语义。注意，这个方案需要引入`pyproject.toml` 它的使用方法暂时不在本文扩展。


**什么时候才需要方案 C：**

- 项目要发布为可 `pip install` 的库
- 团队有明确的打包需求

纯应用程序项目（不发布、不打包）方案 B 已经足够，不必引入额外复杂度。

---

## 附录二：`pip install` vs `python -m pip install`

### 什么情况下会发生版本错位

`pip` 本质上是一个可执行文件，和 `python` 一样放在系统的某个目录里。当系统里只有一个 Python 时，两者自然对应。但以下情况会导致错位：

**macOS / Linux**：系统预装了一个旧版 Python（比如 3.9），用户后来手动装了新版（比如 3.12）。两个版本并存，`python` 的软链接可能已经指向新版，但 `pip` 的软链接还留在旧版那里：

```bash
which python   # /usr/local/bin/python  → 3.12
which pip      # /usr/bin/pip           → 3.9（系统预装那个）
```

**Windows**：用安装包装了多个版本，或者混用了官网安装包和 Microsoft Store 版本，PATH 里哪个排前面哪个生效，`pip` 和 `python` 可能来自不同的安装。

### 什么情况下不会发生

- 使用虚拟环境（venv / conda）并已激活：激活后 `pip` 和 `python` 都指向同一个环境，不存在错位
- Linux 服务器，Python 版本单一，没有多版本并存

**如果你的工作流是"始终在 venv 里工作"，直接写 `pip install` 完全没问题，不需要改习惯。**

### `python -m pip` 的好处

一旦存在多版本并存的情况，`python -m pip` 能保证"用哪个 Python 跑代码，就往哪个 Python 装包"，两者强制绑定：

```bash
pip install requests              # 装到哪个 Python 不确定
python -m pip install requests    # 一定装到 python 指向的那个
```

排查 `ModuleNotFoundError` 时也更直观：

```bash
python -m pip list   # 直接看当前 python 装了哪些包
```

这也是为什么官方文档和很多教程里默认写 `python -m pip`——不是写法更复杂，而是在多版本环境下更可靠。
