LEXICON_MENU: dict[str: str] = {
    'First But': 'First But',
    'B2': 'Second But',
    'B3': 'Third But'
}

# LEXICON_MENU: dict[str: str] = {
#     'First But': 'First But'
#     # 'B1': 'First But',
#     # 'B2': 'Second But',
#     # 'B3': 'Third But'
# }


LEXICON_INLINE: dict[str: str] = {
    'Nobe1': 'First Nobe',
    # 'First Nobe': 'First Nobe',
    'Nobe2': 'Second Nobe',
    'Nobe3': 'Third Nobe'
}

# menu_level: str = '0'
# button_data: list[str] = ['', '', '']

# alt_buttons: dict[str: str] = {
#     'B0': 'Choose from the list',
#     'B1': 'Take a new photo'
#     # 'B1': '',
#     # 'B2': ''
# }

# Не используется
# alt_buttons: list[str] = ['Choose from the list', 'Take a new photo']

# Далее везде int - это идентификатор пользователя message.from_user.id или callback.from_user.id (они совпадают)
main_buttons: dict[int: [str]] = {}

# labels: list[str] = ['', '', '']
labels: dict[int: [str]] = {}

choosen_label: dict[int: str] = {}

probabilities: dict[int: [float]] = {}

# msg: int = 0
