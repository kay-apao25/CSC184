#from flask import Flask, render_template, request
#from account import Account
#from bank import Bank
#app = Flask(__name__)


#@app.route('/') 
#def hello_world():
  # account_number = request.args.get('account_number')  
   #balance = BANK.get_account_balance(account_number)
#   return render_template('about.html')

from lettuce import *
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
	world.browser = webdriver.Firefox()

@after.all
def teardown_browser(total):
    world.browser.quit()
