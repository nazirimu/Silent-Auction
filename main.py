from replit import clear
from art import logo

auction_bidders = {}

def add_auction(name_of_bidder, bid_amount):
    auction_bidders[name_of_bidder] = bid_amount

print(logo)
print('''
Instruction:
1. Enter your name and then your bid amount.
2. If there are more biders, type "yes" when prompted and then pass the computer to the bider.
''')

more_bidders = True
while more_bidders:
    name = input("Name of bidder: ")
    bid = int(input("Bid amount: $"))
    repeat = input('For more biders types "yes". Otherwise type "no". ').lower()
    add_auction(name, bid)
    if repeat == 'no':
        more_bidders = False
    clear()

max_bid = 0
max_bidder = ''
for bidder in auction_bidders:
    if auction_bidders[bidder] > max_bid:
        max_bider = bidder
        max_bid = auction_bidders[bidder]

print(f'The highest bidder was {max_bidder} with a bid of ${max_bid}')
    
    





