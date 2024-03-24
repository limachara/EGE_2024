def find_max_number(number, max_number):
    if number and number[0] != '0' and int(number, 19) % 2 == 0:
        if int(number, 19) > int(max_number, 19):
            return number
    return max_number

f = open('30.txt')
s = f.readline() + '*'
number = ''
max_number = '0'
for c in s:
    if c in '0123456789ABCDEFGHI':
        number += c
    else:
        max_number = find_max_number(number, max_number)
        number = ''

print(max_number)

#"если нечетная система счисления - сумма цифр четная"