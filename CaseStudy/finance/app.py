from flask import Flask, render_template, request, redirect, url_for, session, flash
from db_config import get_connection
import os

# Ensure Flask knows where to look for templates
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'



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


# Expense page to view and add new expenses
@app.route('/expense', methods=['GET', 'POST'])
def expense():
    if request.method == 'POST':
        try:
            # Get form data
            amount = request.form['amount']
            category = request.form['category']
            date = request.form['date']
            description = request.form['description']
            user_id = session.get('user_id')  # Get logged-in user ID from session

            # Look up category_id from category name
            cursor = get_connection().cursor()
            cursor.execute("SELECT category_id FROM expense_categories WHERE category_name = ?", (category,))
            category_row = cursor.fetchone()

            if not category_row:
                flash(f"Category '{category}' not found.", "error")
                return redirect(url_for('expense'))

            category_id = category_row[0]  # Get the category_id

            # Insert the expense into the expenses table
            cursor.execute(""" 
                INSERT INTO expenses (user_id, category_id, amount, date, description)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, category_id, amount, date, description))

            cursor.connection.commit()  # Commit the transaction
            cursor.close()

            flash("Expense added successfully!", "success")
            return redirect(url_for('expense'))  # Redirect to the expense page to show new data

        except Exception as e:
            flash(f"Error adding expense: {str(e)}", "error")
            return redirect(url_for('expense'))

    # For GET requests, fetch expenses for the logged-in user
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.expense_id, e.amount, c.category_name, e.date, e.description
        FROM expenses e
        JOIN expense_categories c ON e.category_id = c.category_id
        WHERE e.user_id = ?
        ORDER BY e.date DESC
    """, (session.get('user_id'),))
    expenses = cursor.fetchall()
    cursor.close()

    return render_template('expense.html', expenses=expenses)


# Edit Expense Route
@app.route('/edit_expense/<int:expense_id>', methods=['POST'])
def edit_expense(expense_id):
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    description = request.form['description']

    conn = get_connection()
    cursor = conn.cursor()

    # Look up category_id from category name
    cursor.execute("SELECT category_id FROM expense_categories WHERE category_name = ?", (category,))
    category_row = cursor.fetchone()
    if not category_row:
        flash(f"Category '{category}' not found.", "error")
        return redirect(url_for('expense'))

    category_id = category_row[0]  # Get the category_id

    # Update the expense in the expenses table
    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category_id = ?, date = ?, description = ?
        WHERE expense_id = ?
    """, (amount, category_id, date, description, expense_id))

    conn.commit()
    cursor.close()

    flash("Expense updated successfully!", "success")
    return redirect(url_for('expense'))


# Delete Expense Route
@app.route('/delete_expense/<int:expense_id>')
def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Delete the expense from the expenses table
    cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id,))
    conn.commit()
    cursor.close()

    flash("Expense deleted successfully!", "success")
    return redirect(url_for('expense'))


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
