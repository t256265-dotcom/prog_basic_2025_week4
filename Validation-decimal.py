x = input("整数を入力してください: ")

try:
    num = int(x)   # ← 数字でなければここでエラー
    print(f"{num} は整数です！")
except ValueError:
    print("数字を入力してください。")
