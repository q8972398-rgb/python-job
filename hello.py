# Day 1: 我的 Python 求职之旅 —— 第一个脚本
# 运行方式: 在终端里执行  python hello.py

print("你好，我是欧阳健，27届，目标是 Python 数据分析方向实习！")

# 我的 8 周作战计划（列表）
plan = [
    "第1周  环境搭建 + Python/SQL 基础",
    "第2-3周 pandas 数据清洗与探索分析",
    "第4-5周 业务深度分析 + 可视化报告",
    "第6周  AI 亮点功能 + 部署上线",
    "第7周  机器学习入门（第二项目）",
    "第8周  简历 + 全面投递",
]
for i, step in enumerate(plan, 1):
    print(f"{i}. {step}")

# 每日打卡（输入输出）
today = input("今天你学到了什么？输入后回车：")
print(f"收到！今天你学会了：{today}，明天继续加油 💪")
