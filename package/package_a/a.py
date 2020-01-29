print('First line of a.py')

from package.package_b.b import fun_b

print('Imported fun_b inside a.py')


def fun_a():
    print('Executing fun_a')
    fun_b()
    return 'a'


print('Last line of a.py')
