# Day 3: 函数 / 文件读写 / 异常处理
# 学习目标：把代码装进函数、把数据存进文件、让程序出错时不崩溃
# 这是 Day4 记账本和之后所有项目的基石。逐节运行示例，最后独立完成练习。

# ========== 第1节 函数 function ==========
# 函数 = 把一段代码打包起个名字，随时调用，避免重复写
def greet(name):
    return f"你好，{name}！"

print(greet("欧阳健"))

# 多个参数 + 默认参数（op 不传就用 "+"）
def calc(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "不能除以0"
        return a / b
    else:
        return "不支持的运算符"

print(calc(3, 5))        # 8
print(calc(3, 5, "-"))   # -2

# 作用域：函数里定义的变量是局部的；函数外的是全局的
x = 10                    # 全局变量
def add_one():
    y = x + 1             # 函数内可以"读"全局变量
    return y
print(add_one())          # 11

# 小知识：return 立刻结束函数；没有 return 的函数返回 None

# ========== 第2节 文件读写 ==========
# 程序关掉后数据还在 —— 记账本、日志、爬虫存储全靠文件

# 写入：w 覆盖写，a 追加写（不存在会自动创建）
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("2026-08-22 学了函数和文件读写\n")
# with ... as 会自动关闭文件（不用手写 f.close()），必须养成习惯

# 读取：整个读进来
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("--- 全部内容 ---")
print(content)

# 按行读（处理大文件时省内存）
print("--- 逐行读 ---")
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("行:", line.strip())     # strip() 去掉行尾换行符

# 编码：中文必须用 encoding="utf-8"，否则 Windows 上会乱码或报错

# ========== 第3节 异常处理 try / except ==========
# 程序遇到错误默认会崩溃，try/except 让它优雅处理
try:
    n = int(input("输入一个数字（我会用10除以它）："))
    print("10 /", n, "=", 10 / n)
except ValueError:
    print("那不是数字！")
except ZeroDivisionError:
    print("不能除以0！")
finally:
    print("无论对错，这行都会执行")

# 调试期想偷懒看所有错误：except Exception as e: print("出错:", e)
# 正式代码要写具体异常类型，不要裸用 except

# ================= 今日练习（先自己写，再看 day3_答案.py） =================
# 练习1 写函数 avg(scores)：返回列表的平均分；空列表返回 0（提示：判断 len）
# 练习2 写函数 save_log(msg)：把一行日志追加写入 study_log.txt（带时间戳）
#       再写函数 read_log()：读出全部内容并打印
#       （提示：from datetime import datetime;  datetime.now().strftime("%Y-%m-%d %H:%M")）
# 练习3 安全输入：用 try/except 循环让用户输入 1~100 的数字，
#       不是数字或超出范围就提示并重新输入，合法才退出
# 练习4（挑战，Day4 记账本预演）记账本 v0：
#       循环输入，格式 "收/支 金额 说明"（如：收 100 生活费 / 支 20 奶茶）
#       每笔写入 money.txt；输入"查"打印全部记录和当前余额；输入"退出"结束
#       （做出来 Day4 就轻松了，做不出来也没关系，明天一起做）
