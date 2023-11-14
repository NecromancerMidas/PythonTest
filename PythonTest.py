x = str("Hello, World!") #No need to declare variables, use typehints. @line 9
y,z = int(5), str("World!")
X,Y,Z = x,y,z
print(x)
print (y,z)
print (type(x), type(y), type(z))
print (X,Y,Z)
print (float(Y))
Typehint:str = x #Typehint Example *ref line 1
Typehint2:str = str(y) + " " + z
print(Typehint, Typehint2)
for char in Typehint2 : 
    print(char)
for char in Typehint :
    print (char)
print(char)
def myfunc() :
    x:str = "myfuncstuff"
    print(x)
myfunc()
print (x)
def myfunc2() :
    for char in X :
        print(char + " " + str(X.index(char)))
myfunc2()
