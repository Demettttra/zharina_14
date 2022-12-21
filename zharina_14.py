#1.
def dec(hello):
    def wrapper(arg):
        hello(str(arg).upper())
    return wrapper

@dec
def hello(name):
    print('Привет, ', name)
hello(input('Как тебя зовут?\n'))

#2.
def summa(a):
    if a==0:    return 0
    else:
        return a%10+summa(a//10)
print(summa(int(input('Введите число: '))))
