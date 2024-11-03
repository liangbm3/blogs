---
title: Python内置库argparse的使用
date: 2024-10-29 15:41:27
description: argparse 是 Python 标准库中用于解析命令行参数的模块，提供了一种简单、直观的方式来定义命令行接口，让程序可以直接从命令行获取输入并据此执行不同的操作，在许多深度学习的工程代码中经常用到。
tags: 
    - Python
    - 日常总结
top_img: /img/Python内置库argparse的使用/cover.png
cover: /img/Python内置库argparse的使用/cover.png
---

# 1. 前言

`argparse` 是 Python 标准库中用于解析命令行参数的模块，提供了一种简单、直观的方式来定义命令行接口，让程序可以直接从命令行获取输入并据此执行不同的操作，在许多深度学习的工程代码中经常用到。

# 2. 基本参数类型

我们通过命令行运行 Python 文件时，可以向文件传递不同类型的参数。主要有以下几种类型：

1.   **位置参数（Positional arguments）**：位置参数是指在命令行中按照特定顺序传递给程序的参数，它们不带任何前缀。示例：

     ```bash
     python main.py arg1 arg2
     ```

2.   **选项参数（Optional arguments）**：选项参数是可选的参数，它们通常以短横线（-）或双短横线（--）开头。示例

     ```bash
     python main.py --config ./config/test/aagcn_B_3d.yaml --phase test
     ```

3.   **标志参数（Flag arguments）**：标志参数是一种特殊的选项参数，它们不带值，只用于表示某个状态或开关是否打开。通常以短横线和单个字符表示，例如 `-v` 表示 verbose 模式。

     ```bash
     python main.py -v
     ```

# 2. 基本用法

## 2.1 创建解析器

使用 `argparse` 的第一步是创建一个 `ArgumentParser` 对象：

```python
parser = argparse.ArgumentParser(description='Descriptive information')
```

`description`是该对象的描述信息，可使用`python main.py -h`命令查看。

## 2.2 添加参数

可以使用`parser.add_argument`方法像解析器添加参数。

### 2.2.1 name属性

参数名称（`name`）是传递给 `add_argument()` 的第一个参数，直接指定了命令行参数的名称。根据参数前缀的不同，可以分为**位置参数**和**可选参数**：

1.   **添加位置参数**

     位置参数是一个字符串，位置参数在使用命令行输入的时候位置不能调换，且不用输入参数名，示例：

     ```python
     parser.add_argument('num1', type=int, help='The first number')
     parser.add_argument('num2', type=int, help='The second number')
     ```

     ```bash
     python main.py 2 3
     ```

2.   **添加可选参数**

     可选参数通常以短横线（-）或双短横线（--）开头，短横线后面一般是缩写，双短横线后面是参数的完整名称。短横线名称可以选择，双短横线名称必须存在。可选参数在使用命令行输入的时候位置可以调换，且要输入参数名，示例：

     ```python
     parser.add_argument('-n1','--number1', type=int, help='The first number')
     parser.add_argument('-n2','--number2', type=int, help='The second number')
     ```

     ```bash
     python main.py -n1 1314 -n2 520
     python main.py --number2 520 --number1 1314
     ```



### 2.2.2 type属性

`type` 属性用于指定参数的预期数据类型，帮助解析和验证命令行输入的数据格式。如果输入的数据类型不符合 `type` 指定的格式，`argparse` 会自动抛出错误。`type` 属性支持多种常见的数据类型，还可以自定义数据转换函数。常见的数据类型如下

1.   `str`：默认类型，将输入解析为字符串类型，适用于大多数文本、路径等输入

     ```python
     parser.add_argument("--name", type=str, help="Your name")
     ```

2.  `int`：将输入解析为整数，适合计数、编号等整数类型的参数；如果输入非整数，会自动报错

     ```python
     parser.add_argument("--age", type=int, help="Your age")
     ```

3.   `float`：将输入解析为浮点数，适合需要精确到小数的参数，比如学习率、权重等

     ```python
     parser.add_argument("--learning-rate", type=float, help="Learning rate for training")
     ```

除此之外，我们还可以通过传递自定义函数，将输入值解析为自定义格式。例如，可以定义一个将输入转换为复数的函数或仅允许特定格式的字符串输入

```python
def parse_complex(value):
    return complex(value)

parser.add_argument("--complex-number", type=parse_complex, help="A complex number input")
```

### 2.2.3 help属性

可以通过这个属性为参数添加描述，用户在命令行输入`-h`或`--help`时会输入相应的帮助信息。

### 2.2.4 default属性

`default` 属性用于为参数设置默认值。如果命令行中没有提供该参数，解析后的结果会使用 `default` 指定的默认值。示例

