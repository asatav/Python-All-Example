#User defined within labda
def A(x):
    return (lambda y:x+y)
t=A(4)
print(t(8))