# 関数を定義
def demo2f():
    try:
        # 整数を入力
        n = int(input("整数を入力してください"))
        
        # 学籍番号下三桁の整数を記述
        student_num_under3 = 32

        # 条件分岐
        if student_num_under3 < n:
            print(f"入力した整数は {student_num_under3} よりも大きい")

        elif student_num_under3 == n:
            print(f"入力した整数は {student_num_under3} と等しい")

        else:
            print(f"入力した整数は {student_num_under3} よりも小さい")

    # 整数入力時に文字列などが入力された際の例外処理
    except ValueError:
        print("無効な入力です。整数を入力してください。")

# 比較回数を入力
hikaku_n = int(input("整数を何回比較しますか？"))
# 入力回数分関数を実行
for i in range(hikaku_n):
    print(i+1,"回目の整数比較")
    demo2f()