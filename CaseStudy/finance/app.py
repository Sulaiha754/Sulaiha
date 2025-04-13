from flask import Flask, render_template, request, redirect, url_for, session, flash
from db_config import get_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management


# Combined Login/Register Page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        # LOGIN
        if form_type == 'login':
            email = request.form['email']
            password = request.form['password']

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = cursor.fetchone()

            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid login credentials!", "error")
                return redirect(url_for('home'))

        # REGISTER
        elif form_type == 'register':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            conn = get_connection()
            cursor = conn.cursor()

            # Check if email exists
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            if cursor.fetchone():
                flash("Email already registered!", "error")
                return redirect(url_for('home'))

            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           (username, email, password))
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('home'))

    return render_template('index.html')


# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html', username=session.get('username'))


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
