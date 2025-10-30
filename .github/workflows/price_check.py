price_input=input("価格を入力してください：")
if not price_input.isdigit():
    print("数字を入力してください")
else:
    price=int(price_input)
if price<0:
    print("0以上を入力してください")   
elif price>=10000:
    print("高額商品です") 
tax_inculuded=int(price*1.1)
print(f"税込み価格は{tax_inculuded}円です")