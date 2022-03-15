from random import choice

my_ticket = []
winning_numbers = []

def generate_numbers(empty_list):
    numbers = list(range(1, 10))
    alphabets = ['A', 'B', 'C', 'D', 'E']
    for i in range(1, 5):
        current_number = choice(numbers)
        empty_list.append(current_number)
        numbers.remove(current_number)
    # sorted(empty_list)
    empty_list.sort()
    empty_list.append(choice(alphabets))
        
    print(empty_list)
    return empty_list

ticket = generate_numbers(my_ticket)
print("\n")
draw = generate_numbers(winning_numbers)

count = 1

while ticket != draw:
    count += 1
    draw = []
    draw = generate_numbers(draw)
print(f"Winner after {count} draws.")    



























# while check is False:
#     check = all(num in my_numbers for num in live_draw)
#     count += 1
#     generate_numbers(winning_numbers)
#     print(f"\n{my_numbers}")
#     print(f"\n{live_draw}")

# check = True
# print(f"Winner, after {count} draws.")

# # count = 0

# if check is False:
#     count += 1
#     live_draw = generate_numbers(winning_numbers)
#     


