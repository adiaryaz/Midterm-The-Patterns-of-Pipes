n = int(input())
expression = ""
if n <= 0:
    print("NoPattern")
else: 
    for i in range(1, n + 1):
        expression += "|>"
        print(expression)