"""Sandwich calculator."""
import collections
import pyinputplus as pyip

BREAD_COST = {"wheat": 1, "white": 1.5, "sourdough": 1.5}
MEAT_COST = {"chicken": 3, "turkey": 4, "ham": 3, "tofu": 4}
CHEESE_COST = {"cheddar": 2, "swiss": 1.5, "mozzarella": 1}
SAUCE_COST = {"mayo": 0.2, "mustard": 0.1, "lettuce": 0.2, "tomato": 0.1}


def print_section_header(string: str):
    """Print title section."""
    print(f' {string} '.center(20, '='))


def make_sandwiches():
    """Build sandwich."""
    options = collections.defaultdict(int)
    print("Welcome to the sandwich ordering program!!! "
          "Please choose ingredients for your sandwich:")
    print_section_header('BREAD')
    bread = pyip.inputMenu(list(BREAD_COST.keys()))
    options[bread] = 1
    print_section_header('MEAT')
    meat = pyip.inputMenu(list(MEAT_COST.keys()))
    options[meat] = 1
    if pyip.inputYesNo('Would you like a cheese? ') == 'yes':
        cheese = pyip.inputMenu(list(CHEESE_COST.keys()))
        options[cheese] = 1
    else:
        cheese = ''
    if pyip.inputYesNo('Would you like a sauce? ') == 'yes':
        sauce = pyip.inputMenu(list(SAUCE_COST.keys()))
        options[sauce] = 1
    else:
        sauce = ''
    number = int(pyip.inputNum("How many sandwiches you want? ", min=1))
    total_cost = (BREAD_COST[bread] + MEAT_COST[meat] +
                  (CHEESE_COST[cheese] if cheese else 0) +
                  (SAUCE_COST[sauce] if sauce else 0)) * number

    print(f"Your sandwich consists of {', '.join(options)}. "
          f"You wanted {number} sandwich(es). That's a total of "
          f"{total_cost} eur")


if __name__ == "__main__":
    make_sandwiches()
