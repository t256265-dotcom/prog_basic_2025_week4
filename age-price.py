age = int(input("年齢: "))

if age < 0 or age > 120:
    print("年齢は0〜120で入力してください")
elif age <= 3:
    print("無料")
elif age <= 12:
    print("500円")
elif age <= 64:
    print("1000円")
else:
    print("700円")
