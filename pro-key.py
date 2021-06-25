import random

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'

all = alpha+num
lenght = 5

key = ''.join(random.sample(all, lenght))
key2 = ''.join(random.sample(all, lenght))
key3= ''.join(random.sample(all, lenght))
key4 = ''.join(random.sample(all, lenght))

keycode = print(key,'-',key2,'-',key3,'-',key4)

