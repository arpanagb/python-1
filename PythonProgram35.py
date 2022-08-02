# Python Program to Check If a String Is a Number (Float)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('a2'))
print(isfloat('1.0'))