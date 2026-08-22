# Day 3 练习参考答案 —— 先自己写！卡住再看

# ---------- 练习1 平均分函数 ----------
def avg(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

print(avg([85, 92, 78]))   # 85.0
print(avg([]))             # 0

# ---------- 练习2 学习日志（文件读写 + 函数） ----------
from datetime import datetime

def save_log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("study_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

def read_log():
    try:
        with open("study_log.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "还没有日志，先写一条吧"

save_log("Day3 完成函数与文件读写练习")
print(read_log())

# ---------- 练习3 安全输入 ----------
while True:
    try:
        n = int(input("输入 1~100 的数字："))
        if 1 <= n <= 100:
            print(f"合法！你输入了 {n}")
            break
        else:
            print("超出范围，重新来")
    except ValueError:
        print("那不是数字，重新来")

# ---------- 练习4 记账本 v0（挑战） ----------
# 每笔记录一行: "收 100 生活费" / "支 20 奶茶"
while True:
    cmd = input("输入(收/支 金额 说明 | 查 | 退出)：")
    if cmd == "退出":
        print("已退出记账本")
        break
    if cmd == "查":
        total = 0
        try:
            with open("money.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print(line.strip())
                    parts = line.split()
                    amount = float(parts[1])
                    total += amount if parts[0] == "收" else -amount
        except FileNotFoundError:
            print("还没有任何记录")
        print(f"当前余额: {total:.2f}")
        continue
    # 解析输入 "收 100 生活费"
    parts = cmd.split()
    if len(parts) < 3 or parts[0] not in ("收", "支"):
        print("格式不对，示例：收 100 生活费")
        continue
    try:
        float(parts[1])
    except ValueError:
        print("金额必须是数字")
        continue
    with open("money.txt", "a", encoding="utf-8") as f:
        f.write(cmd + "\n")
    print("已记录 ✅")
