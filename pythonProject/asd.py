# print(str((lambda a, b: a + b)(2, 8)))

def d(f):
    return f*f

a= map(d,[2,3,6])

print(list(a))
