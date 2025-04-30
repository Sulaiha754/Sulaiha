import pytest
from dao.financerepoimpl import FinanceRepoImpl

@pytest.fixture(scope="module")
def repo():
    return FinanceRepoImpl()

def test_add_user_and_get_all_users(repo):
    repo.add_user("testuser1", "testpass", "test1@example.com")
    users = repo.get_all_users()
    assert any(user.email == "test1@example.com" for user in users) or any("test1@example.com" in str(user) for user in users)

def test_add_income_category(repo):
    repo.add_income_category("Testing Income")
    categories = repo.get_income_categories()
    assert any("Testing Income" in str(cat) for cat in categories)

def test_add_expense_category(repo):
    repo.add_expense_category("Testing Expense")
    categories = repo.get_expense_categories()
    assert any("Testing Expense" in str(cat) for cat in categories)

def test_add_income(repo):
    user_id = 1  # Make sure this exists
    category_id = repo.get_income_category_id_by_name("Testing Income")
    repo.add_income(user_id, category_id, 1500.0, "2025-04-30", "Test income add")
    income_data = repo.get_user_income(user_id)
    assert any("Test income add" in str(row) for row in income_data)

def test_add_expense(repo):
    user_id = 1  # Ensure this user exists
    category_id = repo.get_expense_category_id_by_name("Testing Expense")
    repo.add_expense(user_id, category_id, 500.0, "2025-04-30", "Test expense add")
    expense_data = repo.get_user_expenses(user_id)
    assert any("Test expense add" in str(row) for row in expense_data)

def test_get_income_report(repo):
    result = repo.get_income_report(1)
    assert isinstance(result, float)

def test_get_expense_report(repo):
    result = repo.get_expense_report(1)
    assert isinstance(result, float)

def test_get_all_income(repo):
    data = repo.get_all_income(1)
    assert isinstance(data, list)

def test_get_all_expense(repo):
    data = repo.get_all_expense(1)
    assert isinstance(data, list)
