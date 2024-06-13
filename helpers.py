import sqlite3
from uuid import uuid4

# Luhn's Algorithm checksum function
def checksum(credit_card):
    #credit card number sent as a string
    credit_card = str(credit_card)[::-1]
    total = 0

    for i, digit in enumerate(credit_card):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9 
        total += digit
    
    return total % 10 == 0

# what is the type of valid credit card
def card_type(credit_card):
    
    if len(credit_card) == 13:
        if credit_card[0] == '4':
            return 'VISA'
        return 0
    
    if len(credit_card) == 16:
        if credit_card[0] == '4':
            return ('VISA')
        if 51 <= int(credit_card[0:2]) <= 55:
            return ('MASTERCARD')
        if 2221 <= int(credit_card[0:4]) <= 2720:
            return 'MASTERCARD'
        return 0

    if len(credit_card) == 15:
        if credit_card[0:2] in ('34', '37'):
            return 'AMEX'
        return 0
    return 0

# Initializes an SQLite3 database
def db_init():
    connection = sqlite3.connect('credit_card.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    credit_card_hashed TEXT NOT NULL,
    credit_card_type TEXT NOT NULL
)
''')

    connection.commit()
    connection.close()

# Inserts credit card inforamtion into the database
def insert_recorder(user_id, credit_card_hashed, credit_card_type):
    connection = sqlite3.connect('credit_card.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO credit_cards (user_id, credit_card_hashed, credit_card_type) VALUES (?, ?, ?)", (user_id, credit_card_hashed, credit_card_type))

    connection.commit()
    connection.close()

def generate_user_id():
    return str(uuid4())


