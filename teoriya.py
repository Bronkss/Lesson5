# Семинар 5.

# n = int(input("Введите число: "))
#
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(n - 1))



# list = [2, 3, 4, 5 , 5, 6 , 6] # 2, 3, 4, 2 ,2
# max_number = max(list)
# min_number = min(list)
#
# for i in range(len(list)):
#     if list[i] == max_number:
#         list[i] = min_number
#
# print(list)


# user_numbers = int(input("Введите число, а программа проверит является лт оно простым: "))
#
# for i in range(user_numbers):
#     if user_numbers // 1 == 0 :
#         print("Yes")
#     elif user_numbers // user_numbers == 0:
#         print("Yes")
#     else:
#         print('No')


# def isSimple(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
# print(isSimple(5))




# magazine = [int(input("Введите оценку: ")) for _ in range(int(input("Введите количество оценок: ")))]
# list comprehension
# print(magazine)

# import random
# import time
# magazine = [random.randint(2, 5) for _ in range(10)]
# # list comprehension
# start = time.perf_counter()
# maxx = max(magazine)
# minn = min(magazine)
# end = time.perf_counter()
# print(magazine)
#
# for ind in range(0, len(magazine)):
# if magazine[ind] == maxx:
# magazine[ind] = minn
# print(magazine)








