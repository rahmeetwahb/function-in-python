import random

li1 = [10, 20, 30, 40, 50]
li2 = ['Rani', 'Bima', 'Eko', 'Mukhlas', 'Raya']

#before being shuffled
print('before shuffled')
print('li1', li1)
print('li2', li2)

random.shuffle(li1)
random.shuffle(li2)

#after being shuffled
print('after shuffled')
print('li1', li1)
print('li2', li2)