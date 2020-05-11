import pwd


def fetch_users():
    users = []
    for user in pwd.getpwall():
        if is_real_user() and user_has_home_dir(user):
            users.append({
                'name': user.pw_name,
                'id': user.pw_uid,
                'home': user.pw_dir,
                'shell': user.pw_shell,
            })
    return users


def is_real_user(user):
    return user.pw_uid >= 1000


def user_has_home_dir(user):
    return 'home' in user.pw_dir
