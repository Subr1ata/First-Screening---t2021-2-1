class Calculator:
    def __init__(self,number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2
        
    def add(self):
        return eval('self.number_1 + self.number_2')
        
    def subtract(self):
        return eval('self.number_1 - self.number_2')
    
    def multiply(self):
        return eval('self.number_1 * self.number_2')
    
    def divide(self):
        return eval('self.number_1 / self.number_2')
        
a = float(input())
b = float(input())
calc = Calculator(a,b)
result = calc.add()
print(result)

result = calc.subtract()
print(result)

result = calc.multiply()
print(result)

result = calc.divide()
print(result)