### Lottery game

#1. By ticket: my_ticket()          generates my numbers
#2. Play lotto: play_lotto()        generates numbers to check
#3. Check if we won: check_lotto()  compares lists, replay until we win and give a count.

# # List1
# List1 = ['python' ,  'javascript', 'csharp', 'go', 'c', 'c++']
 
# # List2
# List2 = ['csharp1' , 'go', 'python']

# check =  all(item in List1 for item in List2)
 
# if check is True:
#     print("The list {} contains all elements of the list {}".format(List1, List2))    
# else :
#     print("No, List1 doesn't have all elements of the List2.")

# from random import choice

# number_pool = list(range(1,11))
# alphabet = ['A', 'B', 'C', 'D', 'E']

# #1. buy my ticket
# def buy_ticket(numbers, letters):
#     """Randomly generates lotto ticket 4 ints and a char."""
#     my_ticket = []

#     for i in range(1,5):
#         my_number = choice(numbers)
#         my_ticket.append(my_number)
#         numbers.remove(my_number)
#     my_ticket.append(choice(letters))
    
#     print(my_ticket)
#     return my_ticket

# my_ticket = buy_ticket(number_pool, alphabet)

# def check_lotto(ticket):
#     """Counts how many draws are required for me to win."""
#     #Generate lotto numbers (live lotto draw)
#     number_pool = list(range(1,11))
#     alphabet = ['A', 'B', 'C', 'D', 'E']
#     live_lotto = []
#     count = 0
    
#     check = all(num in ticket for num in live_lotto)
    
# check_lotto(my_ticket[:])
my_numbers = [1,2,3,4,5,'A']
live_draw = [5,4,'A',3,2,1]

live_draw = sorted(live_draw)

check = my_numbers == live_draw

#ll(num in my_numbers for num in live_draw)
print(check)