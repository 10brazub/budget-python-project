import time 

def main_menu():
    print()
    time.sleep(1)
    print("What would you like to do?")
    print("1. Create a new budget(s)")
    print("2. View existing budget(s)")
    print()
    while True:
        try:
            user_choice = str(input("Enter 1 or 2 for your option\n"))
            if(user_choice != "1" and user_choice != "2"):
                raise IOError("Oops something went wrong. Please try again.\n")
            return user_choice

        except IOError as err:
            print(err)

def create_budget():
    budget_name = str(input("What do you want to call this budget?\n"))
    print()
    time.sleep(1)
    print("Your budget will be called {}\n".format(budget_name))

    cont = True
    while cont == True:
        try:
            time.sleep(1)
            change_budget_name = str(input("Do you want to change the name? [Y/N]\n")).lower()
            if change_budget_name != "y" and change_budget_name != "n":
                raise IOError("Hmmm it seems like there was a mistake. Please try again.\n")

            elif change_budget_name == "y":
                budget_name = str(input("What do you want to rename this budget?\n"))
                print("Your budget will be called {}\n".format(budget_name))

            else:
                cont = False

        except IOError as err:
            print(err)

    print()
    return budget_name

def set_budget_details(budget_name):
    cont = True
    while cont == True:
        try:
            max_amount = float(input("How much will be allocated to the {} budget?\n$".format(budget_name)))
            print()
            cont = False
        except ValueError:
            print()
            print("We didn't quite get that. Please try again.\n")

    while cont == False:
        try:
            current_amount = float(input("How much has been spent towards the {} budget?\n$".format(budget_name)))
            print()
            cont = True

        except ValueError:
            print()
            print("We didn't quite get that. Please try again.\n")
    
    return max_amount, current_amount

def view_budget():
    time.sleep(1)
    for budget_name in budget_dict.keys():
                print(f"Budget Name: {budget_name}\n")
    while True:
        try:
            time.sleep(1)
            chosen_budget_name = str(input("What budget would you like to view ?\n"))
            if chosen_budget_name not in budget_dict:
                raise NameError("It seems like that budget doesn't exist.\n")
            else:
                break

        except NameError as err:
            print(err)

    print()
    print("Locating existing budget...\n")
    time.sleep(1)
    print("You are now viewing the {} budget.\n".format(chosen_budget_name))
    print("Total Spent: $", budget_dict[chosen_budget_name][1])
    print("Total Allocated: $", budget_dict[chosen_budget_name][0])
    print()



if __name__ == "__main__":

    user = str(input("Enter your name\n"))
    print()
    print("Welcome {}".format(user))
    budget_dict = {}

    replay = True
    while replay == True:
        choice = main_menu()

        if choice == "1":
            print()
            print("Creating a new budget...")
            time.sleep(2)
            budget = create_budget()
            max_toSpend, curr_spent = set_budget_details(budget)
            budget_dict[budget] = (max_toSpend, curr_spent)
        
        elif choice == "2":
            print()
            if budget_dict:
                view_budget()

            else:
                print("It seems like you haven't created any budgets.\n")
                pass
        
        while True:
            try:
                replay = str(input("Do you want to continue?[Y/N]\n")).lower()
                if replay != "y" and replay != "n":
                    raise ValueError("Something went wrong ... Please try again.")

                elif replay == "n":
                    replay = False
                    break

                else:
                    replay = True
                    break

            except ValueError as err:
                print(err)
