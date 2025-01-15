# mathライブラリを導入
import math

# C0,C1,C2を入力
C0 = float(input("定数項を入力してください"))
C1 = float(input("一次の係数を入力してください"))
C2 = float(input("二次の係数を入力してください"))

# 一次方程式の解を導く関数を定義
def linear_equation():
    if C1 == 0:
        print("警告：C1はゼロです。")

    else:
        x = -C0/C1
        print(f"一次方程式の解は x = {x}")

# 二次方程式の解を導く関数を定義
def quadratic_equation():

    # C2が0の場合と0ではない場合に分岐
    if C2 == 0:
        
        # C2のみが0の場合とC1とC2どちらもが0の場合に分岐
        if C1 == 0:
            print("警告：C1とC2はゼロです。")
        
        # C2のみが0の時、一次方程式として扱う
        else:
            linear_equation()
    
    else:
        # 判別式
        D = C1 ** 2 - 4 * C2 * C0
        # 判別式の結果に応じて分岐
        if D > 0:
            # 実数解が2つある場合
            x1 = (-C1 + math.sqrt(D)) / (2 * C2)
            x2 = (-C1 - math.sqrt(D)) / (2 * C2)
            print(f"二次方程式の実数解は x1 = {x1}, x2 = {x2}")
        elif D == 0:
            # 重解の場合
            x = -C1 / (2 * C2)
            print(f"二次方程式の重解は x = {x}")
        else:
            # 虚数解の場合
            real_part = -C1 / (2 * C2)
            imaginary_part = math.sqrt(-D) / (2 * C2)
            print(f"二次方程式の虚数解は x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")
        
# それぞれの関数をまとめた関数を定義
def pracf():
    linear_equation()
    quadratic_equation()

# 定義した関数を実行
pracf()