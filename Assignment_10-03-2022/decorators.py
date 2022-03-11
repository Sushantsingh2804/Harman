def smartDiv(func):
    def inner(a, b):
        if a<b:
            a, b = b, a
        return func(a, b)
    return inner

@smartDiv
def div(a,b):
    print(a//b)

div(3,6)