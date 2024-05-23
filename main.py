# name: str = input("Enter your name: ")
# print(f'WITAJ{name}')

data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 8, 'location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Wątroba', 'posts': 12, 'location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]['name']}')


def read(users: list) -> None:
    """
    show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'twój znajomy: {user['name']}, opublikował: {user['posts']}')


# read(data_of_users)

def create(users: list) -> None:
    """
    add a user to a list
    :param users: user list
    :return: none
    """
    name=input("Enter your name: ")
    surname:str='Szczepaniuk'
    posts:int=int(input("Enter your number of posts: "))
    location:str='Mińsk Mazowiecki'
    new_user: dict={'name': name, 'surname': surname, 'post': posts, 'location': location}
    users.append(new_user)

# add_user(data_of_users)
# read(data_of_users)
