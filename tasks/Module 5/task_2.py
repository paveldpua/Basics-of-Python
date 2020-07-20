"""Hero's Adventure Game."""
from random import randint, choice
from dataclasses import dataclass
from task_1 import Item, Inventory, LIGHT_WEIGHT_THRESHOLD


FOOD = ["apple", "wine", "chicken", "bread"]
RUBBISH = ["chewed gum", "used tissue"]
ITEMS = ["gold coin", "ruby", "dagger", "rope", "sword", "shield"] + FOOD + RUBBISH
MOVES = ["north", "south", "west", "east", "l", "r", "u", "d"]


@dataclass
class GameItem(Item):
    """GameItem class."""

    heal: int = 0

    def is_rubbish(self):
        """Check if Item is rubbish."""
        return self.name in RUBBISH

    def is_food(self):
        """Check if Item is food."""
        return self.name in FOOD


class Hero:
    """Class Hero."""

    def __init__(self, row, columm):
        """Init Hero."""
        super().__init__()
        self.inv = Inventory()
        self.stamina = 50
        self.position = (row - 1, columm - 1)
        self.can_move = True

    def set_position(self, row, colum):
        """Set initial posision of hero on a field."""
        self.position = (row, colum)

    def heal(self, item):
        """Heal the hero with food."""
        self.stamina += item.heal
        print(
            f"I got the {item.name}. Increased stamina with {item.heal}."
            " Current stamia is {self.stamina}"
        )

    def get_stats(self):
        """Print hero statistics."""
        print(f"Stamina {self.stamina}/50\n" f"{self.inv}")

    def drop_item(self, item):
        """Remove item vrom inventory."""
        self.inv.remove_item(item)

    def check_heal(self):
        """Check current stamina value."""
        if self.stamina <= 0:
            print(f"You fainted and die, your stamina is {self.stamina}")
            return -1
        if self.stamina <= 10:
            print(f"Your healt is too low - {self.stamina}, you need more food")
            return 0
        return 1

    def check_weight(self):
        """Check weight of backpack and ask for drop."""
        if not self.can_move:
            print(
                f"You are overweighed. Current weight of your backpack is {self.inv.get_weight()}\n"
                f"Please drop any item from Inventory"
            )
            self.get_stats()
            responce = input("Write an item name to drop: ").rstrip()
            self.drop_item(responce)
        if self.inv.check_weight() < 3:
            self.can_move = True
        return self.can_move


class Field:
    """Class Field."""

    def __init__(self, columns, rows):
        """Init Field class."""
        self.field = [[" " for c in range(columns)] for r in range(rows)]
        self.columns = columns
        self.rows = rows

    def set_hero(self, hero):
        """Set hero to position."""
        self.field[hero.position[0]][hero.position[1]] = "H"

    def place_items(self):
        """Initialize field with items."""
        for row in self.field:
            item_name = choice(ITEMS)
            cost = 0 if item_name in RUBBISH else randint(1, 5)
            heal = 0 if item_name not in FOOD else randint(5, 10)
            random_position = randint(0, len(row) - 1)
            if row[random_position] != "H":
                item_position = random_position
            elif random_position == len(row) - 1:
                item_position = random_position - 1
            elif random_position == 0:
                item_position = random_position + 1
            row[item_position] = GameItem(item_name, randint(15, 20), cost, heal)

    def move_hero(self, hero, direction):
        """Move hero."""
        initial_position = hero.position
        # print('initial position', initial_position)
        if direction in ("north", "u"):
            # to not cross border
            aligned_init_pos = (
                len(self.field) if initial_position[0] == 0 else initial_position[0]
            )
            # get current contenf of the cell
            cell_content = self.field[aligned_init_pos - 1][initial_position[1]]
            # move hero to new position
            self.field[aligned_init_pos - 1][initial_position[1]] = "H"
            # change hepo position on hero object
            hero.position = (aligned_init_pos - 1, initial_position[1])
        elif direction in ("south", "d"):
            aligned_init_pos = (
                -1
                if initial_position[0] == len(self.field) - 1
                else initial_position[0]
            )
            cell_content = self.field[aligned_init_pos + 1][initial_position[1]]
            self.field[aligned_init_pos + 1][initial_position[1]] = "H"
            hero.position = (aligned_init_pos + 1, initial_position[1])
        elif direction in ("west", "l"):
            aligned_init_pos = (
                len(self.field[0]) if initial_position[1] == 0 else initial_position[1]
            )
            cell_content = self.field[initial_position[0]][aligned_init_pos - 1]
            self.field[initial_position[0]][aligned_init_pos - 1] = "H"
            hero.position = (initial_position[0], aligned_init_pos - 1)
        elif direction in ("east", "r"):
            aligned_init_pos = (
                -1
                if initial_position[1] == len(self.field[0]) - 1
                else initial_position[1]
            )
            cell_content = self.field[initial_position[0]][aligned_init_pos + 1]
            self.field[initial_position[0]][aligned_init_pos + 1] = "H"
            hero.position = (initial_position[0], aligned_init_pos + 1)
        # clear initial hero position
        self.field[initial_position[0]][initial_position[1]] = " "
        # print('position after move', hero.position)
        return cell_content

    def __str__(self):
        """Draw field."""
        to_print = ""
        for _, row in enumerate(self.field):
            to_print += "+---" * self.columns + "+\n"
            to_print += (
                "| "
                + " | ".join(map(lambda x: "X" if isinstance(x, Item) else x, row))
                + " |\n"
            )
        to_print += "+---" * self.columns + "+\n"
        return to_print


class Game:
    """Main Game class."""

    def __init__(self, columns, rows, hero):
        """Init Game instance."""
        self.field = Field(columns, rows)
        self.field.place_items()
        self.hero = hero
        self.field.set_hero(self.hero)
        self.debug = False

    def __handle_responce(self, responce):
        if responce in ("stats", "s"):
            self.hero.get_stats()
            _ = input()
        if responce.startswith("drop"):
            print(self.hero.inv)
            responce = input("What to drop? ").rstrip()
            self.hero.inv.remove_item(responce)
        if responce in MOVES:
            self.hero.stamina -= (
                1 if self.hero.inv.get_weight() < LIGHT_WEIGHT_THRESHOLD else 4
            )
            cell_content = self.field.move_hero(self.hero, responce)
            if self.debug:
                print(cell_content, cell_content.__class__)
            if self.debug:
                print(self.hero.stamina)
            if isinstance(cell_content, GameItem):
                if cell_content.is_food():
                    self.hero.heal(cell_content)
                    return
                print(f"New item found! It is a {cell_content.name}")
                self.hero.inv.add_item(cell_content)
                if self.hero.inv.check_weight() > 2:
                    self.hero.can_move = False
                if self.debug:
                    print(self.hero.inv)

    def play(self):
        """Run main play loop."""
        print(" LET GAME BEGINS ".center(50, "="))
        while any(isinstance(x, GameItem) for row in self.field.field for x in row):
            if not self.hero.check_weight():
                continue
            if self.hero.check_heal() < 0:
                break
            print(self.field)
            responce = input("Choose an action: ").rstrip()
            if responce in ("exit", "q"):
                break
            self.__handle_responce(responce)
        else:
            print(self.field)
            self.hero.get_stats()


if __name__ == "__main__":

    game = Game(10, 10, Hero(5, 5))
    game.play()