```python
parser.add_argument("--timeout", type=int, default=30, help="Set the timeout in seconds (default: 30)")
args = parser.parse_args()
```

### 2.2.5 required属性

当 `required=True` 时，程序运行时必须提供该参数，否则 `argparse` 会自动提示错误并输出帮助信息。

```python
parser.add_argument("--name", required=True,type=str, help="Your name")
```

### 2.2.6 action属性

`action` 属性用于控制命令行参数的解析行为。不同的 `action` 值会导致参数的处理方式不同，特别适用于控制布尔开关、多值参数以及参数累积。`action`的常见可选值如下：

1.   `"store"`：默认值，将用户输入的值存储在变量中。

2.   `"store_const"`：用于将一个预定义的常量值存储为参数值，而不是从命令行中获取该参数的输入。即不需要输入具体的值，只要参数存在，就赋予一个固定的值。示例：

     ```python
     parser.add_argument("--flag", action="store_const", const=42, default=0, help="Store a constant value of 42 if this flag is present")
     ```

     当执行命令`python main.py --flag`时，参数值为常量42。

3.   `"store_true"`：将布尔值 `True` 存储为参数值，常用于启用某个特性，示例：

     ```python
     parser.add_argument("--debug", action="store_true", help="Enable debug mode")
     ```

     `--debug`会将 `args.debug` 设置为 `True`，不指定则为 `False`

4.   `"store_false"`：将布尔值 `False` 存储为参数值，常用于禁用某个特性，示例：

     ```python
     parser.add_argument("--no-cache", action="store_false", help="Disable caching")
     ```

     `--no-cache` 会将 `args.no_cache` 设置为 `False`，不指定则为 `True`。

5.   `"append"`：将每次传入的值追加到一个列表中，适用于接受多个输入值的场景，示例：

     ```python
     parser.add_argument("--tag", action="append", help="Add a tag to the list of tags")
     ```

     命令行输入 `--tag dev --tag test` 后，`args.tag` 的值为 `["dev", "test"]`。

### 2.2.7 dest属性

`dest` 属性用于指定参数在解析后存储的变量名。通过设置 `dest`，可以在代码中访问参数值时使用更直观或自定义的名称，而不依赖于命令行中传入的参数名称。示例：

```python
import argparse

parser = argparse.ArgumentParser(description="Example of dest attribute")

# 使用 dest 定义变量名称为 'input_path'
parser.add_argument("--input", dest="input_path", type=str, help="Path to the input file")
parser.add_argument("-o", "--output", dest="output_path", type=str, help="Path to the output file")

args = parser.parse_args()

print("Input path:", args.input_path)
print("Output path:", args.output_path)
```

### 2.2.8 nargs属性

`nargs` 属性用于指定命令行参数能够接受的值的数量。允许我们控制参数的输入数量，包括支持单个、多个、可变数量的值，甚至可以将所有剩余的命令行参数捕获到一个列表中。

`nargs`属性常见的取值如下：

1.   整数值：指定参数必须接受确切数量的值，如`nargs=2` 表示参数需要接受两个值，示例：

     ```python
     parser.add_argument("--range", nargs=2, type=int, help="Specify a start and end value")
     ```

     命令行输入`python main.py --range 1 10`后得到的变量值为`args.range = [1, 10]`

2.   `?0`：表示参数值是可选的，最多可以接受一个值。若不提供值，则使用默认值（如果设置了默认值）或 `None`，示例：

     ```python
     parser.add_argument("--verbosity", nargs="?", const="INFO", help="Set verbosity level (default: INFO if no value is provided)")
     ```

     +   命令行输入`python main.py --verbosity DEBUG`得到的是`args.verbosity = "DEBUG"`
     +   命令行输入`python main.py --verbosity`得到的是`args.verbosity = "INFO"`

3.   `*`：接受零个或多个值，所有输入将被收集到一个列表中，示例：

     ```python
     parser.add_argument("--files", nargs="*", help="List of files to process")
     ```

     命令行输入`python main.py --files file1.txt file2.txt file3.txt`得到的是`args.files = ["file1.txt", "file2.txt", "file3.txt"]`

4.   `+`：接受一个或多个值，所有值将被收集到一个列表中。如果没有提供值，会报错，示例：

     ```python
     parser.add_argument("--items", nargs="+", help="List of items")
     ```

     命令行输入`python main.py --items apple banana orange`得到的是`args.items = ["apple", "banana", "orange"]`

5.   `argparse.REMAINDER`：将命令行中所有剩余的参数捕获到一个列表中。通常用于将所有剩余的参数传递给另一个命令或子程序，示例：

     ```python
     parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run with all remaining args")
     ```

     在命令行输入`python script.py --command ls -l /home/user`得到的是`args.command = ["ls", "-l", "/home/user"]`

