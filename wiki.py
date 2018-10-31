from flask import render_template
import datetime as d
from flask import Flask, request, jsonify
import mongo
import math
# import multi
import logger
import flask
import flask_pymongo as fp
import os
import json
import bson as bo
import glob
#from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'wiki' # name of database on mongo
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/wiki"
mongo = fp.PyMongo(app)



@app.route("/", methods=["GET"])
def one_request():
    print("SOMETHING")
    # cursor = mongo.db.monuments.find({"REG":"Alsace"})
    cursor = list(mongo.db.monuments.find({"REG":"Alsace"}))
    print("after mongo")

    return render_template('template.html' , data = cursor)
    # , data = cursor
    # return render_template('template.html', ip_address=(jsonify({'ip_address': request.remote_addr}), 200))
    # print((jsonify({'ip_address': request.remote_addr}), 200))
    # return jsonify({'ip_address': request.remote_addr}), 200
    # var_brow = request.user_agent.browser
    # var_nav = request.headers.get('User-Agent')
    # var_os = request.user_agent.platform
    # var_ip = request.environ.get('ip_address', request.remote_addr)
    # our_date = d.datetime.now().strftime("%A %d %B %Y %H %M")
    # with open("journal.co", "a") as fo:
    #     writing = "--date : " + our_date + "\n" + "--informations = " + "\n" + "--browser : " + str(var_brow) + "\n" + "--navigateur : " + str(var_nav) + "\n" + "--os : " + str(var_os) + "\n" + "--adresse_ip : " + str(var_ip)
    #     fo.write(str(writing))
    # return render_template('template.html', ip_address = var_ip, nav = var_nav, brow = var_brow, oos = var_os)

@app.route("/journal")
def printInfos():
    with open("journal.co", "r") as f:
        return render_template('template.html', lines = f)



if __name__ == '__main__':
    app.run(debug=True)