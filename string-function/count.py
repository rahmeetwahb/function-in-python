str = "hello world"
a = str.count('l')
b = str.count('o')
c = str.count('l', 1, 6)

print("Letter 'l' inner str: ", a)
print("Letter 'o' inner str: ", b)
print("Letter 'l' from index 1-6: ", c)