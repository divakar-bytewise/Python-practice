def first_intro(func):
    def wrapper(*args,**kwargs):
        print("Heyy! Dominic.")
        func(*args,**kwargs)
    return wrapper

def intracting(func):
    def wrapper(*args,**kwargs):
        print("How are you!")
        func(*args,**kwargs)
    return wrapper


@first_intro
@intracting
def greet(name):
    print(f"Hello!! {name}.")

greet('John')