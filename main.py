import random

blacklist = ['cannabis', 'abuse', 'crack', 'drunk']
users = ['johana', 'christian', 'cerberuz', 'abel123', 'paytowin']


def suggest_usernames(name):
    if len(name) < 3:
        name += name

    number = '{:03d}'.format(random.randrange(1, 999))
    username = (name + number)
    print(username)

    return username


def find_username(username):
    if any(user == username for user in users):
        print('El usuario Ya existe')
        return True

    else:
        return False


def validate_username(username, blacklist):
    if any(invalid_word in username for invalid_word in blacklist):
        username = clean_username(username, blacklist)
        print('the user contains ivalid words')
        print(username)
    else:
        print('the user is a valid username')


def clean_username(username, blacklist):
    for invalid in blacklist:
        username = username.replace(invalid, '')

    return username


# Main function to validate username
def check_username(username):
    if len(username) >= 6:

        # print(username)
        if not find_username(username):
            validate_username(username, blacklist)
        else:

            suggest_usernames(username)


    else:
        raise ValueError("The username should contains at least 6 characters")


username = input("insert a username: ").lower()
result = check_username(username)
