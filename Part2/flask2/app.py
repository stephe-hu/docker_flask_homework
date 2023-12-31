from flask import Flask, request
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/stephe-hu/medicalcodexes-api-mn/main/data/provider012622.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'This is an API service for MN Provider details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/provider/<value>', methods=["GET"])
def provider(value):
    print('value: ', value)
    filtered = df[df['PROVIDER_TYPE_CD'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/provider/<value>/unique/<value2>', methods=["GET"])
def provider2(value, value2):
    filtered = df[df['PROVIDER_TYPE_CD'] == value]
    filtered2 = filtered[filtered['UNIQUE_PROVIDERS'] == value2]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')