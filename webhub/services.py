

def gender_is_valid(gender):
    valid = True
    gender = gender.lower()
    if gender != 'male' and gender != 'female':
        valid = False
    return valid


def phone_is_valid(phone):
    valid = True
    #Phone number can be formatted to be longer, hence length of 9-25
    if len(phone) > 25 or len(phone) < 9:
        valid = False
    #Check valid characters
    for char in phone:
        if char != ' ' and char != '-' and char != '+' and not ('0' <= char and char <= '9'):
            valid = False
    return valid


def email_is_valid(email):
    valid = True
    if len(email) > 80:
        valid = False
    if '@' not in email or '.' not in email:
        valid = False
    return valid


def location_is_valid(location):
    valid = True
    if len(location) > 50:
        valid = False
    return valid


def name_is_valid(name):
    valid = True
    if len(name) > 30:
        valid = False
    return valid



