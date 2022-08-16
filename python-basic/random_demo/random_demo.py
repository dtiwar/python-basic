from random import random,randint,choice,choices ,shuffle
import string
# print(random())
# print(randint(1,10))

options_list=[1,2,3,4,5,6,7,8,9]
options_str="abcdefg"
print(choice(options_list))

print(choices(options_list,k=3))
result_str=choices(options_str,k=2)
print(result_str)
print(type(options_str))
print(type(result_str))

result_str=choices(options_str,k=4)

# print("".join(choices(options_str,k=4)))


print("".join(choices(string.ascii_letters,k=4)))
print("".join(choices(string.ascii_letters + string.digits,k=5)))

print(options_list)
print(shuffle(options_list))
print(options_list)



