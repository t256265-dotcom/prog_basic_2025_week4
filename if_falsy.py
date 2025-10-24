# name = input("名前を入力してください: ")

# if name:                     # 空でなければTrue
#     print(f"こんにちは、{name}さん！")
# else:
#     print("名前が入力されていません")

try:
    # 価格の入力
    price = int(input("価格を入力してください: "))

    # 範囲チェック
    if price < 0:
        print("0以上を入力してください。")
    else:
        if price >= 10000:
            print("高額商品です。")

        # 税込計算（税率10%）
        total = price * 1.1
        print(f"税込価格は {total:.2f} 円です。")

except ValueError:
    # 数字以外の入力に対応
    print("数字を入力してください！")

