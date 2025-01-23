import math
import statistics
from tabulate import tabulate
num_list = []
try:
    times = int(input("入力したい整数の個数を決めてください："))

    for i in range(times):
        print(i + 1,"回目の入力")
        value = int(input("追加する整数："))
        num_list.append(value)


    def manual_mean(data):
        total = 0
        count = 0
        for a in data:
            total += a
            count += 1
        
        if count > 0:
            average = float(total / count)
            return average
        else:
            print("数値がありません。")
            return None

    def manual_stdev(data):
        count = 0
        total = 0
        for x in data:
            total += x
            count += 1
        
        if count > 0:
            mean = float(total / count)

            variance = 0
            for x in data:
                variance += (x - mean) ** 2
            variance /= count

            std_dev = float(math.sqrt(variance))
            return std_dev
        else:
            print("標準偏差を計算できません。")
            return None

    manual_average = manual_mean(num_list)
    manual_std_dev = manual_stdev(num_list)

    library_average = float(statistics.mean(num_list))
    library_std_dev = float(statistics.pstdev(num_list))

    results = [
        ["平均値", manual_average, library_average],
        ["標準偏差", manual_std_dev, library_std_dev]
    ]

    headers = ["項目", "手動計算結果", "ライブラリ結果"]
    print(tabulate(results, headers=headers, tablefmt="pretty"))

except ValueError:
    print("エラーです。")