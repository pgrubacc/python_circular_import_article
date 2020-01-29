print('First line of a.py')

print('Imported fun_b inside a.py')

from package.package_b.b import fun_b


def fun_a():
    print('Executing fun_a')
    fun_b()
    return 'a'


print('Last line of a.py')
