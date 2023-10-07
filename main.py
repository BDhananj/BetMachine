"""we're actually going to build a text based slot machine.

Now, the way this will work is the user will deposit a certain amount of money. We're then going to allow them to bet on either one,two or three lines of the slot machine, just to keep it pretty simple. I know in real slot machines they have a lot more lines than that

and then we are going to determine if they want. So if they got any lines, we're going to multiply their bet by the value of the line,

add that to their balance, and then allow them to keep playing until they want to cash out or until they run out of money. So- this is actually a fairly complex project because we need to do a lot of things. We need to collect the users deposit, we need to add that to their balance.

We need to allow them to bet on a line or on multiple lines. We then need to see if they actually got any of those lines.

We then need to spin the slot machine or we would have done that before, right? We need to generate the different items that are going to be in the slot machine

on the different reels, and then we need to add whatever they won back to their balance. So there's quite a bit of stuff going on here

consider we have 3*3 slot machine
"""
import random #use this to generate random values in slot machine



MAX_LINES = 3  # Global constant 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#symbols in each column
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

# what is the value amout you get for each symbol
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, line, bet, values):
    winnings = 0
    winning_lines = []
    #check the rows user bet on
    for line in range(line):
        #check symbols are same
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet  # bet on each line
            winning_lines.append(line+1) # adding +1 to the index
    
    return winnings, winning_lines



#generate what symbols are gonna be in each column randomely
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # this holds all the symbols based on the count
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] # each of this nested list represent values in column , columns = [[], [], []]
    for col in range(cols):
        column = []  # it has like [A, A, C] column values, we need to Transpose it later
        current_symbols = all_symbols[:] # here we dont need reference of a object , we are making a copy by using ':' (slice operator) inside list
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    """ here we have all our columns defined as rows , so we need to flip them
    recevied cols: [['D', 'C', 'D'], ['D', 'D', 'A'], ['D', 'D', 'D']]
    so we need to flip them into 

    D | D | D
    C | D | D
    D | A | D

    """
    # Get the row count by using len of columns , columns[0] : this assure we atleast have one column
    print(f"recevied cols: {columns}")
    for row in range(len(columns[0])): 
         #loop through all cols
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ") # every single row
            else:
                print(column[row], end = "")
        print() # ends with newline \n, go to next line at every row

# collect user input for deposit from user

def deposit():
    while True: # ask continuously until we get valid amout
        amount = input("what would you like to deposit ? $ ")
        #check its a number 
        if amount.isdigit():
            amount = int(amount)
            #check if number >0
            if amount > 0 :
                break
            else:
                print("amount is not more than 0.")
        else:
            print("Please Enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on ( 1 - " + str(MAX_LINES)+ ")?")
        if lines.isdigit():
            lines = int(lines)
            #chcek the boundary
            if 1 <= lines  <=  MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter valid amount")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    # check the bet amount not exceeds balance
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"you do not have enough amount to bet , your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")
    #print(balance , lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f" You Won  ${winnings}")
    print(f"You won on lines", *winning_lines) # unpack list here
    return winnings - total_bet

def main():

    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if balance == 0:
            balance = deposit()  
        if answer == "q" :
            break
            
        balance += spin(balance)
        
            

    print(f"You left with ${balance}")
    

main()