um1 = float(input("Ievadi pirmo skaitli: "))
op = input("Operācija (+, -, *, /): ")
num2 = float(input("Ievadi otro skaitli: "))

if op == '+':
    print("Rezultāts:", num1 + num2)
elif op == '-':
    print("Rezultāts:", num1 - num2)
elif op == '*':
    print("Rezultāts:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Rezultāts:", num1 / num2)
    else:
        print("Kļūda: dalīšana ar nulli!")
else:
    print("Nezināma operācija")