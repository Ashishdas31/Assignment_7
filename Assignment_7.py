# Ans.  1.
def fun(x,y):
    Add=x+y
    Sub=x-y
    mul= x*y
    div= x/y
    print(f"""First variable is {x} & second variable is {y}
Addition: {x} + {y} = {Add}
Subtraction: {x} - {y} = {Sub}
Multiplication: {x} * {y} = {mul}
Division: {x} / {y} = {div}
""")

fun(100,50)

# Ans.  5.
list=[1,2,3,4,5,6,7,8,9,10]

element=0
for i in list:
    if i == 10:
        element="found"
        break

if element=="found":
    print("Element 10 is present")

else:
    print("Element 10 is not found")
