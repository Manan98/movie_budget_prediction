from flask.ext.cors import CORS
import json
import numpy as np
import pickle

from flask import Flask, request
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route('/get_data', methods=['POST'])
def getdata():


    g = request.form.get('genre')
    ps=request.form.get('predictedScore')
    re = request.form.get('revenue')
    ru = request.form.get('runtime')

    map=np.genfromtxt('list_of_genres.csv',delimiter=',')
    for i in range(19):
        if(g==map[i][1]):
            g=map[i][0]
    result=compute_budget(g,ps,re,ru)
    print(result)
    return (str)(result)

def compute_budget(g, ps, re, ru):
    test = np.array([g, ps, re, ru])
    test.reshape(4,1)
    filename = 'finalized_model.sav'
    knn = pickle.load(open(filename, 'rb'))
    result = knn.predict(test)
    print(result)
    return result

if __name__=="__main__":
    app.run("0.0.0.0", port=5100)
