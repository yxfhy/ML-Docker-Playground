# 1 から 100 までの数字について、  
# 3 の倍数なら "Fizz"、5 の倍数なら "Buzz"、  
# 3 と 5 の両方の倍数なら "FizzBuzz" を出力する関数を実装してください
# それ以外の数字はそのまま出力してください
# 例: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, ... 
# ヒント: range() 関数を使うと便利です
def fizzbuzz():
    # 1 から 100 までの数字をループ
    for i in range(1, 101):
        # 3 と 5 の両方の倍数の場合
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # 3 の倍数の場合
        elif i % 3 == 0:
            print("Fizz")
        # 5 の倍数の場合
        elif i % 5 == 0:
            print("Buzz")
        # その他の場合はそのまま出力
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
    


