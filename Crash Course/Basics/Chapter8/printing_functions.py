def print_models(unprinted, completed):
    """Simulate printing each design then move to completed list"""
    unprinted.reverse()
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)

def confirm_printed(completed): 
    """Displays all completed models"""
    print("\nThe following models have been printed: ")
    for model in completed:
        print(model.title())