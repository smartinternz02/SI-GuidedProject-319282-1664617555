import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<AsEsgpTJTlp2mmXGHzecK7Zbt8j_hRpabb4IKeU_4jLr>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)
@app.route('/')
def helloworld():
    return render_template('index.html')
@app.route('/')
def home():
    return render_template('demo2.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    input_features=[float(x) for x in request.form.values() ]
    features_values=[np.array(input_features)]
    

payload_scoring = {"input_data": [{"field": ['budget','genres','popularity','runtime','vote_average','vote_count','director','release_month','release_DOW'], "values": [[250,	0,	112.672950,	195.0,	7.9,	9176,	245,	7,	0]]}]}

# NOTE: manually define and pass the array(s) of values to be scored in the next line

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/05d2509e-2802-4941-ae0c-d1d846021c48/predictions?version=2022-10-27', json=payload_scoring,
  headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    
    
    pred = response_scoring.json()
    print(pred)
    output = pred['predictions'][0]['values'][0][0]
    print(output)
    print('prediction is', output)
    # showing the prediction results in a UI
    return render_template('resultnew.html',prediction_text=output)

if __name__=="__main__":
    app.run(debug=False)