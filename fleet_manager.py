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


def main():
    global Fname
    Fname = input("What is your full name >> ")
    while True:
        init_database()
        break

main()