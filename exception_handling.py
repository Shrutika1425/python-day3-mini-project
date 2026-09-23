# ex:1
try:
    print(a)
except:
    print("variable a is not defined")

else:
    print("nothing went wrong")

finally:
    print("try / except executed")

print("welcome to python")



#ex:2
try:
    print(10 / 0)
except:
    print("cannot divide by zero")
else:
    print("nothing went wrong")
finally:
    print("try / except executed")

print("welcome to python")



#ex:3
try:
    num = int("abc")
    print(num)
except:
    print("invalid number conversion")
else:
    print("nothing went wrong")
finally:
    print("try / except executed")



#ex:4
try:
    a = 10
    print(a)
except:
    print("variable a is not defined")
else:
    print("nothing went wrong")
finally:
    print("try / except executed")

print("welcome to python")


