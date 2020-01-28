import pymongo
from pymongo import MongoClient

import ipl2020
client = MongoClient('mongodb+srv://dhi_user:dhi_user@cluster0-vc51s.mongodb.net/test?retryWrites=true&w=majority')
db = client['IPL_2020']
teams = db['team']
players = db['players']


def teamslist():
    teamslist = []
    teamList = teams.find({},{"_id":0,"label":1})
    for team in teamList:
        teamslist.append(team['label'])
    return teamslist

def playelist(team):
    playerslist = []
    playerList = players.find({"label":team,},{"_id":0})
    for player in playerList:
        playerslist.append(player)
    return playerslist

def playerChart(team):
    playerschart = []
    playerdata = players.find({"label":team},{"_id":0,"player":1,"price":1})
    for chartdata in playerdata:
        playerschart.append(chartdata)
    return playerschart


def totalPlayers():
    total_playerslist = []
    total_playerList = players.find({},{"_id":0})
    for player in total_playerList:
        total_playerslist.append(player)
    return total_playerslist


def overallplayerChart():
    overallplayerschart = []
    overallplayerdata = players.find({},{"_id":0,"player":1,"price":1})
    for chartdata in overallplayerdata:
        overallplayerschart.append(chartdata)
    return overallplayerschart

# playerChart('CSK')
