print('First line of b.py')

from package.package_a.a import fun_a

print('Imported fun_a inside b.py')


def fun_b():
    print('Executing fun_b')
    return 'b'


fun_a()
print('Last line of b.py')
