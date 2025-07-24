from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/karakter')
def karakter():
    return render_template('karakter.html')

@app.route('/petualangan')
def petualangan():
    return render_template('petualangan.html')

@app.route('/tema_pesan')
def tema_pesan():
    return render_template('tema_pesan.html')

@app.route('/penutup')
def penutup():
    return render_template('penutup.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')