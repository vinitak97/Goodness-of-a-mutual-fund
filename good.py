from flask import request
from flask import jsonify
from flask import Flask
import numpy as np
import pickle


app = Flask(__name__)

#filename=r'C:\Users\VINITA\Desktop\clf.sav'
model=pickle.load(open("clf.sav","rb"))

allparameter = []

@app.route('/evaluation1', methods=['POST'])
def evaluation1():
    parameter1 = request.get_json(force=True)
    return1 = parameter1['return1']
    expense = float(return1)
    allparameter.append(expense)
    if(expense < 0.75):        
        response1 = {
            'reference1': 'Good Mutual fund expense ratios are generally considered to be around 0.50% to 0.75%. So, ' + return1 + ' is a GOOD feature of the scheme.'         
        }
    else:
        response1 = {
            'reference1': 'Good Mutual fund expense ratios are generally considered to be around 0.50% to 0.75%. So, ' + return1 + ' is a BAD feature of the scheme.'         
        }
    return jsonify(response1)

@app.route('/evaluation2', methods=['POST'])
def evaluation2():
    parameter2 = request.get_json(force=True)
    return2 = parameter2['return2']
    sharpe = float(return2)
    allparameter.append(sharpe)
    if(sharpe > 0.0):
        response2 = {
            'reference2': 'Sharpe ratio greater than 0 is considered acceptable to good by investors. Therefore, ' + return2 + ' is a GOOD feature of the scheme.'
        }
    else:
        response2 = {
            'reference2': 'Sharpe ratio greater than 0 is considered acceptable to good by investors. Therefore, ' + return2 + ' is a BAD feature of the scheme.'
        }            
    return jsonify(response2)

@app.route('/evaluation3', methods=['POST'])
def evaluation3():   
    parameter3 = request.get_json(force=True)
    return3 = parameter3['return3']
    sortino = float(return3)
    allparameter.append(sortino)
    if (sortino > 2.0):
        response3 = {
        'reference3': 'A Sortino ratio greater than 2 is consider to be good. So, ' + return3 + ' is a GOOD feature of the scheme.'
        }
    else:
        response3 = {
        'reference3': 'A Sortino ratio greater than 2 is consider to be good. So, ' + return3 + ' is a BAD feature of the scheme.'
        }
    return jsonify(response3)

@app.route('/evaluation4', methods=['POST'])
def evaluation4():    
    parameter4 = request.get_json(force=True)
    return4 = parameter4['return4']
    alpha = float(return4)
    allparameter.append(alpha)
    if (alpha > 0.0):        
        response4 = {
        'reference4': 'An alpha of 1.0 means the fund has outperformed its benchmark index by 1%. Hence, ' + return4 + ' is a GOOD feature of the scheme.'
        }
    else:
        response4 = {
        'reference4': 'An alpha of -1.0 would indicate an under-performance of 1%.. Hence, ' + return4 + ' is a BAD feature of the scheme.'
        }
    return jsonify(response4)

@app.route('/evaluation5', methods=['POST'])
def evaluation5():
    parameter5 = request.get_json(force=True)
    return5 = parameter5['return5']
    beta = float(return5)
    allparameter.append(beta)
    if (beta > 1.0):
        response5 = {
        'reference5': 'A beta of more than 1.0 indicates that the investment\'s price will be more volatile than the market. Therefore, ' + return5 + ' is a GOOD feature of the scheme.'
        }
    else:
        response5 = {
        'reference5': 'A beta of less than 1.0 indicates that the investment will be less volatile than the market. Therefore, ' + return5 + ' is a BAD feature of the scheme.'
        }
    return jsonify(response5)

@app.route('/evaluation6', methods=['POST'])
def evaluation6():    
    parameter6 = request.get_json(force=True)
    return6 = parameter6['return6']
    stddev = float(return6)
    allparameter.append(stddev)
    if (stddev < 15.0):
        response6 = {
        'reference6': 'The standard deviation below 15 shows returns on a fund is less deviating from the expected returns. So, ' + return6 + ' is a GOOD feature of the scheme.'
        }
    else:
        response6 = {
        'reference6': 'The standard deviation above 15 shows returns on a fund is more deviating from the expected returns. So, ' + return6 + ' is a BAD feature of the scheme.'
        }
    return jsonify(response6)

@app.route('/evaluation7', methods=['POST'])
def evaluation7():    
    parameter7 = request.get_json(force=True)
    return7 = parameter7['return7']
    rsquared = float(return7)
    allparameter.append(rsquared)
    if (rsquared >= 85.0):
        response7 = {
        'reference7': 'R-squared value between 85 and 100 has a performance record that is closely correlated to the portfolio\'s returns to the benchmark\'s returns. Hence, ' + return7 + ' is a GOOD feature of the scheme.'
        }
    else:
        response7 = {
        'reference7': 'R-squared value between 85 and 100 has a performance record that is closely correlated to the portfolio\'s returns to the benchmark\'s returns. Hence, ' + return7 + ' is a BAD feature of the scheme.'
        }
    return jsonify(response7)

@app.route('/evaluation8', methods=['POST'])
def evaluation8():    
    parameter8 = request.get_json(force=True)
    return8 = parameter8['return8']
    netreturns = float(return8)
    allparameter.append(netreturns)
    if (netreturns > 10.0):
        response8 = {
        'reference8': 'Net returns of the scheme since inception is considered good if it is grater than 10. So, ' + return8 + ' is a GOOD feature of the scheme.'
        }
    else:
        response8 = {
        'reference8': 'Net returns of the scheme since inception is considered good if it is grater than 10. So, ' + return8 + ' is a BAD feature of the scheme.'
        }        
    return jsonify(response8)

@app.route('/evaluation9', methods=['POST'])
def finaltest():
    sample=[]
    sample.append(allparameter)
    prediction = model.predict(sample)
    predicted = prediction.tolist()
    goodness = predicted[0]
    if (goodness == 1):
        finalresponse = {
         'reference9': 'Overall, this is a GOOD fund scheme.' 
        }   
    else:
        finalresponse = {
         'reference9': 'Overall, this is a BAD fund scheme.' 
        }
    return jsonify(finalresponse)
    
    
    
