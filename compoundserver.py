# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:05:45 2018

@author: Narayana Vadapalli
"""

import psycopg2
import requests
from flask import Flask, redirect, render_template, request, url_for, session, make_response
from flask_login import login_required, login_user, LoginManager, logout_user, UserMixin
import random
import os

app = Flask(__name__)
    

def simple(amount, rate, time):
    sub-interest = amount * rate * time
    final_interest = sub-interest / 100
    final-amount = final_interest + amount
    

@app.route('/compound', methods=['POST'])
def compound(amount, rate, compounds_in_year, time):
    amount = request.form.get('principalbox')
    rate = request.form.get('annualbox')
    compounds_in_year = request.form.get('compound')
    time = request.form.get('year')
    multiplier = (1 + (rate / compounds_in_year)) ** (compounds_in_year * time)
    final_amount = amount * multiplier
    interest = final_amount - amount
    return render_template('calculator.html')
    

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=111)
