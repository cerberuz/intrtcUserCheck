import random

# List of Restricted Words
restricted_words = ['cannabis', 'abuse', 'crack', 'drunk']
# List of taken usernames
users = ['user123', 'christian', 'cerberuz', 'abel123', 'paytowin', 'Developer', 'admin', 'admin123', 'anderson']


# Generate random username based on user input
def suggest_usernames(name):
    if len(name) < 3:
        name += name
    number = '{:03d}'.format(random.randrange(1, 999))
    generated_username = (name + number)

    return generated_username


# Generate the list of suggested usernames and validate that are uniques
def generate_usernames_list(name):
    usernames_lists = []
    failed = 0

    for i in range(14):
        new_username = suggest_usernames(name)

        if find_username(new_username):
            if new_username not in usernames_lists:
                usernames_lists.append(new_username)
            else:
                failed += 1
    if failed:
        for i in range(failed):
            new_username = suggest_usernames(name)

            if find_username(new_username):
                if new_username not in usernames_lists:
                    usernames_lists.append(new_username)

    usernames_lists.sort()
    return usernames_lists


# check if the username is already taken (can be modified to change de data source)
def find_username(username):
    return not any(user == username for user in users)


# check if the username contain restricted words (can be modified to change de data source)
def check_restricted_words(username, restricted_words):
    return any(invalid_word in username for invalid_word in restricted_words)


# remove the restricted words from the user input to generate the suggestions
def clean_username(username, restricted_words):
    old_username = username
    for restricted_word in restricted_words:
        username = username.replace(restricted_word, '')

    if len(username) < 2:
        username = old_username[:3] * 2

    return username


# Main function to validate the username.
# Return a Dictionary with the keys: 'valid': bool and 'suggested_usernames': list of generated usernames
def check_username(username):
    if len(username) >= 6:

        validation = {'valid': find_username(username), 'suggested_usernames': []}

        if check_restricted_words(username, restricted_words):
            new_username = clean_username(username, restricted_words)
            validation['valid'] = False
            validation['suggested_usernames'] = generate_usernames_list(new_username)

            return validation
        elif validation['valid']:
            return validation
        else:
            validation['suggested_usernames'] = generate_usernames_list(username)

            return validation

    else:
        raise ValueError("The username should contain at least 6 characters")


username = input("insert a username: ").lower()
result = check_username(username)

print(result)
