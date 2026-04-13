# # # # # # # # # # # # def function1():
# # # # # # # # # # # #     print("This is function 1")
# # # # # # # # # # # # function1()
# # # # # # # # # # # def add(a, b):
# # # # # # # # # # #     result = a + b
# # # # # # # # # # #     print("The sum is:", result)
# # # # # # # # # # # add(10, 20)
# # # # # # # # # # def sutraction():
# # # # # # # # # #     a = 20
# # # # # # # # # #     b = 10
# # # # # # # # # #     result = a - b
# # # # # # # # # #     print("The sutraction is:", result)
# # # # # # # # # # sutraction()
# # # # # # # # # def multiplication(a, b):
# # # # # # # # #     result = a * b
# # # # # # # # #     return result
# # # # # # # # # x=multiplication(10, 20)
# # # # # # # # # print(f"The multiplication is: {x}")
# # # # # # # # def division(a, b):
# # # # # # # #     if b != 0:
# # # # # # # #         result = a / b
# # # # # # # #         return result
# # # # # # # #     else:
# # # # # # # #         return "Error: Division by zero is not allowed."
# # # # # # # # final_result = division(10, 2)
# # # # # # # # print(f"The division is: {final_result}")
# # # # # # # def db_connection(username, password, db_name):
# # # # # # #     if db_name == "my_database" and username == "admin" and password == "password123":
# # # # # # #         return "Database Connection Established"
# # # # # # #     else:
# # # # # # #         return "Error: Invalid credentials or database name."
# # # # # # # connection_status = db_connection("admin", "password123", "my_database")
# # # # # # # print(connection_status)
# # # # # # #default arguments in function
# # # # # # def greet(name="Guest"):
# # # # # #     print(f"Hello, {name}!")
# # # # # # greet()  # Output: Hello, Guest!
# # # # # # greet("Alice")  # Output: Hello, Alice!
# # # # # # greet(100)  # Output: Hello, 100!

# # # # # def func_one(num1, num2):
# # # # #     print(num1, num2)
# # # # # func_one(num2=10, num1=20)

# # # # #data stored in tuple is immutable
# # # # # my_tuple = (1, 2, 3, 4, 5)
# # # # # print(my_tuple[0])  # Output: 1
# # # # # print(my_tuple[2])  # Output: 3 
# # # # # #Lamda function not have name and it is used for small operations and no return statement is used in lamda function
# # # # # check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# # # # # print(check_even_odd(10))  # Output: Even
# # # # # print(check_even_odd(15))  # Output: Odd

# # # # # addition = lambda a, b: a + b
# # # # # print(addition(5, 3))  # Output: 8
# # # # # #map function is used to apply a function to all items in an iterable (like a list) and returns a map object (which is an iterator).
# # # # # numbers = [1, 2, 3, 4, 5]
# # # # # squared_numbers = map(lambda x: x ** 2, numbers)
# # # # # #print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# # # # #filter function is used to filter items in an iterable based on a function that returns True or False.
# # # # numbers = [1, 2, 3, 4, 5]
# # # # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# # # # print(even_numbers)  # Output: [2, 4]
# # # #pass one lamda function to another lamda function
# # # # add = lambda x, y: x + y
# # # # multiply = lambda a, b: a * b
# # # # result = add(5, 3)  # This will return 8
# # # # final_result = multiply(result, 2)  # This will return 16
# # # # print(final_result)  # Output: 16
# # # #sorted function is used to sort the items in a list or any iterable based on a key function.
# # # # numbers = [5, 2, 9, 1, 5, 6]
# # # # sorted_numbers = sorted(numbers)  # Sort in ascending order
# # # # print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
# # # # sorted_numbers_desc = sorted(numbers, reverse=True)  # Sort in descending order
# # # # print(sorted_numbers_desc)  # Output: [9, 6, 5, 5, 2, 1]
# # # # #sorting based on key function
# # # # words = ["apple", "banana", "cherry", "date"]
# # # # sorted_words = sorted(words, key=len)  # Sort by length
# # # # print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']
# # # # sorted_words_alpha = sorted(words)  # Sort alphabetically
# # # # print(sorted_words_alpha)  # Output: ['apple', 'banana', 'cherry', 'date']
# # # #Define a list of tuples containing student names and their scores, and sort the list based on scores in descending order.
# # # # students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 90)]
# # # # sorted_students = sorted(students, key=lambda x: x[1], reverse=True)  # Sort by scores in descending order
# # # # print(sorted_students)  # Output: [('Bob', 92), ('David', 90), ('Alice', 85), ('Charlie', 78)]

# # # #dictionary is not sorted but we can sort the dictionary based on key or value using sorted function
# # # data = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
# # # sorted_data= sorted(data.items(), key=lambda x: x[1],)  # Sort by values in descending order
# # # print(sorted_data)  # Output: [('Bob', 92), ('David', 90), ('Alice', 85), ('Charlie', 78)]
# # nums = [5, 2, 9, 1, 5, 6]
# # max_value = max(nums, key=lambda x: x)  # Output: 9
# # print(max_value)

# # result = lambda x: "High" if x > 90 else ("Medium" if x > 80 else "Low")
# # print(result(95))  # Output: High

# def student(**data):
#     print(data)
# student(name="Alice", age=20, grade="A")


















