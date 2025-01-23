#必要なライブラリを導入(mathライブラリ,statisticsライブラリ,tabulateライブラリ)
import math
import statistics
from tabulate import tabulate

#数値を格納するリストを作成
num_list = []

try:
    #計算に使用する数値の入力回数を決める
    times = int(input("入力したい整数の個数を決めてください："))

    #先に決めた入力回数分の整数を入力してリストに格納
    for i in range(times):
        print(i + 1,"回目の入力")
        value = int(input("追加する整数："))
        num_list.append(value)

    #手動計算で平均値を出すユーザー定義関数
    #引数をdataにすることで汎用性向上
    def manual_mean(data):
        total = 0
        count = 0
        for a in data:
            total += a
            count += 1

        #要素の有無で条件分岐
        if count > 0:
            average = float(total / count)
            return average
        
        #要素がないときに警告を表示
        else:
            print("警告：数値がありません。")
            return None
        
    #手動計算で標準偏差を出すユーザー定義関数
    #引数をdataにすることで汎用性向上
    def manual_stdev(data):
        count = 0
        total = 0
        for x in data:
            total += x
            count += 1

        #要素の有無で条件分岐
        if count > 0:
            mean = float(total / count)

            variance = 0
            for x in data:
                variance += (x - mean) ** 2
            variance /= count

            std_dev = float(math.sqrt(variance))
            return std_dev
        #要素がないときに警告を表示
        else:
            print("警告：標準偏差を計算できません。")
            return None

    #作成したリストをもとにユーザー定義関数を使用した結果を代入
    manual_average = manual_mean(num_list)
    manual_std_dev = manual_stdev(num_list)

    #statisticsライブラリを用いて計算した結果を変数に代入
    library_average = float(statistics.mean(num_list))
    library_std_dev = float(statistics.pstdev(num_list))

    #二つの方法でそれぞれ出した結果をresultsリストに格納
    results = [
        ["平均値", manual_average, library_average],
        ["標準偏差", manual_std_dev, library_std_dev]
    ]

    #表で出力することで比較を視覚的にわかりやすくする。
    headers = ["項目", "手動計算結果", "ライブラリ結果"]
    print(tabulate(results, headers=headers, tablefmt="pretty"))

#初めに数字以外を入力したときに例外処理
except ValueError:
    print("エラーです。")