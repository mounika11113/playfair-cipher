from flask import Flask, render_template, request
from playfair import encrypt, decrypt, create_matrix, format_matrix

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""
    matrix = ""

    if request.method == 'POST':

        key = request.form['key']
        text = request.form['text']

        action = request.form['action']

        if action == "encrypt":
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        matrix = format_matrix(create_matrix(key))

    return render_template(
        'index.html',
        result=result,
        matrix=matrix
    )

if __name__ == '__main__':
    app.run(debug=True)