from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it externally accessible
    app.run(host='0.0.0.0', port=8080)
