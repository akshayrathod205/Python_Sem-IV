from flask import Flask, redirect, jsonify

app = Flask(__name__)

@app.route('/books')
def books():
    return 'Here are some books'


@app.route('/result/<int:marks>')
def result(marks):
    if marks < 50:
        return redirect('/failed')
    else:
        return redirect('/passed')


@app.route('/failed')
def failed():
    message = 'Sorry, you failed the exam!'
    return jsonify({'message': message})

@app.route('/passed')
def passed():
    message = 'Congratulations, you passed the exam!'
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True)
