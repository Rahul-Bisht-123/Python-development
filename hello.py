# exploring the print() function of python

# print('this line will get print')
# print(55+33)
# print('ram'+'singh')
# print(True)
# print(False)
# print(7.99+6.55)
# print(1_00_000)
# print(5.9 + 99)

# ----------------helper function for module.py----------

def fib(n):
    fibo = []
    a,b = 0,1
    while a < n:
        fibo.append(a)
        a,b = b,a+b
    return fibo