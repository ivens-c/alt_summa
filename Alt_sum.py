from time import *

num1 = int(input('Ввведите а:'))
num2 = int(input('Введите b:'))

def summa_chisel (num1,
                  num2) -> int:
    start = time()
    sleep(num1)
    sleep(num2)
    return int(time() - start)
print(summa_chisel(num1, num2))
