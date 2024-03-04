import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A':2,
    'B':3,
    'C':5,
    'D':7
}

symbol_value = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check_symbol = column[line]
            if symbol != check_symbol:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings, winning_lines





def get_slot_machine_spin(rows, cols, symbols):
    all_symbol=[]
    for symbol, symbol_count in symbols.items():  #.items gives both key and value associated with dict
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol.copy()
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end='|')
            else:
                print(column[row], end='')

        print()
                     


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid amount.")
    return amount
    
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines

        if total > balance:
            print(f"You don't have enough balance. Your current balance is {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. So your total bet is, {total}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines:', *winning_lines)

    return winnings - total

def main():
    balance = deposit()
    while True:
        print(f'Current Balance is {balance}')
        answer = input('Press enter to spin (q to quit):')
        if answer == "q":
            break
        else:
            balance += spin(balance)

    print(f'You left with {balance}')


main()

