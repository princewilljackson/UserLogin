user = input("Enter username: ")
user_names = ['admin', 'elnino', 'emma', 'kalu', 'kanex']
for name in user_names:
    if user == user_names[0]:
        print("Hello {}, would you like a status report?".format(user_names[0]))
        break
    elif user in name:
        print("Hello {}, welcome back!".format(name))
    elif user not in user_names:
        prompt = input("Would you like to be part of the list?\n y/n: ")
        if prompt == 'y':
            user_names.append(user)
            print(user_names)
        else:
            print("Thanks for your patronage!")
            break
