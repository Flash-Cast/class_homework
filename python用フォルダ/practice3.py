import math

# C0, C1, C2を入力
C0 = float(input("定数項を入力してください: "))
C1 = float(input("一次の係数を入力してください: "))
C2 = float(input("二次の係数を入力してください: "))

# 動的に方程式を構築する関数
def format_equation(C0, C1, C2):
    equation = ""
    if C2 != 0:
        equation += f"{C2}x²"
    if C1 != 0:
        if equation:
            equation += f" + {C1}x" if C1 > 0 else f" - {abs(C1)}x"
        else:
            equation += f"{C1}x"
    if C0 != 0:
        if equation:
            equation += f" + {C0}" if C0 > 0 else f" - {abs(C0)}"
        else:
            equation += f"{C0}"
    return equation + " = 0"

# 一次方程式の解を計算
def linear_equation(C0, C1):
    if C1 == 0:
        print("警告：C1はゼロです。一次方程式の解はありません。")
    else:
        x = -C0 / C1
        equation1 = format_equation(C0, C1, 0)
        print(f"一次方程式「{equation1}」の解は x = {x}")

# 二次方程式の解を計算
def quadratic_equation(C0, C1, C2):
    if C2 == 0:
        # C2が0の場合、一次方程式として処理
        linear_equation(C0, C1)
        return
    D = C1 ** 2 - 4 * C2 * C0  # 判別式
    equation2 = format_equation(C0, C1, C2)
    if D > 0:
        x1 = (-C1 + math.sqrt(D)) / (2 * C2)
        x2 = (-C1 - math.sqrt(D)) / (2 * C2)
        print(f"二次方程式「{equation2}」の実数解は x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -C1 / (2 * C2)
        print(f"二次方程式「{equation2}」の解は x1 = x2 = {x} (重解)")
    else:
        real_part = -C1 / (2 * C2)
        imaginary_part = math.sqrt(-D) / (2 * C2)
        print(f"二次方程式「{equation2}」の虚数解は x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

# 方程式を計算する関数
def pracf():
    if C2 == 0:
        linear_equation(C0, C1)
    else:
        quadratic_equation(C0, C1, C2)

# 実行
pracf()
