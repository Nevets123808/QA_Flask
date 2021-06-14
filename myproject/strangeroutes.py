from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome, friends to the show that never ends."

@app.route('/<garble>')
def garble(garble):
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return 'this is nonsense'


if __name__ == '__main__':
    app.run(debug=True)