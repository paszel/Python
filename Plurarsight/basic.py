def add_numbers(a:int, b:int) -> int:
    return a + b

print(add_numbers(5,13))
print("Don't worry about conversions!")
print(add_numbers(123,10.5))
print('Casting')

pi = 3.14159
c = 15

print(int(pi))
print(float(c))

print('hello {0}-{1}'.capitalize().format('Jhon','Thomas'))
print('hello'.replace('e','a'))
print('some, strings, to, table'.split(','))

if not pi > c or pi == c:
    print('Simple if')
else:
    print('Simple else')

a = 1
b = 2
print('bigger' if a>b else 'smaller')

students_names = ['Mark','Jhon','Elena']
students_names[2]==students_names[-1] #Elena
students_names.append('Homer')

'Homer' in students_names #true
del students_names[2]
students_names[1:] #skip first element Dont

x=0
print('Initial value of x: {0}'.format(x))
for index in range(5,10,2):
    x+=index
    print(index)

print('End value of x: {0}'.format(x))