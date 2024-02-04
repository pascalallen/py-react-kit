from flask import Flask, render_template, request
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(
        name=String(default_value="World!")
    )

    def resolve_hello(self, info, name):
        return 'Hello, ' + name

helloSchema = Schema(query=Query)

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    hello_query = """
        {
            hello ( name : "%s" )
        }
    """%(name)

    result = helloSchema.execute(hello_query)

    return {
        "data": result.data['hello']
    }

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it externally accessible
    app.run(host='0.0.0.0', port=8080)
