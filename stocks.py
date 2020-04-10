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

# for (ticker, name) in stockDict.items():
#     shares = 0
#     price = 0
#     for purchase in purchases:
#         if purchase[0] == ticker:
#             shares += purchase[1]
#             price += purchase[3]

#     print(f"I purchased {name} stock for ${shares * price}")

done = {}
for item in purchases:
    if item[0] not in done:
        done[item[0]] = [f"-----{item[0]}-----", 0]
    # print(done[item[0]].)

for (ticker, array) in done.items():
    break
    last_index = len(array) - 1
    for i in range(len(array)):
        if last_index == i:
            print(f"Total value of stock in portfolio: ${array[i]}")
            
        else:
            print(array[i])

else:
    print("done")
# print(done)
