# # class test:
# #     @staticmethod
# #     def display():  
# #         print("This is a static method")
# # test.display()
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def subtract(a, b):
#         return a - b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def divide(a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Cannot divide by zero"
#     @staticmethod
#     def power(a, b):
#         return a ** b

# print(MathUtils.add(10, 5))        # Output: 15
# print(MathUtils.subtract(10, 5))   # Output: 5
# print(MathUtils.multiply(10, 5))   # Output: 50
# print(MathUtils.divide(10, 5))     # Output: 2.0
# print(MathUtils.divide(10, 0))     # Output: Cannot divide by zero
# print(MathUtils.power(2, 3))      # Output: 8
class test:
    #class level variable
    company_name = "Tech Solutions"
    
    #constructor 
    def __init__(self, name):
        self.name = name  #instance variable
    #instance method
    def test1(self):
        print(self.name)

    #class method
    @classmethod
    def chg_company_name(cls, new_company_name):
        cls.company_name = new_company_name
    #static method
    @staticmethod
    def is_major(age):
        return age >= 18
#creating an object of the class
obj = test("EMP001")
#accessing instance method
obj.test1()  # Output: EMP001
#accessing class method
test.chg_company_name("New Tech Solutions")
print(test.company_name)  # Output: New Tech Solutions
#accessing static method
print(test.is_major(20))  # Output: True
print(test.is_major(16))  # Output: False
