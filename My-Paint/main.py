from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


app.run(debug=True,port=5000,host='0.0.0')


# erasor icon added.