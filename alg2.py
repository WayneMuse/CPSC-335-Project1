'''
input_string = input('Enter elements of a list separated by space \n')
user_list = input_string.split()
print('string list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    if user_list[i] != ',':
        user_list[i] = int(user_list[i])

print('User list: ', user_list)
# Calculating the sum of list elements
print("Sum = ", sum(user_list))
'''