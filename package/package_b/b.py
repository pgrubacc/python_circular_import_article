print('First line of b.py')

from package.package_a.a import fun_a

print('Imported fun_a inside b.py')


def fun_b():
    print('Executing fun_b')
    fun_a()
    return 'b'


print('Last line of b.py')
