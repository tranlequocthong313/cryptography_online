from flask import Flask, render_template, request, redirect

from app.algorithms import caesar
from app.algorithms import vigenere
from app.algorithms import playfair


app = Flask(__name__)


@app.get('/')
def home():
    return redirect('/caesar')


@app.route('/caesar')
def caesar_page():
    return render_template('caesar.html', mode=get_mode())


@app.post('/caesar')
def caesar_encrypt():
    mode = get_mode()

    message = request.form['message']
    key = request.form['key']

    if mode == 'encrypt':
        result = caesar.encrypt(message, key)
    elif mode == 'decrypt':
        result = caesar.decrypt(message, key)

    return render_template('caesar.html', mode=get_mode(), result=result)


@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html', mode=get_mode())


@app.post('/vigenere')
def vigenere_encrypt():
    mode = get_mode()

    message = request.form['message']
    key = request.form['key']

    if mode == 'encrypt':
        result = vigenere.encrypt(message, key)
    elif mode == 'decrypt':
        result = vigenere.decrypt(message, key)

    return render_template('vigenere.html', mode=get_mode(), result=result)


@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html', mode=get_mode())


@app.post('/playfair')
def playfair_encrypt():
    mode = get_mode()

    message = request.form['message']
    key = request.form['key']

    if mode == 'encrypt':
        result = playfair.encrypt(message, key)
    elif mode == 'decrypt':
        result = playfair.decrypt(message, key)

    return render_template('playfair.html', mode=get_mode(), result=result)


def get_mode():
    mode = request.args.get('tab') 
    valid_modes = ['encrypt', 'decrypt']
    return mode if mode in valid_modes else 'encrypt'


if __name__ == '__main__':
    app.run(debug=True)
