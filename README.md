# 中文解释器示例项目

## 项目背景

编程语言是人与计算机交流的桥梁，是程序员的工具。目前，主流的编程语言都是英文编写的，如Python、Java、C++等。但是，对于一些不熟悉英文的人来说，学习编程语言可能会有一定的障碍。
所以，有人想到，是否可以用中文编写编程语言呢？这样一来，不熟悉英文的人也可以轻松学习编程了。但是，中文编程语言并不是那么容易实现的，因为编程语言需要有严谨的语法规则，而中文的表达方式并不那么严谨。
不过，我们可以通过解释器的方式来实现中文编程语言。解释器是一种特殊的程序，它可以解析并执行特定的代码，而不需要编译成机器码。通过解释器，我们可以实现一种简单的中文编程语言，让不熟悉英文的人也能学习编程。

一、项目结构设计

中文解释器项目
├── cn_interpreter.py    # 解释器核心程序
├── grammar.lark         # 中文语言语法定义
├── example.cn          # 中文代码示例文件
└── README.md           # 使用说明文档（可选）



⸻

二、每个文件的具体内容：

① 中文解释器主程序（compiler.py）

# compiler.py: 中文解释器
from lark import Lark, Transformer
import sys

grammar = '''
start: statement+

statement: "整数" NAME "为" expr          -> assign
         | "输出" "(" expr ")"            -> output

?expr: expr "加" expr                    -> add
     | NUMBER                            -> number
     | NAME                              -> var

%import common.NUMBER
%import common.CNAME -> NAME
%import common.WS_INLINE
%ignore WS_INLINE
'''

class Interpreter:
    def __init__(self):
        self.vars = {}

    def execute(self, tree):
        for stmt in tree.children:
            method = getattr(self, stmt.data)
            method = stmt.data
            getattr(self, method)(stmt)

    def assign(self, name, value):
        self.vars[name] = value

    def expr(self, node):
        if node.data == 'add':
            return self.evaluate(node.children[0]) + self.evaluate(node[1])
        elif node.data == 'number':
            return int(node.children[0])
        elif node.data == 'var':
            var_name = node.children[0]
            return self.vars.get(var_name, 0)

    def evaluate(self, node):
        return self.execute_expr(node)

    def run(self, source_code):
        parser = Lark(grammar)
        tree = parser.parse(source_code)
        self.execute(tree)

class TreeTransformer(Interpreter):
    def assign(self, node):
        var_name = node.children[0]
        value = self.evaluate(node.children[1])
        self.vars[var_name] = value

    def var(self, name):
        return self.vars[name[0]]

    def number(self, n):
        return int(n[0])

    def add(self, items):
        left, right = items
        return left + right

    def output(self, items):
        print(*items)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("用法： python compiler.py example.cn")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        code = f.read()

    parser = Lark(grammar)
    tree = parser.parse(code)
    interpreter = TreeInterpreter()
    interpreter.visit(tree)



⸻

② 中文语法定义文件（grammar.lark）

start: statement+

statement: "整数" NAME "为" expr        -> assign
         | "输出" "(" expr ")"          -> output

?expr: expr "加" expr  -> add
     | NUMBER          -> number
     | NAME            -> var

%import common.NUMBER
%import common.CNAME -> NAME
%import common.WS
%ignore WS



⸻

③ 中文示例源码（example.cn）

整数 甲 为 10
整数 乙 为 20
整数 结果 为 甲 加 乙
输出(结果)



⸻

④ 使用说明文件（README.md）

# 中文解释器示例项目

这是一个简单的中文解释型编程语言示例，类似于Python，但使用纯中文编写代码。

## 环境要求：
- Python >= 3.7
- lark-parser库

### 安装依赖
```bash
pip install lark

如何运行中文程序

python compiler.py example.cn

示例结果：

30



⸻

三、下一步的扩展建议：
	•	支持更多数据类型（如小数、文本、判断）
	•	支持控制结构（如若...则、否则、循环）
	•	支持函数定义调用
	•	内置中文标准库函数，方便中文生态建设

这样一来，你就能实现你设想的类似Python的中文解释型语言，安装解释器（compiler.py）后即可直接运行.cn文件，无需额外编译步骤。