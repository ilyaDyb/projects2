def func(str1, str2):
    if type(str1) is not str or type(str2) is not str:
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and len(str1) > len(str2) and str2 != 'learn':
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3


print(func(1, 'asdasd'))
print(func('asdasd', 'asdasd'))
print(func('asdasd', 'asdas'))
print(func('asdasd', 'learn'))

