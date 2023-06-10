import re



class calculator:
    numerical = int | float

    @staticmethod
    def add(x: numerical, y : numerical) -> numerical:
        return x + y

    @staticmethod
    def subtract(x: numerical, y: numerical) -> numerical:
        return x - y

    @staticmethod
    def multiply(x: numerical, y: numerical) -> numerical:
        return x * y

    @staticmethod
    def devide(x: numerical, y: numerical) -> numerical:
        if y == 0:
            raise ValueError("divider cannot be equal to 0")
        return x / y


    expr_regex = r'^([-]?\d+(\.\d+)?)\s*([+\-*/])\s*([-]?\d+(\.\d+)?)$'
    operations = {
        '+': add.__get__(object),
        '-': subtract.__get__(object),
        '*': multiply.__get__(object),
        '/': devide.__get__(object)
    }


    @staticmethod
    def parse_num(number_str: str) -> numerical:
        sign = -1 if number_str[0] == '-' else 1
        if sign == -1:
            number_str = number_str[1:]

        if number_str.isdigit():
            return sign * int(number_str)
        return sign * float(number_str)

    @staticmethod
    def parse_expr(expression: str) -> numerical | None:
        match = re.match(calculator.expr_regex, expression)
        if not match:
            return "Error: invalid expression!"

        x = match.group(1)
        op = match.group(3)
        y = match.group(4)

        try:
            result = calculator.operations[op](
                calculator.parse_num(x), 
                calculator.parse_num(y)
            )
            return result
        except ValueError as err:
            print(err)
            return None
