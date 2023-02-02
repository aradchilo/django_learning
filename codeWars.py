# I have four positive integers, A, B, C and D, where A < B < C < D.
# The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order.
# Your task is to return the value of D.
from audioop import reverse

# def alphabet(ns):
#     ns_sorted = sorted(ns)
#     num_a = min(ns_sorted)
#     ns_sorted.remove(num_a)
#     num_b = min(ns_sorted)
#     ns_sorted.remove(num_b)
#     ns_sorted.remove(num_a*num_b)
#     num_c = min(ns_sorted)
#     ns_sorted.remove(num_c*num_b)
#     return min(ns_sorted)
#
#
# print(alphabet([2, 3, 4, 1, 12, 6, 2, 4]))
# print(alphabet([2, 6, 7, 3, 14, 35, 15, 5]))
# print(alphabet([20, 10, 6, 5, 4, 3, 2, 12]))
# print(alphabet([20, 10, 6, 5, 4, 3, 2, 12]))
# print(alphabet([2, 6, 18, 3, 6, 7, 42, 14]))

# def reverse_words(s):
#     list_s = s.split(' ')
#     list_s.reverse()
#     s = ' '.join(list_s)
#     return s
#
#
# print(reverse_words('Hello bitch!'))


def sum_arrays(arrays, shift):
    temp_array = []
    for idx, x in enumerate(arrays):
        temp = [0] * idx * shift + arrays[idx]
        temp_array.append(temp)
    print(temp_array)

    for element, y in enumerate(temp_array):
        sum_list =


arr = [[1, 2, 3], [7, 7, 7], [8, 8, 8]]

sum_arrays(arr, 3)
