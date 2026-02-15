def init_database(): 
    global Names,Ranks,Divs,Ids # Global variable used so the lists can be accesed from every function
    Names = ["Kirk", "Troi", "Mccoy", "Sulu", "Harry"]
    Ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    Divs = ["Command", "Councillor", "Medical", "Command", "Operations"]
    Ids = [0,1,2,3,4] # I am silly and forgot to add 5 IDs
    return Names, Ranks, Divs, Ids

def display_menu():
    print("-=x=-=x=-=x=- MENU -=x=-=x=-=x=-")
    print("1) Add Members")
    print("2) Remove Members")
    print("3) Update Rank")
    print("4) Display Roster")
    print("5) Search Crew")
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
    div = input("What is their division >> ")
    while True:
        try:
            id = int(input("What is their ID >> "))
            if id < 0:
                print("Invalid ID. Must be positive")
                continue
            if id in Ids:
                print("Invalid ID. ID alredy in use") # Fixed the ID check as i realised the the logic would'nt work as the IDs are not sorted in order so would break
                continue
            while True:
                ValidRanks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
                try:
                    rank = str(input("What is their rank >> "))
                    if rank not in ValidRanks:
                        print("Not a valid rank")
                        continue
                    Ids.append(id) # Also added the rank check with the same logic 
                    Ranks.append(rank)
                    Names.append(name)
                    Divs.append(div)
                    break
                except:
                    print("Must be a rank")
                    continue
            break
        except:
            print("Invalid. IDs must be a number")
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
    try:
        print(f"{Names[id]} was removed") # Couldnt really tell what happens when yoy remove someone so added this
        num = Ids.index(id)
        Names.pop(num)
        Ranks.pop(num)
        Divs.pop(num)
        Ids.pop(num)
    except: 
        print("No assigned ID")

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

def display_roster():
    for i in range(len(Names)):
        print(f"{i+1} : {Names[i]} | {Ranks[i]} | {Divs[i]} | {Ids[i]}")

def search_crew():
    search = input("What name do you want to search for >> ")
    people = 0
    for i in range(len(Names)):
        if search in Names[i]:
            print(Names[i])
            people += 1
    if people == 0:
        print(f"No names found") # Added this same count so it tells you if no one is found

def filter_by_division():
    filter = input("What division do you want to filter for (Command, Operations, Sciences, Councillor or Medical)>> ")
    filtered = 0
    for i in range(len(Divs)):
        if filter == Divs[i]:
            print(f"{Names[i]} | {Ranks[i]}")
            filtered += 1
    if filtered == 0:
        print(f"No people found in {filter} division")

def calculate_payroll():
    payroll = 0
    for i in range(len(Ranks)):
        if Ranks[i] == "Captain":
            payroll += 1000
        elif Ranks[i] == "Commander":
            payroll += 800
        elif Ranks[i] == "Lieutenant Commander":
            payroll += 600
        elif Ranks[i] == "Lieutenant":
            payroll += 400
        elif Ranks[i] == "Ensign":
            payroll += 200
        else:
            payroll = payroll
    print(f"Crew cost : ${payroll}")
        
def main():
    global Fname
    Fname = input("What is your full name >> ")
    init_database() # Have to move before because the lists are being reset if not
    while True:
        opt = display_menu()
        if opt == 1:
            add_member()
        elif opt == 2:
            remove_member()
        elif opt == 3:
            update_rank()
        elif opt == 4:
            display_roster()
        elif opt == 5:
            search_crew()
        elif opt == 6:
            filter_by_division()
        elif opt == 7:
            calculate_payroll()
        while True:
            change = str(input(f"Is {Fname} still logged in (y/n) >> "))
            if change == "y":
                Fname = Fname
                break
            elif change == "n":
                Fname = input("What is your full name >> ")
                break

main()
