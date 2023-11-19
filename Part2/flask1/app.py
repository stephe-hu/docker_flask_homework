from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/stephe-hu/azure_flask_deployment/main/data/covid_deaths.csv')

@app.route('/')
def data(data=df):
    data = data.sample(15)
    return render_template('index.html', data=data)


if __name__=='__main__':
    app.run(debug=True)