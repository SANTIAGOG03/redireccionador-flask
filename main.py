
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://alacarta-3-0-g3rb.vercel.app/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
