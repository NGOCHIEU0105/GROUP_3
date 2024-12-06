from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy user database
users = {"admin": "password123"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return f"<h1>Welcome, {username}!</h1>"
        else:
            return "<h1>Invalid credentials. Please try again.</h1>"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
