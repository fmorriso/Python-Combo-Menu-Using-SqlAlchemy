import sys

import sqlalchemy as sa

from menu_item import MenuItem
from restaurant import Restaurant
from single_order import SingleOrder


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_SqlAlchemy_version() -> str:
    return sa.__version__


def make_example_menu_items() -> None:
    category = 'Sandwich'
    for selection in (['Chicken', 5.25], ['Beef', 6.25], ['Tofu', 5.75]):
        menu_item = MenuItem(category, selection[0], selection[1])
        print(f'{menu_item=}')

    # example of a menu item with override of default quantity
    menu_item = MenuItem(category, 'Chicken sliders', 1.5, 2)
    print(f'{menu_item=}')


def get_order() -> SingleOrder:
    order = SingleOrder()
    order.get_sandwich()
    order.get_beverage()
    order.get_fries()
    order.get_ketchup_packets()
    order.check_for_discount()
    order.display()

    return order

if __name__ == '__main__':
    print(f'Combo Menu via SqlAlchemy using python version {get_python_version()}')
    print(f'and SQLAlchemy version {get_SqlAlchemy_version()}')

    # make_example_user()
    # make_example_menu_items()

    restaurant = Restaurant("Fred's Fast Food")
    print(f'Welcome to {restaurant.name} where the food is always delicious.')

    current_order: SingleOrder = get_order()
