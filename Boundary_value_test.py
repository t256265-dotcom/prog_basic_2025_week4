# 年齢が有効かどうかをチェックする関数
def is_valid_age(age):
    """年齢が 0〜120 の範囲なら True、それ以外は False を返す"""
    if 0 <= age <= 120:
        return True
    else:
        return False


# 境界値テスト
tests = [-1, 0, 1, 119, 120, 121, "abc"]

for t in tests:
    try:
        print(t, "->", is_valid_age(int(t)))
    except Exception as e:
        print(t, "->", e)
