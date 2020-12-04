# data structures

# lists are mutable, sets do not have duplicates, tuples are immutable
names = ["sakura", "naruto", "sasuke"]
names.sort()
numbers = set()

# dictionary is key-value pairs: dict[key] = value
initialising = {
    "new key": "new value"
}

# functions 
def square(i):
    return (i*i)

def get_name():
    # inputs and printing using print(f) 
    name = str(input("Name: "))
    print(f"Hello, {name}")
    return name


