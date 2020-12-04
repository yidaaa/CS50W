def announce(f):
    # able to take in a function, add decorators increase capability of function
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()