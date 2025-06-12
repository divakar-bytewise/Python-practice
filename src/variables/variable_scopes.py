x="Hello Everyone"
def global_var(x):
    x="Hiii"
    print("Using Global variable : " +x)
global_var(x)
print("Using global var outside the fun: " + x)