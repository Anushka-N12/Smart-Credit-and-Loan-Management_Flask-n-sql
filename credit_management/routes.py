from flask import Blueprint, jsonify
from credit_management.service import add_loan,get_loan_by_id,get_loans_by_borrowers_id,get_all_loans,get_credit_limit,get_paymentdetails,loan_repayment
from credit_management.service import add_borrower
from datetime import date
import json

credit_management_bp = Blueprint('credit_management', __name__)

@credit_management_bp.route('/loans/process', methods=['POST'])
def add_loan_process(json_data):
    #Preparing data
    borrower_id, loan_amount = json_data['borrowerId'], json_data['loanAmount']
    loan_date = date.today()
    #Checking history
    loans = json.loads(get_loans_by_borrowers_id_def(borrower_id))['loans']
    
    if loans == None:
        #For new user
        add_borrower(borrower_id)
        loans = add_loan(borrower_id, loan_amount, loan_date)
        return jsonify(loans)
    else: 
        #Check for defaulted payments
        defaulter = False
        for row in loans:
            if (row[5] == 'Not Paid') and (row[6] < loan_date): #
                #If repayment date is crossed & not one yet
                defaulter = True
        if defaulter == False:
            #Check credit_limit
            credit_info = json.load(get_credit_limit_def(borrower_id))['limit_info']
            if credit_info[3] >= loan_amount:
                loans = add_loan(borrower_id, loan_amount, loan_date)
                return jsonify(loans)
            else:
                return jsonify({"message": "Loan amount above allowed credit limit", "status": "unsuccessful"})
        else: 
            return jsonify({"message": "Repayment not done on time", "status": "unsuccessful"})
        

@credit_management_bp.route('/loans/:id', methods=['GET'])
def get_loan_by_id_def(loan_id):
    loan = get_loan_by_id(loan_id)
    return jsonify(loan)

@credit_management_bp.route('/loans/borrowers/:id', methods=['GET'])
def get_loans_by_borrowers_id_def(borrowers_id):
    loans = get_loans_by_borrowers_id(borrowers_id)
    return jsonify(loans)

@credit_management_bp.route('/loans', methods=['GET'])
def get_all_loans_def():
    loans = get_all_loans()
    return jsonify(loans)

@credit_management_bp.route('/loans/creditlimit/:id', methods=['GET'])
def get_credit_limit_def(borrowers_id):
    limit = get_credit_limit(borrowers_id)
    return jsonify(limit)

@credit_management_bp.route('/loans/paymentdetails/:id', methods=['GET'])
def get_paymentdetails_def(loan_id):
    payments = get_paymentdetails(loan_id)
    return jsonify(payments)

@credit_management_bp.route('/loans/paymentdetails/:id/repayment', methods=['POST'])
def loan_repayment_def(loan_id):
    loans = loan_repayment(loan_id)
    return jsonify(loans)