from PythonMath import *


def main():
    # ライブラリ利用宣言
    math = PythonMath()

    # 2進数を10進数へ変換
    x = [1, 1, 0]
    y = math.tr2to10(x)
    print(x)
    print(y)

    print('')

    # 2進少数を10進数へ変換
    x = [1, 0, 1, 0, 1]
    y = math.tr2Dto10(x)
    print(y)

    # 8進数を10進数へ変換
    x = 21
    y = math.tr8to10(x)
    print(y)





if __name__ == '__main__':
    main()
