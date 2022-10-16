class Conversion:
    def __init__(self):
        self.__stack = []
        self.__result = []
        self.__precedence = {'(':0, '+':1, '-':1, '*':2, '/':2, '^':3}

    def __isEmpty(self):
        return self.__stack == []


    def __push(self, ele):
        self.__stack.append(ele)

    def __top(self):
        if not self.__isEmpty():
            return self.__stack[len(self.__stack) - 1]
        # return '-1'

    def __pop(self):
        if not self.__isEmpty():
            return self.__stack.pop()
        # return '-1'

    def __notGreater(self, c):
        try:
            a = self.__precedence[self.__top()]
            b = self.__precedence[c]
            return True if a >= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for char in exp:
            if char.isalnum():
                self.__result.append(char)
            elif char == '(':
                self.__push(char)
            elif char == ')':
                x = self.__pop()
                while x != '(' and not self.__isEmpty():
                    self.__result.append(x)
                    x = self.__pop()
            else:
                while (not self.__isEmpty() and self.__notGreater(char)):
                    self.__result.append(self.__pop())
                self.__push(char)

        while not self.__isEmpty():
            self.__result.append(self.__pop())

        return "".join(self.__result)

    def infixToPrefix(self, expr):
        rev_expr_list = []
        for char in reversed(expr):
            if char == '(':
                rev_expr_list.append(')')
            elif char == ')':
                rev_expr_list.append('(')
            else:
                rev_expr_list.append(char)

        rev_expr = "".join(rev_expr_list)
        post_expr = self.infixToPostfix(rev_expr)
        return post_expr[::-1]


class Evaluation:
    def __init__(self):
        self.__stack = []

    def __isEmpty(self):
        return self.__stack == []

    def __push(self, ele):
        self.__stack.append(ele)

    def __pop(self):
        if not self.__isEmpty():
            return self.__stack.pop()

    def evaluatePostfix(self, expr):
        for char in expr:
            if char.isdigit():
                self.__push(char)
            else:
                a = self.__pop()
                b = self.__pop()
                self.__push(str(eval(a + char + b)))
        return int(self.__pop())

    def evaluatePrefix(self, expr):
        return self.evaluatePostfix(expr[::-1])

if __name__ == '__main__':
    exp = "(2*3+4*(5-6))"

    c1 = Conversion()
    result1 = c1.infixToPostfix(exp)
    print('Postfix:', result1)

    c2 = Conversion()
    result2 = c2.infixToPrefix(exp)
    print('Prefix:', result2)

    post = '234*6*+'
    e1 = Evaluation()
    result3 = e1.evaluatePostfix(post)
    print(result3)

    pre = '+2**346'
    e2 = Evaluation()
    result4 = e2.evaluatePrefix(pre)
    print(result4)