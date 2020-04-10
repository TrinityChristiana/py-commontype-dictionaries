# **************************** Challenge: Stock Portfolio ****************************
"""
Author: Trinity Terry
pyrun: python stocks.py  
"""

stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak"
}

purchases = [
    ('GE', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GE', 200, '1-jul-1998', 56)
]

"""
Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

Example output for one block: I purchased General Electric stock for $4800
"""
print("******** Purchase History Report ************************************************")
for (ticker, name) in stockDict.items():
    shares = 0
    price = 0
    for purchase in purchases:
        if purchase[0] == ticker:
            shares += purchase[1]
            price += purchase[3]

    print(f"I purchased {name} stock for ${shares * price}")

"""
Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

Example output:
    ------ GE ------
    100 shares at 48 dollars each on 01-jul-1998
    200 shares at 56 dollars each on 10-sep-2001

    Total value of stock in portfolio: $16000
"""

print("******** Purchase Summary ************************************************")

# a dictionary that will hold values to show in console
done = {}

for item in purchases:
    if item[0] not in done:
        done[item[0]] = [f"-----{item[0]}-----", "", 0, ""]

    done[item[0]].insert(1,
                         f"{item[1]} shares at {item[3]} dollars each on {item[2]}")
    done[item[0]][-2] += item[1] * item[3]

for (ticker, array) in done.items():
    last_index = len(array) - 2

    for i in range(len(array)):
        if last_index == i:
            print(f"Total value of stock in portfolio: ${array[i]}")
        else:
            print(array[i])
