def init_database(): 
    global Names,Ranks,Divs,Ids # Global variable used so the lists can be accesed from every function
    Names = ["Kirk", "Troi", "Mccoy", "Sulu", "Harry"]
    Ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    Divs = ["Command", "Councillor", "Medical", "Command", "Operations"]
    Ids = [0,1,2,3]
    return Names, Ranks, Divs, Ids

def display_menu():
    print("-=x=-=x=-=x=- MENU -=x=-=x=-=x=-")
    print("1) Add Members")
    print("2) Remove Members")
    print("3) Update Rank")
    print("4) Display Roster")
    print("5) Search Crew : 5")
    print("6) Filter By Division")
    print("7) Calculate Payroll")
    print("8) Count Officers")
    print("-=x=-=x=-=x=-=x=-=x==x=-=x=-=x=-=x=-=x=-")
    print(f"{Fname} is currently logged in")
    print("-=x=-=x=-=x=-=x=-=x==x=-=x=-=x=-=x=-=x=-")
    while True:
        try:
            choice = int(input("What option do you want to select >> "))
            if 0 <= choice <= 8:
                break
        except:
            continue
    return choice

def add_member():
    name = input("What is their name >> ")
    rank = input("What is their rank >> ")
    div = input("What is their division >> ")
    while True:
        try:
            id = int(input("What is their ID >> "))
            if id > 0:
                if id > Ids[-1]:
                    Ids.append(id)
                    Ranks.append(rank)
                    Names.append(name)
                    Divs.append(div)
                    break
                elif Ids[-2] < id < Ids[-1]:
                    Ids.append(id)
                    Ranks.append(rank)
                    Names.append(name)
                    Divs.append(div)
                    break
                else:
                    print("Invalid ID")
                    continue
        except:
            print("Invalid")
            continue

def remove_member():
    while True:
        try:
            id = int(input("What is the ID >> "))
            if id >= 0:
                break
            else:
                print("Invalid ID")
                continue
        except:
            print("ID's are a number")
            continue
    num = Ids.index(id)
    Names.pop(num)
    Ranks.pop(num)
    Divs.pop(num)
    Ids.pop(num)

def update_rank():
    while True:
        try:
            id = int(input("What is the ID >> "))
            if id >= 0:
                break
            else:
                continue
        except:
            print("ID's are a number")
            continue
    new_rank = input("What is the new rank >> ")
    Ranks[id] = new_rank


def main():
    global Fname
    Fname = input("What is your full name >> ")
    while True:
        init_database()
        opt = display_menu()
        if opt == 1:
            add_member()
        elif opt == 2:
            remove_member()
        elif opt == 3:
            update_rank()
        while True:
            change = str(input(f"Is {Fname} still logged in (y/n) >> "))
            if change == "y":
                Fname = Fname
                break
            elif change == "n":
                Fname = input("What is your full name >> ")
                break

main()
