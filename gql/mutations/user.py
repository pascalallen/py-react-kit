from graphene import Mutation, UUID, String, Field, ObjectType
from domain.user import User
from domain.base import db
from gql.queries.user import UserType

class CreateUser(Mutation):
    class Arguments:
        id = UUID(required=True)
        username = String(required=True)

    user = Field(lambda: UserType)

    def mutate(root, info, id, username):
        new_user = User(id=id, username=username)
        db.session.add(new_user)
        db.session.commit()

        return CreateUser(user=new_user)


class Mutation(ObjectType):
    create_user = CreateUser.Field()
