def check(func):
    def inside(a,b):
        if b==0:
            print("Not accepted")
            return
        func(a,b)
    return inside

@check
def add1(a,b):
    print(a+b)

print(add1(10,0))
