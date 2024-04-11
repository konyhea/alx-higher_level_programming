# Python Class and Object Readme

## Introduction
In Python, everything is an object, including functions, classes, and data types. This means that you can use object-oriented programming (OOP) principles to create and manipulate data structures efficiently. This README will cover the basics of classes in Python, highlighting object-oriented concepts like data abstraction, encapsulation, file hiding, and the use of getters and setters.

## Classes in Python
A class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) that objects of that class will have. Here's a basic example of a Python class:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}")


```
## Data Abstraction

Data abstraction is the concept of hiding the implementation details and showing only the necessary features of an object. In Python, you can achieve data abstraction by using methods to manipulate object data, rather than directly accessing attributes. This allows you to control how data is accessed and modified.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self._balance
```
In this example, the balance attribute is prefixed with an underscore (_), indicating that it's intended to be private. Methods like deposit and withdraw provide controlled access to the balance attribute, maintaining data abstraction.

## Data Encapsulation
Data encapsulation is the bundling of data and methods that operate on the data within a single unit (a class). In Python, you can enforce encapsulation by using private attributes and methods. Access to these members is restricted to within the class itself.

```python
Copy code
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def get_name(self):
        return self._name
    
    def set_salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("Invalid salary")
    
    def get_salary(self):
        return self._salary
```

Here, name and salary attributes are private (prefixed with _), and getter and setter methods (get_name, set_salary, get_salary) are used to access and modify them, ensuring encapsulation.

## Getter and Setter Methods
Getter and setter methods are used to retrieve and modify the values of private attributes, respectively. They provide controlled access to class attributes, allowing validation and modification logic to be applied.

``` python
Copy code
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print("Radius must be positive")

```

In this example, get_radius returns the value of the radius attribute, while set_radius allows modifying the radius, with validation to ensure it's a positive value.

## Conclusion
Understanding classes and objects in Python is essential for building robust and maintainable code. By leveraging object-oriented principles like data abstraction, encapsulation, and getter/setter methods, you can create clean, modular, and reusable code. Remember that everything in Python is an object, and object-oriented programming is a powerful paradigm for structuring your programs effectively.