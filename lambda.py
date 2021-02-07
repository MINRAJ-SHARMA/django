#A lambda function is a small anonymous function
hellofunction=lambda a: a+10
print(hellofunction(5))
#multiply
function1=lambda a,b: a*b
print(function1(5,6))
#
fun2=lambda c,d,e: c+d+e
print(fun2(3,5,7))
#example
def aryalfunction(a):
     return lambda c: a*c
aryal=aryalfunction(4)
print(aryal(5))

