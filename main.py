def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

while True:
    expression = input("Enter expression: ")
    print(expression, '=', calculate(expression))


