from decorates import time_this, time_Class

@time_this(40)
def my_func_fibonachi(n):
    fib1 = 1
    fib2 = 2
    n = int(n)
    i = 0
    fib_sum=0
    while i < n:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i=i+1
        print(fib2)
@time_Class
def my_f(n):
    s=0
    for j in range(n):
        j=j**3
        s=s+j
        print(s)
    print(s)


def  main():
    print("Проверяем декоратор-класс и декоратор-функция")
    mode = input("Выбери режим.\n1 - Проверяем декоратор-класс\n2 - Проверяем декоратор-функция\n")

    if mode == "1":
        n=input("Введите число итераций для функции my_f(n) >500")
        my_f(int(n))
    elif mode == "2":
        n = input("Введите число итераций для функции my_func_fibonachi(n) >200")
        my_func_fibonachi(int(n))


if __name__ == "__main__":
    main()
# my_f(1000)
# my_func_fibonachi(500)


