# #Qual o resultado de:
# class Interno:
#     def __init__(self):
#         self.__x = 10
#
#     def exibe(self):
#         print(self.__x)
#
# i = Interno()
# i.__x = 5
# i.exibe()
########
# def f(a, b):
#     print(a - b)
#
# f(b=3, a=1)
#########
# while Verdadeiro:
#     print("Alô!")
#########
# def f(a, b=2):
#     return a + b
#
# print(f(3))
#########

# A = [1, 2, 3]
# A.append(4)
# print(A.pop())
##########
# a = 1
# b = "2"
# print(a + b)
#########
# for x in range(10):
#     print(x)
#########

# def f(a):
#     if a > 0:
#         return f(a - 1) * a
#     return 1

# def f(a):
#     b = 0
#     while a >= 1:
#         b *= a
#         a -= 1
#     return b
#
# print(f(10))

###########
# L = [1, 2, 3]
# L.extend([4, 5])
# print(L)
###########
# b = 5/ 3
# print(b)
##########
# a = 1500
# b = 3.0
# print(a/b)
###########
# A = [1, 2, 3]
# B = A[:]
# del B[1]
# print(A)
##########

# def f(v=[]):
#     v.append(1)
#     print(v)
#
# print(f())
# print(f())
# print(f())

###########

# Qual o número impresso ao final deste programa?
# x = 0
# while x < 9:
#    x += 1
# print(x)

###########

# a = 10
# print(f"{a}")
# print(f"{a:10}")
# print(f"{a:010}")
###########
# a = 1
# b = 2
# print(a % b)
##########

# v = 100.0
# while v != 0:
#     v -= 0.1
# print(v)

#########

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
#
# print(s.issubset(set([1,2,3,4])))

#########
#
# a = 10.129
# print(f"{a}")
# print(f"{a:10f}")
# print(f"{a:10.2f}")

#########

x = 0

def i(v):
    global x
    x += v

i(4)
i(5)
i(1)
print(x)