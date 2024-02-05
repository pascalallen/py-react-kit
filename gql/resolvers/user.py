from services.user_service import get_all_users, get_user_by_id

def resolve_users(root, info):
    return get_all_users()

def resolve_user(root, info, id):
    return get_user_by_id(id)