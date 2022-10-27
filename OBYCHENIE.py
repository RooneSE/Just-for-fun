# def spis(lst):
#     lst1 = []
#     for i in lst:
#         if i not in lst1:
#             lst1.append(i)
#     return lst1
#
# ss = [1, 2, 3, 4, 3, 3]
# print(spis(ss))
# print(list(set(ss)))
# lst = [1, 2, 3, 3, 4, 3, 3, 6, 534, 5, '3', 2, 54333, 5435, '5252', 'a']
# lst2 = []
#
# for i in lst:
#     if type(i) == str:
#         if i.isdigit():
#             i = int(i)
#             if i < 5:
#                 lst2.append(i)
#     elif i < 5:
#         lst2.append(i)
#
# print(lst2)


# a = [1, 2, 3, 9, 0]
# b = [1, 2, 3, 6, 4]
#
# result = filter(lambda x: x in a and x in b, a)
#
# print(list(result))



# dict_a = {1: 10, 2: 20}
# dict_b = {3: 30, 4: 40}
# dict_c = {5: 50, 6: 60}
#
# lst = [dict_c, dict_b, dict_a]
# def dictir(lst):
#     a = {}
#     for i in lst:
#         a.update(i)
#     return a
# print(dictir(lst))
fds



# set1 = set(['white', 'black', 'red'])
# set2 = set(['white', 'red', 'blue'])
#
# print(set1.difference(set2))
# print(set1 - set2)


l = [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]

for i in l:
    if l.count(i) >= 2:
        print('не уникальный')
    else:
        print('уникальный')
fskdfjsdfksdjfks