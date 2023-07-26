from database import get_db_connection
import numpy as np

my_cursor = get_db_connection().cursor()

def add_loan(borrower_id, loan_amount, loan_date):
    #Setting id 
    my_cursor.execute('SELECT id FROM loan ORDER BY id DESC LIMIT 1') + 1
    id = my_cursor.fetchone()[0]
    #Addning loan
    my_cursor.execute(f'INSERT INTO loan VALUES ({id}, {borrower_id}, {loan_amount}, {loan_date}, null, \'Not Paid\', {str(np.datetime64(loan_date)+np.timedelta64(1, 'M'))});')
    #Changing credit_limit info
    limit_info = get_credit_limit(borrower_id)['limit_info']
    my_cursor.execute(f'UPDATE credit_limit SET remaining_amount = {limit_info[3]-loan_amount}, used_amount = {limit_info[4]+loan_amount} WHERE borrower_id = {borrower_id}')

    return {"message": "Loan application approved and transaferred", "status": "success"}

def get_loan_by_id(loan_id):
    my_cursor.execute(f'SELECT * FROM loan WHERE id == \'{loan_id}\'')
    loan = my_cursor.fetchone()
    loans = {"loan_info": loan}
    
    return loans

def get_loans_by_borrowers_id(borrowers_id):
    my_cursor.execute(f'SELECT * FROM loan WHERE borrower_id == \'{borrowers_id}\'')
    loans = my_cursor.fetchall()
    loans = {"loans": loans}
    
    return loans

def get_all_loans():
    my_cursor.execute('SELECT * FROM loan')
    loans = my_cursor.fetchall()
    loans = {"all_loans": loans}
    
    return loans

def get_credit_limit(borrowers_id):
    my_cursor.execute(f'SELECT * FROM credit_limit WHERE borrower_id == \'{borrowers_id}\'')
    limit = my_cursor.fetchone()
    limit_info = {"limit_info": limit}
    
    return limit_info

def get_paymentdetails(loan_id):
    my_cursor.execute(f'SELECT * FROM payment_transaction WHERE loan_id == {loan_id}')
    payments = my_cursor.fetchall()
    payments = {"payments": payments}
    
    return payments

def loan_repayment(loan_id):
    
    loans = {"name": "test"}
    
    return loans
    
def add_borrower(borrower_id):
    my_cursor.execute('SELECT id FROM credit_limit ORDER BY id DESC LIMIT 1') + 1
    id = my_cursor.fetchone()[0]
    my_cursor.execute(f'INSERT INTO credit_limit VALUES ({id}, {borrower_id}, 5000, 5000, 0);')
