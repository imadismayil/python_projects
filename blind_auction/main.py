from art import logo
print(logo)
bidding = True
auction = {}
while bidding:
    name = input("Enter Your Name:")
    bid = float(input("Enter Your bid Amount:$"))
    auction[name] = bid
    choice = input("Type Yes if there are other person's left to bid,if nor type no.").lower()
    if choice == "no":
        bidding = False
    else:
        print("\n" * 20)
highest = 0
top_bidder = "nil"
for name in auction:
    if auction[name] > highest:
        highest = auction[name]
        top_bidder = name

print(f"The winner of the auction is {top_bidder} with a winning bid of ${highest}")

# method 2
# res = max(auction, key=auction.get)
# print(f"The winner of the auction is {res} with a winning bid of ${auction[res]}")

# # method 3
# res2 = sorted(auction, key=auction.get,reverse=True)[0]
# print(f"The winner of the auction is {res2} with a winning bid of ${auction[res2]}")
