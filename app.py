from flask import Flask, render_template,request
import pickle
import pandas as pd
import numpy as np
from functions import popular_df,recommend

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html',df = (popular_df))

# @app.route('/book_recommendation',methods=['GET','POST'])
# def book_recommendation():
#     book = request.form.get('book')
#     data = recommend(book)
#     return render_template('recommend.html',data=data)

if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0')
