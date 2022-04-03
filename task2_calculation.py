import calculator as calc


a = float(input("Please provide a number for a: "))
b = float(input("Please provide a number for b: "))


print(calc.add(a, b))
print(calc.substract(a, b))
print(calc.multiplication(a, b))
print(calc.division(a, b))
print()
print()
print(calc.result(a, b))