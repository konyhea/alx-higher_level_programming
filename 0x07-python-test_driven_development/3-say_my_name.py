#!/usr/bin/python3


"function that print your name"
def say_my_name(first_name, last_name=""):
    """
    it prints your first and last name
    
    arguments
    -----------
    first_name: str
    it takes your first name, it should be of string type else raise 
    TypeError
    last_name: str
    it takes your last name, it should be of string type else raise 
    TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
    return
