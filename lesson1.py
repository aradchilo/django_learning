# import turtle
#
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.append(6)
# print(numbers)
#
# for i in range(8, 21):
#     numbers.append(i)
# print(numbers)
#
# print(numbers[::-1])
#
# print('=========================')
#
# print(list(range(0, 2)))
#
# print('=========================')
#
# listnum = list(range(0, 3))
# print(listnum)
#
#
# def sum_list(new_list):
#     theSum = 0
#     for number in new_list:
#         theSum = theSum + number
#     return theSum
#
#
# print(sum_list(listnum))
#
# print('=========================')
#
# count = 0
# while count < 50:
#     count = count + 5
#     print(count)
#
# print('=========================')
#
#
# def last_letter(my_string):
#     return my_string[-1]
#
#
# print(last_letter('Hello, bitch'))
#
# print('=========================')
#
#
# def bigger_boy(my_list):
#     max_temp = 0
#     for item in my_list:
#         if item > max_temp:
#             max_temp = item
#     return max_temp
#
# print(bigger_boy([5, 7, 9]))
#
#
# print('=========================')


def factor(factorial):
    count = 1
    for number in range(1, factorial + 1):
        count = count * number
    return count


print(factor(5))


def fuck(factorialchik):
    if factorialchik > 0:
        return factorialchik * fuck(factorialchik - 1)
    else:
        return factorialchik


print(fuck(4))
