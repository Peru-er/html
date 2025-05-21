
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/countries/')
def countries():
    places = [
        'Tokio, Japan',
        'Paris, France',
        'Roma, Italy',
        'Kiyv, Ukraine',
        'Madrid, Spain'
    ]
    return render_template('countries.html', places=places)

@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
