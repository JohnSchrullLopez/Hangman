def GetInput(**kwargs):
    """Get user input from a list of options
    Parameters:
        message: (str): message to promote
        options: (list): all options allowed
    Returns:
        the player input"""
    
    message = kwargs["message"]
    options = kwargs["options"]

    userInput = input(f"{message}:\n{options}\n>>>")
    while userInput not in options:
        print("invalid input!")
        userInput = input(f"{message}:\n{options}\n>>>")

    return userInput

def GameRunner(GameToRun):
    def wrapper(): 
        while True:
            GameToRun()
            if GetInput(message = "\n\nDo you want to play again?", options = ["Y", "N"]) == "N":
                    return
    return wrapper