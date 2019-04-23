from flask import Flask, jsonify, request, redirect
from examples.norvig_spell import correction

app = Flask(__name__)


# routes
@app.route("/")
def index():
    return redirect('/spell?q=helol')


@app.route("/spell", methods=['GET', 'POST'])
def spellcheck():
    word = request.args.get('q', 'Hello')
    return jsonify(word=word, correction=correction(word))


@app.route('/correct/<word>')
def show_user_profile(word):
    # show the user profile for that user
    return jsonify(word=word, correction=correction(word))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
