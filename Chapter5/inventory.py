stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
    return(inventory)


displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)