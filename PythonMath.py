class PythonMath(object):
    def transRadix2to10(self, x):
        # 基数変換 2進数 → 10進数
        y = 0
        for i,j in enumerate(reversed(x)):
            y += 2**i * j
        return y

    def transRadix2Dto10(self, x):
        # 基数変換 2進少数 → 10進数
        y = 0
        for i,j in enumerate(x):
            y += j / (2**(i+1))
        return y

    def transRadix8to10(self, x):
        # 基数変換 8進数 → 10進数
        if(x >= 10):
            xx = int(x / 10) * 10
            xxx = x - xx
            y = (int(x / 10) * 8) + xxx
            return y
        elif(7 < x and x < 10):
            print('Type Error: 8 ~ 9 Not Octal')
        else:
            return x