### 2.2.9 choices属性

用于限制参数的值只能在指定的选项范围内，如果传入的值不在范围内，`argparse` 会自动报错。示例：

```python
parser.add_argument("--mode", choices=["train", "test", "validate"], help="Specify the operation mode")
```

### 2.2.10 metavar属性

用于在帮助信息中显示参数的占位符名称，而不影响变量名称。可以让帮助信息更简洁明了，示例：

```python
parser.add_argument("--input", metavar="INPUT_FILE", help="Path to the input file")
```

## 2.3 解析参数

添加完参数之后，我们使用如下语句进行解析：

```python
args = parser.parse_args()
#解析命令行参数
```

## 2.4 使用参数

解析完成后，我们使用语句`arg.参数名`就可以直接使用了。

注意：`name`属性中的短横线（-）被解析成Python变量时会变成下划线，示例：

```python
import argparse

parser = argparse.ArgumentParser(description="Example of argparse usage")
parser.add_argument("--train-path", type=str, help="Path to training data")
parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")

args = parser.parse_args()

# 访问参数
print(args.train_path)
print(args.epochs)
```

# 3. 一个完整的示例

```python
import argparse

# 创建 ArgumentParser 对象，并设置程序的描述和 epilog
parser = argparse.ArgumentParser(
    prog="FileProcessor",
    description="This program processes an input file and outputs the results based on specified options.",
    epilog="For more details, please visit our documentation."
)

# 添加必需的输入文件参数（位置参数）
parser.add_argument(
    "input_file",  # 位置参数，不需要 -- 前缀
    type=str,
    help="Path to the input file that will be processed."
)

# 添加可选参数：输出文件
parser.add_argument(
    "-o", "--output",  # 支持 -o 和 --output 两种形式
    type=str,
    default="output.txt",  # 默认值
    metavar="OUTPUT_FILE",  # 在帮助信息中显示的参数名称
    help="Specify the output file path. Default is 'output.txt'."
)

# 添加可选参数：处理模式
parser.add_argument(
    "-m", "--mode",
    choices=["fast", "slow", "custom"],  # 限制选项
    default="fast",
    help="Choose the processing mode. Available options are 'fast', 'slow', or 'custom'. Default is 'fast'."
)

# 添加可选参数：详细模式（布尔开关）
parser.add_argument(
    "-v", "--verbose",
    action="store_true",  # 如果提供此参数，则将其值设为 True，否则为 False
    help="Enable verbose mode to get detailed output."
)

# 添加可选参数：重复次数（整数类型，默认值为 1）
parser.add_argument(
    "-r", "--repeat",
    type=int,
    default=1,
    help="Specify the number of times to repeat the processing. Default is 1."
)

# 添加可选参数：设置日志级别（可选的多值参数）
parser.add_argument(
    "--log-level",
    nargs="?",
    const="INFO",  # 如果没有提供值，则默认为 INFO
    help="Set the logging level. If no level is specified, 'INFO' is used by default."
)

# 添加可选参数：标签（允许多个值）
parser.add_argument(
    "--tags",
    nargs="*",
    help="Specify tags associated with this processing task. You can pass multiple tags."
)

# 解析命令行参数
args = parser.parse_args()

# 打印解析后的参数（供调试）
print("Parsed arguments:")
print("Input file:", args.input_file)
print("Output file:", args.output)
print("Mode:", args.mode)
print("Verbose:", args.verbose)
print("Repeat count:", args.repeat)
print("Log level:", args.log_level)
print("Tags:", args.tags)

# 基于解析的参数执行逻辑
if args.verbose:
    print("[Verbose Mode Enabled] Detailed processing information will be shown.")
    
for i in range(args.repeat):
    print(f"\nProcessing '{args.input_file}' in '{args.mode}' mode (Run {i+1}/{args.repeat})...")
    # 模拟处理逻辑
    if args.mode == "fast":
        print("Processing quickly...")
    elif args.mode == "slow":
        print("Processing slowly...")
    elif args.mode == "custom":
        print("Processing with custom settings...")

    # 处理标签
    if args.tags:
        print("Applying tags:", ", ".join(args.tags))

    print(f"Output will be saved to '{args.output}'.")

# 日志信息
if args.log_level:
    print(f"Log level set to: {args.log_level}")

```

# 4. 参考资料

+   [【Python进阶】argparse库基础用法全总结：高效脚本参数解析 | 参数类型使用代码-CSDN博客](https://blog.csdn.net/Q52099999/article/details/137028697)

+   [argparse --- 用于命令行选项、参数和子命令的解析器 — Python 3.13.0 文档](https://docs.python.org/zh-cn/3/library/argparse.html#module-argparse)
