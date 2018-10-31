########################################
# Simple 'Hello World' python program. #
########################################

avar, bvar = 12.0, 2
str1 = "Hello"
str2 = "World"
int1 = 12
cvar = avar + bvar

print (str1 + " " + str2)
print (avar)
print (float(bvar))
print ("result {w1} {w2}".format(w2 = str1, w1 = str2))

ls = [12, "non", 235]
print(ls[0])
print(ls[2])
print(ls[1])

print(7 ** 2)
print(2 ** 3)

shitTon ="SHIT" * 100
print(shitTon)

even = [2, 4, 6]
odd  = [1, 3, 5]
al   = even * 10
print(al)

name = "Quentin"
age = 25

print("\n")
print("%s is %d y.o" %(name, age))
