print('First line of b.py')

from package.package_a import a  # alternative way of writing import package.package_a.a

print('Imported fun_a inside b.py')


def fun_b():
    print('Executing fun_b')
    return 'b'


def fun_calling_fun_a():
    print('Executing fun_a from b.py')
    a.fun_a()


print('Last line of b.py')
