from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Soham@2006",
    database="petshop"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        product = request.form['product']
        address = request.form['address']
        cursor.execute("INSERT INTO orders (name, phone, email, product, address) VALUES (%s, %s, %s, %s, %s)",
                       (name, phone, email, product, address))
        db.commit()
        return redirect('/')
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM officials WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            session['user'] = username
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        return render_template('dashboard.html', orders=orders)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
