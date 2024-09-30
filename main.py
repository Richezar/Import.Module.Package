from application.salary import calculate_salary
from application.db.people import get_employees
from pprint import pprint as p
from datetime import date

if __name__ == '__main__':
    print(date.today())
    p(calculate_salary())
    p(get_employees())
