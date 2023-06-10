from calculator import calculator



def main():
    while True:
        expression = input('expr> ')
        if expression == "exit":
            raise SystemExit
        
        result = calculator.parse_expr(expression)
        if result: print(result)


if __name__ == "__main__":
    main()