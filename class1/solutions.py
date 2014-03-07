# Exercise Solutions

# 1.
x = 0
while x < 5:
    print('{}'.format(2 * x + 1))
    x += 1


# 2.
my_list = list()
while len(my_list) < 5:
    my_list.append(2 * len(my_list) + 1)


# 3.
name = 'rico'
if name == 'rico':
    print("That's my name, don't wear it out.")
else:
    print("That's someone else's name.")


# 4.
my_list = [1, 2, 3, 4]
largest_val = 0
for val in my_list:
    if val > largest_val:
        largest_val = val


# 5.
my_list = ['1', 'a', '2', 'b']
current_index = len(my_list) - 1
new_list = list()
while current_index >= 0:
    new_list.append(my_list[current_index])
    current_index -= 1


# 6.
name = 'rico'
tmp_list = list()
for letter in name:
    tmp_list.append(letter)

reverse_name = ''
current_index = len(tmp_list) - 1
while current_index >= 0:
    reverse_name += tmp_list[current_index]
    current_index -= 1


# 7.
my_str = 'ten_values'
new_str = ''
for index in range(2, 7):
    new_str += my_str[index]


# 8.
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2


# Advanced Exercise Solutions

# 9.
my_list = [1, 2, 3, 4]
largest_val = max(my_list)


# 10.
my_str = 'ten_values'
new_str = my_str[3:7]


# 11.
my_list = ['1', 'a', '2', 'b']
new_list = my_list[::-1]


# 12.
name = 'rico'
new_name = name[::-1]


# 13.
my_str = 'and'
my_list = [char for char in my_str]


# 14.
my_sentence = 'I like Python.'
my_list = my_sentence.split()


# 15.
my_list = ['a', 'n', 'd']
my_str = ''.join(my_list)
