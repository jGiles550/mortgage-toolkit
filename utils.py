import json

with open('constants.json', 'r') as file:
    data = json.load(file)

LOAN_TERM_YRS           = data['LOAN_TERM_YRS']
HOMEOWNERS_INSURANCE    = data['HOME_OWNERS_MONTHLY_INSURANCE']
HOA_FEES                = data['HOA_MONTHLY_FEES']
DESIGN_CENTER           = data['DESIGN_CENTER_FEES']
PROPERTY_TAX_RATE       = data['PROPERTY_TAX_RATE']
MORTGAGE_INSURANCE_RATE = data['MORTGAGE_INSURANCE_RATE']

def get_loan_amount(base_price, down_payment):
    return base_price - down_payment


def get_down_payment(base_price, down_payment_percentage):
    return 0.01 * down_payment_percentage * base_price


def get_monthly_interest_rate(interest_rate):
    return interest_rate * (0.01 / 12)


def get_monthly_taxes(base_price):
    return PROPERTY_TAX_RATE * base_price / 12
    

def get_monthly_mortgage_insurance(loan_amt):
    return loan_amt * MORTGAGE_INSURANCE_RATE / 12


def get_monthly_mortgage_payment(loan_term_yrs, interest_rate, loan_amt):
    N = loan_term_yrs * 12
    r = interest_rate * (0.01 / 12)
    P = loan_amt
    mp = (r * P * (1 + r) ** N) / ((1 + r)**N - 1)

    return mp


def interest_rate_buy_down(target_rate, starting_rate, loan_amt):
    irbd = ((starting_rate - target_rate) / 0.25) * 0.01 * loan_amt
    return irbd

