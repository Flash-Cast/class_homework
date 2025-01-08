# coding: utf-8
import sys
sys.stdout.reconfigure(encoding='utf-8')
# 文字化けが起きたためutf-8を指定

# 正規表現用
import re

try:
    # 整数を入力
    n = int(input("整数を入力してください"))
    
    # 学籍番号を入力
    student_num = input("学籍番号を入力してください")

    # 数字を抽出して整数に変換
    numbers = [int(num) for num in re.findall(r'\d+', student_num)]  

    # リストに2番目の要素があるか確認
    if len(numbers) == 2 :
        # 二つ目の文字列を採用
        student_num_under3 = numbers[1]

        # 条件分岐
        if student_num_under3 < n:
            print(f"入力した整数は {student_num_under3} よりも大きい")

        elif student_num_under3 == n:
            print(f"入力した整数は {student_num_under3} と等しい")

        else:
            print(f"入力した整数は {student_num_under3} よりも小さい")
        
    # 正しい学籍番号(数字の要素が二つ)ではないときにプログラムを終了する。
    else:
        print("正しい学籍番号ではありません")
        sys.exit()

# 整数入力時に文字列などが入力された際の例外処理
except ValueError:
    print("無効な入力です。整数を入力してください。")
