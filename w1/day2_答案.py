# Day 2 练习参考答案 —— 先自己写！实在卡住了再看这里
# 参考答案不是唯一写法，能跑通就是好代码

# ---------- 练习1 简易计算器 ----------
a = float(input("输入第一个数字："))
b = float(input("输入第二个数字："))
op = input("输入运算符(+ - * /)：")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("不能除以0")
    else:
        print(a / b)
else:
    print("不支持的运算符")

# ---------- 练习2 能被3整除的数 ----------
row = []
for i in range(1, 101):
    if i % 3 == 0:
        row.append(str(i))
for i in range(0, len(row), 10):        # 每10个一行
    print(" ".join(row[i:i+10]))

# ---------- 练习3 成绩单 ----------
scores = {"张三": 92, "李四": 45, "王五": 78, "赵六": 60}
pass_list, fail_list = [], []
for name, score in scores.items():
    if score >= 60:
        pass_list.append(name)
    else:
        fail_list.append(name)
print("及格:", pass_list)
print("不及格:", fail_list)

# ---------- 练习4 猜数字（挑战） ----------
import random
target = random.randint(1, 100)
count = 0
while True:
    guess = int(input("猜一个 1~100 的数字："))
    count += 1
    if guess > target:
        print("大了")
    elif guess < target:
        print("小了")
    else:
        print(f"恭喜！共猜了 {count} 次")
        break
