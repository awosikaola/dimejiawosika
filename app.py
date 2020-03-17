from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    try:
        port = int(sys.argv[1])
    except:
        port = 12345

    app.run(port=port, debug=True)