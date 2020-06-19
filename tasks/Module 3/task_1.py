"""Sandwich calculator."""
import pyinputplus as pyip

BREAD_COST = {"wheat": 1, "white": 1.5, "sourdough": 1.5}
MEAT_COST = {"chicken": 3, "turkey": 4, "ham": 3, "tofu": 4}
CHEESE_COST = {"cheddar": 2, "swiss": 1.5, "mozzarella": 1}
SAUSE_COST = {"mayo": 0.2, "mustard": 0.1, "lettuce": 0.2, "tomato": 0.1}


def sandwich_maker():
    """Build sandwich."""
    print("Welcome to the sandwich ordering program!!! Please choose ingridients for your sandwich:")
    print(' BREAD '.center(20, '='))
    bread = pyip.inputMenu(list(BREAD_COST.keys()))
    print(' MEAT '.center(20, '='))
    meat = pyip.inputMenu(list(MEAT_COST.keys()))
    if pyip.inputYesNo('Would you like a cheese? ') == 'yes':
        cheese = pyip.inputMenu(list(CHEESE_COST.keys()))
        cheese_to_print = f", {cheese}"
    else:
        cheese = ''
        cheese_to_print = ''
    if pyip.inputYesNo('Would you like a sause? ') == 'yes':
        sause = pyip.inputMenu(list(SAUSE_COST.keys()))
        sause_to_print = f", {sause}"
    else:
        sause = ''
        sause_to_print = ''
    number = int(pyip.inputNum("How many sandwiches you want? ", min=1))
    total_cost = (BREAD_COST[bread] + MEAT_COST[meat] + (CHEESE_COST[cheese] if cheese else 0) + (SAUSE_COST[sause] if sause else 0)) * number

    print(f"Your sandwich consists of {bread} bread, {meat}{cheese_to_print}{sause_to_print}. You wanted {number} sandwich(es). That's a total of {total_cost} eur")


if __name__ == "__main__":
    sandwich_maker()
