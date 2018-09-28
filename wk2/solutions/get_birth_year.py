import datetime

def birth_year(age, has_had_birthday):
    current_year = datetime.date.today().year
    if has_had_birthday:
        return current_year - age
    else:
        return current_year - age - 1

ian_birth_year = birth_year(36, True)
jared_birth_year = birth_year(16, False)
print('Ian was born in ' + str(ian_birth_year))
print('Jared was born in ' + str(jared_birth_year))
