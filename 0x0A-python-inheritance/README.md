# Inheritance in Object-Oriented Programming

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows classes to inherit properties and behavior from other classes. This enables code reusability, promotes modularity, and simplifies the design and maintenance of software systems.

## How Inheritance Works

Inheritance establishes a parent-child relationship between classes, where the child class (subclass) inherits attributes and methods from the parent class (superclass). The subclass can then extend or override inherited behavior as needed.

### Syntax

In most object-oriented languages like Java, Python, and C++, the syntax for defining a subclass that inherits from a superclass is as follows:

```python
class ParentClass:
    # Parent class attributes and methods

class ChildClass(ParentClass):
    # Child class attributes and methods
