# write your code here
import random
names = {}
print('Enter the number of friends joining (including you): ')
num_of_friends = int(input())
if num_of_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line: ')
    for i in range(num_of_friends):
        enter_name = input()
        names[enter_name] = 0
    print('Enter the total bill value: ')
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    lucky_string = input()
    if lucky_string == 'Yes':
        winner = random.choice([k for k in names])
        print(f'{winner} is the lucky one!')
        share_bill = round((bill / (num_of_friends - 1)), 2)
        for name in names:
            if winner == name:
                names[name] = 0
            else:
                names[name] = share_bill
    elif lucky_string == 'No':
        print('No one is going to be lucky')
        share_bill = round((bill / num_of_friends), 2)
        for name in names:
            names[name] = share_bill
    print(names)
