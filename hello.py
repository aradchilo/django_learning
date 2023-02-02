# print('Hello, World!'[:6] + ' bitch')

data = 'XBOX 360 | 150 | New'

print(data.index('|'))
product = data[:data.index('|')]
print(product)

price = data[(data.index('|') + 1):data.rindex('|')]
print(price)

condition = data[(data.rindex('|') + 1):]
print(condition)

print('========================================================')

data_list = data.split('|')
print(data_list)

for i in data_list:
    print(i)

print('========================================================')


def find_first_index(benis):
    for index_of_el, el in enumerate(benis):
        if el == '|':
            return index_of_el
    else:
        return -1


def find_last_index(vori_tsak):
    temp = -1
    for inx, el in enumerate(vori_tsak):
        if el == '|':
            temp = inx
    return temp


print(find_last_index(data))
print(find_first_index(data))

print('========================================================')

name, price, cond = data.split('|')
print(name)
print(price)
print(cond)

print('========================================================')

print (data.find('|', data.find('|')+1))