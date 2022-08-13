from flask import Flask, render_template, redirect, request, url_for, flash, session
from snowflake_client import *
from datetime import datetime

TODAYS_DATE = str(datetime.today()).split('.')[0]

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)