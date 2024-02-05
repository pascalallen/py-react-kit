from domain.user import User

def get_all_users():
    return User.query.all()

def get_user_by_id(id):
    return User.query.get(id)