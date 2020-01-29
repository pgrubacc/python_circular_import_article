print('First line of a.py')

from package.package_b import b  # alternative way of writing import package.package_b.b

print('Imported fun_b inside a.py')


def fun_a():
    print('Executing fun_a')
    b.fun_b()
    return 'a'


print('Last line of a.py')
