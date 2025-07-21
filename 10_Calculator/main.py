#Calculator
import art
#Add
def add(n1,n2):
  return n1+n2

#Subtract
def sub(n1,n2):
  return n1-n2

#Multiply
def mul(n1,n2):
  return n1*n2

#Divide
def div(n1,n2):
  return n1/n2
  
operations={"+":add, "-" : sub, "*" : mul, "/" : div}

def calculator():
  print(art.logo)
  should_accumulate=True
  num1=float(input("Enter the first number: "))
  
  while should_accumulate:
    for symbol in operations:
      print(symbol)
    operation_symbol=input("Pick an operation")
    num2=float(input("Enter the second number: "))
    answer=operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
    
    if choice=="y":
      num1=answer
    else:
      should_accumulate=False
      print("/n" * 20)
      calculator()

calculator()