from PythonMath import *


def main():
    # ライブラリ利用宣言
    math = PythonMath()

    # 2進数を10進数へ変換
    x = [0, 1, 1]
    y = math.transRadix2to10(x)
    math.showBoxReversed(x)
    print(y)

    print('')

    # 8進数を10進数へ変換
    x = 21
    y = math.transRadix8to10(x)
    print(y)

    # 2進少数を10進数へ変換
    x = [1, 0, 1, 0, 1]
    math.showBoxReversed(x)


if __name__ == '__main__':
    main()
