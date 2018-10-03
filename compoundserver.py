# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:05:45 2018

@author: Narayana Vadapalli
"""

def compound(amount, rate, compounds_in_year, time):
    multiplier = (1 + (rate / compounds_in_year)) ** (compounds_in_year * time)
    final_amount = amount * multiplier
    interest = final_amount - amount
    

def simple(amount, rate, time):
    sub-interest = amount * rate * time
    final_interest = sub-interest / 100
    final-amount = final_interest + amount
    

@app.route('/compound')
def compound(amount, rate, compounds_in_year, time):
    multiplier = (1 + (rate / compounds_in_year)) ** (compounds_in_year * time)
    final_amount = amount * multiplier
    interest = final_amount - amount
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=111)
