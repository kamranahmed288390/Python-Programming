p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe"
p4 = "click"

message = input("Enter your comment: ").lower()

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
