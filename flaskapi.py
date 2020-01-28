import pymongo
from pymongo import MongoClient
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import ipl2020



app = Flask(__name__)
CORS(app)

@app.route('/teams')
def teamList():
    response = jsonify({'Teams':ipl2020.teamslist()})
    return response

@app.route('/playerlist/<label>')
def players(label):
    response = jsonify({'teamPlayers':ipl2020.playelist(label)})
    return response

@app.route('/playerchartdata/<label>')
def playerchartData(label):
  
    response = jsonify({'playerchart':ipl2020.playerChart(label)})
    return response

@app.route('/all')
def totalplayerList():
    response = jsonify({'overallteamPlayers':ipl2020.totalPlayers()})
    return response

@app.route('/overallchartdata')
def overallchartData():
    response = jsonify({'overallplayerschart':ipl2020.overallplayerChart()})
    return response
    

if __name__ == "__main__":
    app.run(host= '192.168.10.105',port=8080,debug=True)










