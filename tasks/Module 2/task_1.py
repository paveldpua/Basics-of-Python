"""Work with inventory."""


def display_inventory(inventory):
    """Print inventory."""
    print('Inventory:')
    items = 0
    # check that inventory is a dict
    if not isinstance(inventory, dict):
        print('Wrong inventory type. Should be dict')
        return
    # print inventory and calculate sum of items
    for key, value in inventory.items():
        print(value, key)
        items += value
    print()
    # check number of item and print according caution if needed
    print('Total number of items:', items, end='\n\n')
    if 60 <= items <= 69:
        print('CAUTION: Your backpack weighs a lot, your stamina runs out quicker!')
    elif 70 <= items <= 79:
        print('CAUTION: Your equipment is very heavy, you\'re moving slower than usual!')
    elif items >= 80:
        print('CAUTION: You are overloaded, can\'t move!')


def add_to_inventory(inventory, added_items):
    """Add items from list to inventory."""
    skipped = {}
    added_items_number = 0
    rubbish = ['rubbish', 'chewed gum', 'used tissue']

    for item in added_items:
        if item in rubbish:
            if item in skipped:
                skipped[item] += 1
            else:
                skipped[item] = 1
        else:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
            added_items_number += 1
    print(f'added {added_items_number} items to inventory')
    print('Skipped:')
    for key, value in skipped.items():
        print(value, key)
    print()
    return inventory


hero_inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'rubbish', 'chewed gum', 'used tissue']
inv = add_to_inventory(hero_inventory, dragon_loot)
display_inventory(hero_inventory)
