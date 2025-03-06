from lark import Lark, Transformer
import sys

# ✅ 载入 grammar.lark 语法
with open("grammar.lark", "r", encoding="utf-8") as f:
    grammar = f.read()

class Interpreter(Transformer):
    def __init__(self):
        self.vars = {}  # 存储变量
        self.functions = {}  # 存储函数
        self.return_value = None  # 存储 `返` 的返回值

    def assign(self, items):
        """ 变量赋值 """
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

    def func_def(self, items):
        """ 解析 `功能` 语法，存储函数 """
        name = items[0]

        # ✅ 处理参数，支持 `（甲,乙）` 和 `甲,乙`
        if isinstance(items[1], list):
            params = items[1]
        else:
            params = [p for p in items[1].children] if hasattr(items[1], 'children') else []

        body = items[2] if len(items) > 2 else []  # ✅ 确保 `body` 不为空
        self.functions[name] = (params, body)

    def func_call(self, items):
        """ 解析 `整数 和 取 加法(甲, 乙)` 语法 """
        result_var, func_name, args = items[0], items[1], items[2]

        if func_name not in self.functions:
            raise ValueError(f"错误：功能 '{func_name}' 未定义")

        params, body = self.functions[func_name]
        args = [a for a in args.children] if hasattr(args, 'children') else []  # ✅ 确保 `args` 是列表

        local_vars = dict(zip(params, args))  # ✅ 确保 `params` 和 `args` 都是列表
        return_value = self.execute_function(body, local_vars)

        self.vars[result_var] = return_value  # ✅ 将返回值赋给调用变量

    def return_stmt(self, items):
        """ 处理 `返` 语法，存储返回值 """
        self.return_value = items[0]

    def execute_function(self, body, local_vars):
        """ 执行函数 """
        prev_vars = self.vars.copy()  # 备份全局变量
        self.vars.update(local_vars)  # 使用局部变量
        self.return_value = None  # 重置返回值

        # ✅ 处理空函数体
        if not body or not hasattr(body, "children"):
            self.vars = prev_vars
            return None

        for stmt in body.children:
            if stmt and hasattr(stmt, "data") and stmt.data == "return_stmt":
                self.return_stmt(stmt.children)
                break
            self.transform(stmt)  # ✅ 替换 `_dispatch(stmt)`

        result = self.return_value  # ✅ 记录返回值
        self.vars = prev_vars  # 恢复全局变量
        return result  # ✅ 返回 `返` 语法的值

# ✅ 运行解释器
def run_cn(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    parser = Lark(grammar, parser="lalr", start="start")
    tree = parser.parse(code)
    interpreter = Interpreter()
    interpreter.transform(tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python interpreter.py example.cn")
        sys.exit(1)

    run_cn(sys.argv[1])