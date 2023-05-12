from flask import Flask
import pandas as pd

df = pd.read_csv('./data/Smallservices.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for MN ICD code details'  
@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/countycode/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    if len(filtered) <= 'anoka':
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.route('/icd/<value>/sex/<value2>')
def icdcode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")   
if __name__ == '__main__':
    app.run(debug=True)