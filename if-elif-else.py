try:
    price = int(input("価格を入力してください: "))
    print(f"税込価格は {price * 1.1} 円です")
except ValueError:
    print("数字を入力してください！")
