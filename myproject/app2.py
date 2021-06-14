from flask import Flask, url_for, redirect

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def main():
    return "This is the home page"

# @app.route('/home')
# def home():
#     return redirect(url_for('main'))
@app.route('/about')
def about():
    return "This is the about page"

if __name__ == '__main__':
    app.run(debug=True)