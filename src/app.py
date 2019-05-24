from flask import Flask
import connexion


app = connexion.App(__name__, specification_dir="./")
app.add_api('./configuration/swagger.yml')

@app.route('/')
def dashboard():
    return"Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)