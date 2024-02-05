from flask import jsonify, Blueprint, request
from domain.user import User
from graphene import Schema
from gql.queries.user import Query
from gql.mutations.user import Mutation
import uuid

schema = Schema(query=Query, mutation=Mutation)

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users/<uuid:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)

    return jsonify({'id': user.id, 'username': user.username})


@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify([{'id': user.id, 'username': user.username} for user in users])


@user_routes.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    id = uuid.uuid4()
    username = data.get('username')

    result = schema.execute(f'''
        mutation {{
            createUser(id: "{id}", username: "{username}") {{
                user {{
                    id
                    username
                }}
            }}
        }}
    ''')

    if result.errors:
        return jsonify({'error': str(result.errors[0])}), 400

    return jsonify(result.data['createUser'])
