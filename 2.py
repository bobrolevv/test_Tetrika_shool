from mwclient import Site

dict = ('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ')
site = Site('ru.wikipedia.org')
result = {}

# category = site.categories['Животные_по_алфавиту']
# for page in category:
    # with open('example.txt', 'a') as f:
    #     f.write(f'{page.name}\n')


with open('example.txt') as f:
    category = f.readlines()


for symbol in dict:
    i = 0
    for item in category:
        if item[0] == symbol:
            i += 1
    result[symbol] = i

print(result)



