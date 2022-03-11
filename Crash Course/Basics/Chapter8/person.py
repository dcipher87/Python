# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

def build_person(first_name, last_name, age=None):
    """Returns dictionary of information about a person"""
    person = {'fist': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'henxrix', 27)
print(musician)

musician = build_person('beyonce', 'knowels')
print(musician)