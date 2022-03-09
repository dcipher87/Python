# Dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    'shawking': {
        'first': 'stephen',
        'last': 'hawking',
        'location': 'harvard',
        },
}
# for user, info in users.items():
#     print(f"\nUsername: {user}")
#     print(f"\tFull name: {info['first'].title()} {info['last'].title()}")
#     print(f"\tLocation: {info['location'].title()}")

# using variables
for user, info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    location = f"{info['location'].title()}"
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")