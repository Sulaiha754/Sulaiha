from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao.financerepoimpl import FinanceRepoImpl
from exception.invaliduserexception import InvalidUserException

app = Flask(__name__)
app.secret_key = 'supersecret123'

finance_repo = FinanceRepoImpl()

@app.route('/')
def show_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    try:
        user = finance_repo.validate_user(email, password)
        session['user_id'] = user['user_id']
        session['email'] = user['email']
        return redirect('/dashboard')
    except InvalidUserException as e:
        flash(str(e))
        return redirect('/')
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        from util.dbconnutil import get_connection  # Import the required module or function
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    expenses = finance_repo.get_user_expenses(user_id)
    incomes = finance_repo.get_user_incomes(user_id)
    exp_categories = finance_repo.get_expense_categories()
    inc_categories = finance_repo.get_income_categories()
    return render_template(
        'index.html',
        username=session['email'],
        expenses=expenses,
        incomes=incomes,
        exp_categories=exp_categories,
        inc_categories=inc_categories
    )

@app.route('/add-expense', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    category_id = int(request.form['expense_category'])
    amount = float(request.form['expense_amount'])
    date = request.form['expense_date']
    description = request.form['expense_desc']
    finance_repo.add_expense(user_id, category_id, amount, date, description)
    flash("Expense added successfully!")
    return redirect('/dashboard')

@app.route('/add-income', methods=['POST'])
def add_income():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    category_id = int(request.form['income_category'])
    amount = float(request.form['income_amount'])
    date = request.form['income_date']
    description = request.form['income_desc']
    finance_repo.add_income(user_id, category_id, amount, date, description)
    flash("Income added successfully!")
    return redirect('/dashboard')

@app.route('/edit-expense/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    if 'user_id' not in session:
        return redirect('/')
    if request.method == 'POST':
        user_id = session['user_id']
        category_id = int(request.form['expense_category'])
        amount = float(request.form['expense_amount'])
        date = request.form['expense_date']
        description = request.form['expense_desc']
        finance_repo.update_expense(expense_id, user_id, category_id, amount, date, description)
        flash("Expense updated successfully!")
        return redirect('/dashboard')
    else:
        # Fetch current data and pass it to form
        return render_template('edit_expense.html', expense_id=expense_id)

@app.route('/edit-income/<int:income_id>', methods=['GET', 'POST'])
def edit_income(income_id):
    if 'user_id' not in session:
        return redirect('/')
    if request.method == 'POST':
        user_id = session['user_id']
        category_id = int(request.form['income_category'])
        amount = float(request.form['income_amount'])
        date = request.form['income_date']
        description = request.form['income_desc']
        finance_repo.update_income(income_id, user_id, category_id, amount, date, description)
        flash("Income updated successfully!")
        return redirect('/dashboard')
    else:
        # Fetch current data and pass it to form
        return render_template('edit_income.html', income_id=income_id)

@app.route('/delete-expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    finance_repo.delete_expense(expense_id, user_id)
    flash("Expense deleted successfully!")
    return redirect('/dashboard')

@app.route('/delete-income/<int:income_id>', methods=['POST'])
def delete_income(income_id):
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    finance_repo.delete_income(income_id, user_id)
    flash("Income deleted successfully!")
    return redirect('/dashboard')

@app.route("/logout", methods=["POST"])
def logout():
    print("Logging out...")  # Debug print
    session.clear()
    return redirect(url_for("show_login"))



if __name__ == '__main__':
    app.run(debug=True) 