from flask import Flask

app = Flask(name)

@app.route('/')
def helloworld():
    return 'Hello, World!'

if name == '_main':
    app.run(debug=True)