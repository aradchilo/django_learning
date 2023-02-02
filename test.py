# def get_sum(a, b):
#     return sum(range(min(a, b), max(a, b) +1))
#
# print(get_sum(-5, -2))

# def even_or_odd(number):
#     if number % 2 == 0:
#         return'Even'
#     else:
#         return 'Odd'

# alias_dict = {
#         'A': ('Alpha', 'Analogue'),
#         'B': ('Beta', 'Basstard'),
#         'C': ('Cache', 'Catalonia'),
#         'D': ('Dinasour', 'Discharge'),
#         'E': ('Exam', 'Electron'),
#         'F': ('Funeral', 'Faraday'),
#         'G': ('Gamma', 'Granny'),
#         'H': ('Heart', 'Hacker'),
#         'I': ('Ice', 'Idioto'),
#         'J': ('Jason', 'Jabber'),
#         'K': ('Keystroke', 'Killer'),
#         'L': ('Logic', 'Lazer'),
#         'M': ('Malware', 'Machine'),
#         'N': ('Noisy', 'Noob'),
#         'O': ('Odd', 'Over'),
#         'P': ('Palpatine', 'Paket'),
#         'Q': ('Quantum', 'Quark'),
#         'R': ('Radioactive', 'Roro'),
#         'S': ('Strike', 'Spy'),
#         'T': ('Tapok', 'T-Rex'),
#         'U': ('Ultraviolet', 'Utility'),
#         'V': ('Vanilla', 'Virus'),
#         'W': ('Warm', 'Worm'),
#         'X': ('Xerox', 'X'),
#         'Y': ('Yoda', 'Yarl'),
#         'Z': ('Zero', 'Zombie')
#     }

# def alias_gen(f_name, l_name):
#     error_message = 'Your name must start with a letter from A - Z.'
#     f_name = FIRST_NAME.get(f_name.upper()[0])
#     l_name = SURNAME.get(l_name.upper()[0])
#     if f_name and l_name:
#         return '{} {}'.format(f_name, l_name)
#     else:
#        return error_message

# def litres(time):
#     return int(time * 0.5 // 1)
#
# print(litres(3))

# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     res = [x for x in geese + birds if x not in geese]
#     return res
#
# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))

# def invert(lst):
#     new_list = []
#     for el in lst:
#         new_list.append(el * -1)
#     return new_list
#
# print(invert([1, 2, 3]))

# def add_length(str_):
#     new_list = str_.split(' ')
#     listOfThings = []
#     for el in new_list:
#         listOfThings.append(el + ' ' + str(len(el)))
#     return listOfThings
#
# print(add_length('Hello you bitch'))

# def how_many_light_sabers_do_you_own(name='empty'):
#     if name == 'Zach':
#         return 18
#     else:
#         return 0
#
# print(how_many_light_sabers_do_you_own('Zach'))

# def powers_of_two(n):
#     listofTwo = []
#     for x in range(n + 1):
#         listofTwo.append(2**x)
#     return listofTwo

# def grow(arr):
#     total = 1
#     for el in arr:
#         total *= el
#     return total
#
# print(grow([4, 1, 1, 1, 4]))

# vowels = ['a', 'i', 'e', 'o', 'u']
# def shortcut(s):
#     s_list = [char for char in s]
#     new_s = [letter for letter in vowels + s_list if letter not in vowels]
#     return str(''.join(new_s))
#
# print(shortcut('hello'))


# def hotpo(n):
#     error_msg = "n must be positive"
#     if n == 1:
#         return 0
#     elif n != 1:
#         count = 0
#         while n != 1:
#             if n % 2 == 0:
#                 n = n / 2
#                 count = count + 1
#             elif n % 2 > 0:
#                 n = 3 * n + 1
#                 count = count + 1
#         return count
#     elif n < 0:
#         return error_msg

# print(hotpo(23))


# def bar_triang(point_a, point_b, point_c):
#     x0_coord = round(((point_a[0] + point_b[0] + point_c[0]) / 3), 4)
#     format(x0_coord, '.4f')
#     y0_coord = round(((point_a[1] + point_b[1] + point_c[1]) / 3), 4)
#     format(y0_coord, '.4f')
#
#     return [x0_coord, y0_coord]
#
# print(bar_triang([23, 25], [34, 23], [24, 40]))

# 1. Взять индекс каждого координата
# 2. Посчитать по формуле
# 3. Сделать список из результатов
# 4. Ввести

# def quarter_of(month):
#     firstQ = [1, 2, 3]
#     secondQ = [4, 5, 6]
#     thirdQ = [7, 8, 9]
#     fourthQ = [10, 11, 12]
#
#     if month in firstQ:
#          return 1
#     elif month in secondQ:
#          return 2
#     elif month in thirdQ:
#         return 3
#     elif month in fourthQ:
#          return 4
#     else:
#         'There is no such month'

# print(quarter_of(5))

# value=input("2+2=")
# print(value)

class Solution:

    def countOdds(self, low: int, high: int) -> int:
        count_odd = 0

        for number in range(low, high + 1):
            if low < 0:
                raise ValueError('Low number is lower then 0')
            elif high > 10 ** 9:
                raise ValueError('High number is higher then 10^9')
            elif low > high:
                raise ValueError('Low number cannot ba higher then high one')
            else:
                if number % 2 != 0:
                    count_odd += 1
                else:
                    pass
        return count_odd


examp = Solution()
print(examp.countOdds(1, 10))

# def countOdds(low: int, high: int):
#     count_odd = 0
#     for number in range(low, high):
#         if number % 2 == 0:
#             count_odd += 1
#         else:
#             pass
#     return count_odd
