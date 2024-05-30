str1 = '  python'
str2 = 'python11'
str3 = '--python--'

print('str1: ', str1)
print('str1.lstrip(): ', str1.lstrip())

print('\nstr2: ', str2)
print('str2.rstrip(): ', str2.rstrip('1'))

print('\nstr3: ', str3)
print('str3.strip()', str3.strip('-'))