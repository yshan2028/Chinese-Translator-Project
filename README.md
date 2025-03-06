# 中文编程语言解释器

## 介绍
本项目是一个基于 Python 和 Lark 开发的中文解释型编程语言。它允许使用 **中文变量名、整数赋值、加法运算、输出** 语法，并可以直接运行 `.cn` 文件，类似 Python 解释器。

---

## 📌 功能特性
- **纯中文编程**：支持中文关键字，如 `整数`、`输出`。
- **变量赋值**：可以使用中文变量名，如 `甲 为 10`。
- **数学运算**：支持 `加` 运算符。
- **输出功能**：使用 `输出()` 打印变量值。

## 中文文档

[手册](https://github.com/yshan2028/Chinese-Translator-Project/wiki/%E4%B8%BB%E8%A6%81)

---

## 🛠️ 环境要求
- Python 3.7 及以上
- `lark-parser` 库（用于解析 `.cn` 代码）

---

## 🚀 安装

### **1️⃣ 安装 Python 依赖**
```bash
pip install -r requirements.txt
```

---

## 📄 示例代码 (`example.cn`)
```cn
整数 甲 为 10
整数 乙 为 25
整数 和 为 甲 加 乙
输出(和)
```

---

## 🎯 运行 `.cn` 文件
```bash
python interpreter.py example.cn
```

✅ 预期输出：
```
35
```

---

## 📌 目录结构
```
ChineseInterpreter/
├── interpreter.py    # 解释器核心程序
├── grammar.lark      # 中文语法定义文件
├── example.cn        # 示例中文代码
├── requirements.txt  # 依赖库
└── README.md         # 说明文档
```

---

## 🛠️ 未来扩展
- ✅ **支持小数、文本类型**
- ✅ **支持逻辑判断** (`若...则...否则`)
- ✅ **支持循环 (`重复...直到` 或 `循环`)**
- ✅ **支持函数定义 (`法...入...返`)**

---

## 📌 贡献
如果你对中文编程感兴趣，欢迎提交 PR 和 Issue ！🎉

---

## 📝 许可证
本项目基于 MIT 许可证开源。
