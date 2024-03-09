import sys

import sqlalchemy as sa

from menu_item import MenuItem


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_SqlAlchemy_version() -> str:
    return sa.__version__


def make_example_menu_items() -> None:
    category = 'Sandwich'
    for selection in (['Chicken', 5.25], ['Beef', 6.25], ['Tofu', 5.75]):
        menu_item = MenuItem(category, selection[0], selection[1])
        print(f'{menu_item=}')

    menu_item = MenuItem(category, 'Chicken sliders', 1.5, 2)
    print(f'{menu_item=}')


if __name__ == '__main__':
    print(f'Combo Menu via SqlAlchemy using python version {get_python_version()}')
    print(f'and SQLAlchemy version {get_SqlAlchemy_version()}')

    # make_example_user()
    make_example_menu_items()
