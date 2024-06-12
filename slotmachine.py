import random

rows = 3
cols = 3


symbol_count = {"A" : 2 ,"B" : 4,"C" : 6}
symbol_value= {"A" : 5 , "B" : 4 , "C" : 3}

MAX_LINES = 3
MAX_BET= 100
MIN_BET = 1
flagVal = 0


print("=====================================================================================")
print("WELCOME TO THE GRAND CASINO!!")
print("=====================================================================================")
print("""--INSTRUCTIONS--

1) YOU WILL GET PROMPT TO DEPOSIT MONEY,
NUMBER OF LINES YOU WANT TO BET ON ,
AND THE AMOUNT OF MONEY YOU BET ON EACH LINE.
2) THE SPIN WILL HAPPEN AUTOMATICALLY AND YOU WILL SEE A GRID OF LETTERS WHERE
A IS THE BEST LETTER AND IT HAS A MULTIPLIER OF 5 I.E MULTIPLIES BET BY 5
B MULTIPLIES BET BY 4
C MULTIPLIES BET BY 3

3) CONDITION OF WINNING IS TO GET ALL THE SAME LETTERS IN A SINGLE LINE.
4) IF YOU WIN, THE BET WILL GET MULTIPLIED AND BE ADDED TO YOUR CURRENT BALANCE.
5) YOU CAN BET ON UPTO 3 LINES, AND UPTO $100 ON EACH LINE.
==================================================================================== \n \n """)

def slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    coloumns = []
    for _ in range(cols):
        coloumn = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)

        coloumns.append(coloumn)

    return coloumns

def print_slot_machine(coloumns):
    for row in coloumns :
        for i,symbol in enumerate(row):
            if i !=  row[-1]:
                print(symbol, end = " | ")
            else:
                print(symbol , end= " ")
        print()
    print("=====================================================================================")

def win_or_loose(coloumns, lines, bet, values, balance):
    winnings = 0
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                print(f"You lost on line {line + 1}!!")
                break
        else:
            print(f"You WON on line {line +1 }!! ")
            winnings += values[symbol]*bet

    if winnings != 0 :
        print(f"""Congratulations! you have won ${winnings}
this brings your balance to {balance + winnings}""")
        print("=====================================================================================")
        return winnings
    else:
        print("=====================================================================================")
        print(f"Your remaining balance is {balance + winnings}")
        return winnings
    return winnings

def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0!")
        else:
            print("please enter a number!")
    return amount

def get_number_of_lines():
    while True:
         lines= input("number of lines you want to bet on (1- " + str(MAX_LINES)+ ")? :")
         if lines.isdigit():
             lines = int(lines)
             if 1<= lines <= MAX_LINES :
                 break
             else:
                 print("Enter a valid number of lines!")
         else:
              print("please enter a number!")
    return lines

def get_bet():
        while True:
            bet = input("What would you like to bet on each line? $ ")
            if bet.isdigit():
                bet = int(bet)
                if MIN_BET<= bet<= MAX_BET :
                    break
                else:
                    print(f"bet must be between ${MIN_BET} and ${MAX_BET}")
            else:
                print("please enter a number!")
        return bet


money = deposit()


def main(money, flagVal):

    print("=====================================================================================")

    lines = get_number_of_lines()
    bet = get_bet()
    balance = money - (lines * bet)
    while True:

        if balance<0 :
            print("You don't have enough money!")
            print(f"You are missing ${abs(balance)}")
            print("=====================================================================================")
            ch = input("""how would you like to proceed?
            1. Add remaining money
            2. Change bet
            3. End game
            (Enter 1/2/3 for your choice : """)
            if ch == "1":
                AddDep = deposit()
                money += AddDep
                main(money, flagVal)
                return
            elif ch == "2":
                main(money, flagVal)
                return
            elif ch == "3":
                print(" THANKYOU!!")
                print("=====================================================================================")
                flagVal+= 1
                return
            else:
                print("INVALID CHOICE!")
                continue




        else:
            print("=====================================================================================")
            print(f"you have bet ${bet} on each of the {lines} lines and your total bet comes out to be ${bet*lines}")
            print( f"you have ${balance} left to play" )
            print("=====================================================================================")
            break
    slots = slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    balance += win_or_loose(slots, lines, bet, symbol_value, balance)


    while True:
        ch2 = input("""how do you want to proceed?
        1. Keep playing
        2. Quit game
        Please input 1/2 for your choice : """)
        if ch2 == "1":
            main(balance, flagVal)
        elif ch2 == "2":
            print("THANKYOU!!")
            print("=====================================================================================")
            flagVal += 1
            break
        else:
            print("INVALID CHOICE!")
            continue
        break

if flagVal==0:
    main(money, flagVal)
else:
    pass

#THE CODE IS OFFICIALLY FINISHED
