from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Register.html')

@app.route('/',methods=["post"])
def register():
    return  'xyz';

if __name__ == '__main__':
    app.run(debug=True)