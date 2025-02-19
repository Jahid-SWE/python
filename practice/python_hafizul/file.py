
#file read process
# file = open("python/practice/python_hafizul/file/file.txt", "r")
# text = file.read()
# print(text)

#file write with append
'''file = open("python/practice/python_hafizul/file/file.txt", "a")
txt = file.write("\nBis millah Hir Rahma nir rahim")
print(txt)'''


# TypeError,ValueError,ZeroDivisionError, NameError,

'''try:
    number = int(input('Enter your Name : '))
    result = 10/number
    print(result)
except(TypeError,ValueError,ZeroDivisionError, NameError):
    print("Invalid Key ")'''

try:
    name = input(" Enter your name : ")
    print(name[50])
except(IndexError):
    print("pleas select range between star to end")