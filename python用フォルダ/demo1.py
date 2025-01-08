# coding: utf-8
import sys
sys.stdout.reconfigure(encoding='utf-8')
# 文字化けが起きたためutf-8を指定

try:
    # 整数を入力
    n = int(input("整数を入力してください"))

    # 比較する学籍番号下三桁
    student_num_under3 = 32

    # 条件分岐
    if student_num_under3 < n:
        print(f"入力した整数は {student_num_under3} よりも大きい")
    elif student_num_under3 == n:
        print(f"入力した整数は {student_num_under3} と等しい")
    else:
        print(f"入力した整数は {student_num_under3} よりも小さい")
# 以下、整数入力時に文字列などが入力された際の例外処理
except ValueError:
    print("無効な入力です。整数を入力してください。")
