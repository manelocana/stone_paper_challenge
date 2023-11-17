
"""
  - hacemos que el jugador eliga, 
  - luego elige la maquina (con modulo random), 
  - hacemos la logica (que gana a que, opcion no valida, ) 
  - comparamos resultado jugador vs maquina, 
  - printamos resultado, 
  - lo metemos todo en un bucle,
  - y que pregunte si quiere volver a jugar al final de cada partida
  """


import random


options = ["stone", "paper", "scissors"]

def pj_selection():
    while True:
        pj = input(str("Choose an option: stone, paper, scissors \n").lower())
    
        if pj in options:
            return pj
    
        else:
            print("This option is not correct ")



def machine_selection():
    machine = random.choice(["stone", "paper", "scissors"])
    
    return machine



def winner(pj_selection, machine_selection):
    if pj_selection == machine_selection:
        print("This is draw!, play again")

    elif (pj_selection == "stone" and machine_selection == "scissors") or\
        (pj_selection == "paper" and machine_selection == "stone") or\
        (pj_selection == "scissors" and machine_selection == "paper"):
        return "You win! "
    
    else:
        return "You lose :(   \nPlay again"



def game():
    print("Hi, welcome to mini-game stone-paper")

    while True:
        pj = pj_selection()
        machine = machine_selection()

        print(f"\nYour choice is: {pj}")
        print(f"Computer choice:  {machine}")

        result = winner(pj, machine)
        print(f"\n{result}!\n")

        play_again = input("Play again? (Yes/No): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    game()
