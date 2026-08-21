# Day 2: Python 核心基础 —— 变量 / 条件 / 循环 / 列表与字典
# 学习目标：学完后能独立写出"判断 + 循环 + 处理数据"的脚本
# 方法：每一节先读注释，然后逐行运行示例（VS Code 里点右上角 ▶），最后独立完成底部练习

# ========== 第1节 变量与数据类型 ==========
# 变量 = 给数据起个名字（相当于贴标签），之后可以用名字引用它
name = "欧阳健"        # 字符串 str：用引号包起来
age = 22               # 整数 int
height = 1.75          # 浮点数 float（带小数）
is_studying = True     # 布尔 bool（True/False 判断用）

print(type(name), type(age), type(height), type(is_studying))
# 输出: <class 'str'> <class 'int'> <class 'float'> <class 'bool'>

# 字符串拼接 vs f-string（面试手写代码常用 f-string，推荐掌握）
print("我叫" + name + "，今年" + str(age) + "岁")       # 拼接：数字要转 str
print(f"我叫{name}，今年{age}岁，身高{height}米")        # f-string：直接插值

# 注意：input() 返回的一律是字符串，要参与计算必须先转换
n = int(input("输入一个数字（我会把它乘以2）："))
print("结果 =", n * 2)

# ========== 第2节 条件判断 if / elif / else ==========
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 比较运算符: >  >=  <  <=  ==  !=    逻辑运算符: and  or  not
print(age >= 18 and age < 60)   # True
print(not is_studying)          # False

# ========== 第3节 循环 for / while ==========
# for + range：重复固定次数
for i in range(5):              # range(5) 生成 0,1,2,3,4
    print(i, end=" ")
print()

# for + enumerate：遍历列表时同时拿到"序号"和"内容"（Day1 的 hello.py 用过）
plan = ["第1周 基础", "第2周 pandas", "第3周 分析"]
for i, step in enumerate(plan, 1):
    print(f"{i}. {step}")

# while：条件成立就一直循环（小心死循环）
total, n = 0, 1
while n <= 100:
    total += n
    n += 1
print("1 加到 100 =", total)     # 5050（高斯的故事，也是 while 经典入门）

# break = 提前跳出循环；continue = 跳过本次进入下一次
for i in range(1, 6):
    if i == 3:
        continue        # 跳过 3
    if i == 5:
        break           # 到 5 直接结束
    print(i, end=" ")
print()

# ========== 第4节 列表 list 与字典 dict ==========
# 列表：有序、可改，用 [ ] 
scores = [85, 92, 78, 60, 45]
scores.append(99)                       # 末尾追加
print(scores[0], scores[-1], len(scores))  # 第一个、最后一个、长度
print("平均分 =", sum(scores) / len(scores))

# 字典：键值对，用 { } —— 真实业务数据（如一条用户记录）长这样
user = {"name": "张三", "score": 92, "city": "广州"}
print(user["name"], user.get("score"))
for k, v in user.items():
    print(k, "->", v)

# ================= 今日练习（先自己写，写完再看 day2_答案.py） =================
# 练习1 简易计算器：输入两个数字和一个运算符(+ - * /)，输出结果；除数为 0 时提示"不能除以0"
# 练习2 输出 1~100 中所有能被 3 整除的数字（每 10 个换一行）
# 练习3 成绩单：dict = {"张三": 92, "李四": 45, "王五": 78, "赵六": 60}
#       分别输出"及格名单"和"不及格名单"（≥60 及格）
# 练习4（挑战）猜数字：程序随机生成 1~100 的整数，你输入数字猜；
#       大了提示"大了"，小了提示"小了"，猜中输出"恭喜！共猜了 X 次"
#       （提示：import random;  target = random.randint(1, 100)）
