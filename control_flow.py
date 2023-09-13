print('Control Flow')
# if condition to test:
# code to execute if  test passes

bank_balance = 100.00
item_cost = int(input("Enter the cost of the item: "))
if item_cost < bank_balance:
    bank_balance -= item_cost
    print("Transaction successful")
    print(bank_balance)
elif item_cost == bank_balance:
    bank_balance -= item_cost
    print("Transaction successful, no more funds left")
    print(bank_balance)
else:
    print("Transaction failed, Insufficient Bank Balance")
    print(bank_balance)
if True:
    pass
if True and True:
    if False or True:
        print("and, or")


print("loops(while, for")
# while condition:
# execute code as long as condition is still true
while True:
    break
# for condition:
# execute code as long as condition is still true
for value in range(1, 10, 2):
    print(value)
    continue

print("Match Case")
language = "python3"
match language:
    case "python":
        print("Hey you are learning python")
    case "javascript":
        print("Hey you are learning javascript")
    case _:
        print("Hey you are learning default language")
