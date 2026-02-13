def init_database(): 
    global Names,Ranks,Divs,Ids # Global variable used so the lists can be accesed from every function
    Names = ["Kirk", "Troi", "Mccoy", "Sulu", "Harry"]
    Ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    Divs = ["Command", "Councillor", "Medical", "Command", "Operations"]
    Ids = [0,1,2,3]
    return Names, Ranks, Divs, Ids

