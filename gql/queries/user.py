from graphene import ObjectType, String, UUID, Field, List
from domain.user import User

class UserType(ObjectType):
    id = UUID()
    username = String()


class Query(ObjectType):
    user = Field(UserType, id=UUID(required=True))
    users = List(UserType)

    def resolve_user(root, info, id):
        return User.query.get(id)

    def resolve_users(root, info):
        return User.query.all()
