def addition( a= 2,b=3):
    return a+b    
def divisionByTwo(additionValue=6):
    return additionValue/2
def multiplication(divisionValue=2,h=3):
    return divisionValue*h

if __name__=="__main__":
    additionValue=addition()
    divisionValue=divisionByTwo(additionValue)
    print("Area of trapeziod is ",multiplication(divisionValue,3))
