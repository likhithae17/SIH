import pandas as pd
from flask import Flask, jsonify, request
import pickle
import json

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    outputs = []
    
    data = request.get_json(force=True)
    yr = data['Year']
    
    for i in range(yr, yr + 5):
        data = {'Year':i}
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)
        result = model.predict(data_df)
        output = {i: int(result[0])}
        outputs.append(output)
    return jsonify(results=outputs)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
