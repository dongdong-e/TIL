# String Interpolation
a = '123'
new_q = f'{a}'

# 1. 옛날 방식
f'%s %s' % ('one', 'two') # => 'one two'

# 2. pyformat
'{} {}'.format('one', 'two') # => 'one two'

# 3. f-string
a, b = 'one', 'two'
f'{a} {b}' # => 'one two'

# Example
name = '홍길동'
eng_name = 'Hong Gil dong'

print('안녕하세요, {1}입니다. My name is {0}'.format(name, eng_name))
print(f'안녕하세요, {name}입니다.')