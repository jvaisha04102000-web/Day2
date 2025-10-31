#Simple inventory Management
inventory={"laptop":10,"mouse":25,"keyboard":15}

inventory["monitor"]=5
print(inventory)

inventory["laptop"]-=2
print(inventory)

if inventory.get("keyboard")>0:
    print(inventory["keyboard"])
