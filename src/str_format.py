# C-style string format
print('Hello, %s!' % ('caiman',))
print('%s + %s = love!' % ('caiman', 'python'))
print('Hello, %(username)s!' % {'username': 'caiman'})

print('Hello, {}'.format('caiman'))
print('{} + {} = {}'.format(2, 2, 2+2))
print('{0} + {0} = {1}'.format(2, 2+2))
print('{male} + {female} = love'.format(male='John', female='Jane'))


params = {'male': 'Jack', 'female': 'Jane'}
print('{male} + {female} = love'.format(**params))

male = 'Bob'
female = 'Alice'

print(f'{male} + {female} = love')
print(f'2 + 2 = {2+2}')
