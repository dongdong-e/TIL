def hello(func):
    print('hi hi')
    print(func())
    print('hi hi')

@hello
def bye(a=1, b=2):
    return a + b