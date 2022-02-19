# print('  O ','|',' X ','|',' O ')
# print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
# print('  O ','|',' X ','|',' O ')
# print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
# print('  O ','|',' X ','|',' O ')

# field = ' {} | {} | {}'
# print(input.format('O','X','O'))


# field  = ' {} | {} | {}'
# print(field .format('O','X','O'))
# print('‾‾‾‾‾‾‾‾‾‾‾')
# field = ' {} | {} | {}'
# print(field.format('O','1','O'))
# print('‾‾‾‾‾‾‾‾‾‾‾')
# field = ' {} | {} | {}'
# print(field.format('O','X','O'))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

field = ' {} | {} | {}'
print(field.format(data[0], data[1], data[2]))
print('‾‾‾‾‾‾‾‾‾‾‾')
print(field.format(data[3], data[4], data[5]))
print('‾‾‾‾‾‾‾‾‾‾‾')
print(field.format(data[6], data[7], data[8]))

data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# x = int(input()) - 1
# data[x] = 'O'
# print(data[x])
# field = ' {} | {} | {}'
# print(field.format(data[0], data[1], data[2]))
# print('‾‾‾‾‾‾‾‾‾‾‾')
# print(field.format(data[3], data[4], data[5]))
# print('‾‾‾‾‾‾‾‾‾‾‾')
# print(field.format(data[6], data[7], data[8]))

mark = 'O'

for i in range(9):
    print('please enter number 1 to 9 where you want :')
    x = int(input()) - 1
    if data[x] == ' ':
        data[x] = mark
        field = ' {} | {} | {}'
        print(field.format(data[0], data[1], data[2]))
        print('‾‾‾‾‾‾‾‾‾‾‾')
        print(field.format(data[3], data[4], data[5]))
        print('‾‾‾‾‾‾‾‾‾‾‾')
        print(field.format(data[6], data[7], data[8]))

        if data[0] != ' ' and data[0] == data[1] == data[2]:
            print('player', mark, 'is winner!')
            break
        elif data[3] != ' ' and data[3] == data[4] == data[5]:
            print('player', mark, 'is winner!')
            break
        elif data[6] != ' ' and data[6] == data[7] == data[8]:
            print('player', mark, 'is winner!')
            break

        if data[0] != ' ' and data[0] == data[3] == data[6]:
            print('player', mark, 'is winner!')
            break
        elif data[1] != ' ' and data[1] == data[4] == data[7]:
            print('player', mark, 'is winner!')
            break
        elif data[2] != ' ' and data[2] == data[5] == data[8]:
            print('player', mark, 'is winner!')
            break

        if data[0] != ' ' and data[0] == data[4] == data[8]:
            print('player', mark, 'is winner!')
            break
        elif data[2] != ' ' and data[2] == data[4] == data[6]:
            print('player', mark, 'is winner!')
            break
        data_set = set(data)
        if ' ' not in data_set:
            print('no winner :( ')
            break

        if mark == 'O':
            mark = 'X'
        elif mark == 'X':
            mark = 'O'

print("game ended")


