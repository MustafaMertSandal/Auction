import art

print(art.logo)
print("Welcome to the secret auction program.")
bids = {}

while True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bids[name] = int(bid)

    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if new_bidder == "no":
        break
    print("\n" * 20) #Onceki bid gozukmesin diye

max_key = ""
max_value = 0
for key in bids:
    if(bids[key] > max_value):
        max_key = key
        max_value = bids[key]
print(f"The winner is {max_key} with a bid of ${bids[max_key]}")