"""Inventory Revisited."""


import collections
from dataclasses import dataclass

MAX_INVENTORY_CAP = 80
HEAVY_WEIGHT_THRESHOLD = 70
LIGHT_WEIGHT_THRESHOLD = 60


@dataclass
class Item:
    """Item data class."""

    name: str
    weight: int
    price: int


class Inventory:
    """Inventory class."""

    EXCLUDE_ITEMS = ['rubbish', 'chewed gum', 'used tissue']
    FOOD = ['apple', 'wine', 'chicken', 'bread']

    def __init__(self):
        """Init inventory."""
        super().__init__()
        self.inventory = collections.defaultdict(int)
        self.storage = []

    def add_item(self, item):
        """Add items to inventory."""
        if item.name in self.EXCLUDE_ITEMS:
            print(f'{item.name} was no added to inventory as it is rubbish\n')
        else:
            self.inventory[item.name] += 1
            self.storage.append(item)

    def remove_item(self, item_name):
        """Remove item from inventory."""
        if self.inventory[item_name] > 0:
            for i, item in enumerate(self.storage):
                if item.name == item_name:
                    del self.storage[i]
                    print(f'Removed {item} from Inventory\n')
                    self.inventory[item_name] -= 1
                    break

    def load_items(self, items):
        """Load lost of items to inventory."""
        skipped = collections.defaultdict(int)
        added_items_number = 0
        for item in items:
            if item.name in self.EXCLUDE_ITEMS:
                skipped[item.name] += 1
            else:
                self.inventory[item.name] += 1
                self.storage.append(item)
                added_items_number += 1
        print(f'added {added_items_number} items to inventory')
        print('Skipped:')
        for key, value in skipped.items():
            print(value, key)
        print()

    def check_weight(self):
        """Check waight and return severity."""
        severity = 0
        items_weight = self.weight
        if LIGHT_WEIGHT_THRESHOLD <= items_weight < HEAVY_WEIGHT_THRESHOLD:
            print('CAUTION: Your backpack weighs a lot, your stamina runs out quicker!')
            severity = 1
        elif HEAVY_WEIGHT_THRESHOLD <= items_weight < MAX_INVENTORY_CAP:
            print('CAUTION: Your equipment is very heavy, you\'re moving slower than usual!')
            severity = 2
        elif items_weight >= MAX_INVENTORY_CAP:
            print('CAUTION: You are overloaded, can\'t move!')
            severity = 3
        return severity

    @property
    def weight(self):
        """Get weight."""
        return sum(x.weight for x in self.storage)

    def __str__(self):
        """Print inventory."""
        to_print = 'Inventory:\n'
        items_count = 0
        items_weight = self.weight
        for key, value in self.inventory.items():
            to_print += str(value) + ' ' + str(key) + '\n'
            items_count += value
        to_print += '\n'
        to_print += (f'Total number of items: {items_count}\n'
                     f'Total weight of items: {items_weight}\n')
        if LIGHT_WEIGHT_THRESHOLD <= items_weight < HEAVY_WEIGHT_THRESHOLD:
            to_print += 'CAUTION: Your backpack weighs a lot, your stamina runs out quicker!'
        elif HEAVY_WEIGHT_THRESHOLD <= items_weight < MAX_INVENTORY_CAP:
            to_print += 'CAUTION: Your equipment is very heavy, you\'re moving slower than usual!'
        elif items_weight >= MAX_INVENTORY_CAP:
            to_print += 'CAUTION: You are overloaded, can\'t move!'
        return to_print


if __name__ == '__main__':
    hero_inventory = Inventory()
    for _ in range(42):
        hero_inventory.add_item(Item('gold coin', 1, 1))
    for _ in range(5):
        hero_inventory.add_item(Item('rope', 5, 2))

    dragon_loot = [
        Item('gold coin', 1, 1), Item('chewed gum', 1, 0), Item('dagger', 3, 1),
        Item('gold coin', 1, 1), Item('gold coin', 2, 1), Item('ruby', 3, 10),
        Item('rubbish', 5, 0), Item('chewed gum', 1, 0), Item('used tissue', 1, 0)]
    print(hero_inventory)
    hero_inventory.load_items(dragon_loot)
    print(hero_inventory)
    hero_inventory.remove_item('rope')
    hero_inventory.remove_item('rope')
    hero_inventory.remove_item('gold coin')
    hero_inventory.add_item(Item('used tissue', 1, 0))
    print(hero_inventory)
