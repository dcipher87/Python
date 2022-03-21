from email.encoders import encode_noop
import encodings


file_name = "alice.txt"

# with open(file_name, encoding='utf-8') as f:
#     contents = f.read()

# try:
#     with open(file_name, encoding="utf-8") as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {file_name} does not exist.")

# else:
#     # Count the approximate number of words in the file
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {file_name} has about {num_words} words.")

# def count_words(file_name):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(file_name, encoding="utf-8") as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {file_name} doesn't exist.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {file_name} has about {num_words} words.")

# # file_name = "alice.txt"
# # count_words(file_name)

# file_names = ["alice.txt", "tom_sawyer", "little_women.txt", "moby_dick.txt", "black_beauty.txt", "siddhartha.txt"]

# for file_name in file_names:
#     count_words(file_name)

### Failing silently

def count_words(file_name):
    """Count the approximate number of words in a file."""
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has approximately {num_words} words in it.")

file_names = ["alice.txt", "great_gatsby.txt", "moby_dick.txt", "little_women.txt"]
for file in file_names:
    count_words(file)

