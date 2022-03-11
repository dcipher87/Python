# to_print = ["dodecahedron", "robot pendant", "phone case"]
# printed = []

# to_print.reverse()

# def print_models(models, printed):
#     """Prints models and confirms models printed"""
#     while to_print:
#         current_model = to_print.pop()
#         print(f"Printing: {current_model}")
#         printed.append(current_model)
    
#     print("\nThe following models have been printed: ")
#     for model in printed:
#         print(model.title())

# print_models(to_print, printed)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

#simulate printing each design and move each from unprinted to completed
def print_models(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def confirm_printed(completed): 
#display all completed models
    print("\nThe following models have been printed: ")
    for model in completed_models:
        print(model)

print(f"\n{unprinted_designs}\n")

print_models(unprinted_designs[:], completed_models)
confirm_printed(completed_models)

print(unprinted_designs)