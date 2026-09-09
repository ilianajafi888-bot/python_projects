

bid = {}
end_of_bid = True

def finding_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the highest amount of ${highest_bid}")

while end_of_bid:
    name = input("name of the bidder? ")
    price = int(input("the money you wanna bid $"))
    bid[name] = price
    more = input("are there any other bidders type 'yes' or 'no' ")
    if more == "no":
        end_of_bid = False
        
    elif more == "yes":
        print("pass the phone to the next person")
finding_highest_bid(bidding_record=bid)




