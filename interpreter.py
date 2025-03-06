from lark import Lark, Transformer
import sys

# ✅ 直接在 Python 代码中加载 Lark 语法文件
with open("grammar.lark", "r", encoding="utf-8") as f:
    grammar = f.read()

# ✅ 解析器
parser = Lark(grammar, parser="lalr", start="start")

# ✅ 解释器核心逻辑
class Interpreter(Transformer):
    def __init__(self):
        self.vars = {}  # 变量存储

    def assign(self, items):
        """ 处理变量赋值 """
        name, value = items
        self.vars[name] = value

    def output(self, items):
        """ 处理 输出() 语法 """
        print(items[0])

    def add(self, items):
        """ 处理 加法运算 """
        left, right = items
        return left + right

    def number(self, items):
        """ 解析数字 """
        return int(items[0])

    def var(self, items):
        """ 解析变量 """
        var_name = items[0]
        if var_name in self.vars:
            return self.vars[var_name]
        else:
            raise ValueError(f"错误：变量 '{var_name}' 未定义")

# ✅ 运行解释器
def run_cn(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    tree = parser.parse(code)
    interpreter = Interpreter()
    interpreter.transform(tree)

# ✅ 运行入口
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python interpreter.py example.cn")
        sys.exit(1)

    run_cn(sys.argv[1])