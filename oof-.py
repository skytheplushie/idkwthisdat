a = int(input('write first number please '))
b = int(input('write second number please '))
c = int(input('write third number please '))
if a == b and a == c and b == c:
    print('BINGO')
elif a == b or a == c or b ==c:
    print('gg')
else:
    print('eh...')
