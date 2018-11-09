from flask import render_template
import datetime as d
from flask import Flask, request, jsonify
import mongo
import math
# import multi
#import logger
import flask
import flask_pymongo as fp
import os
import json
import bson as bo
import glob
#from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Famywiki_Articles' # name of database on mongo
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/Famywiki_Articles"
mongo = fp.PyMongo(app)



@app.route("/", methods=["GET"])
def accueil():
    #ACCUEIL
    # cursor = mongo.db.monuments.find({"REG":"Alsace"})
    cursor = list(mongo.db.articles.find({"thème":"Autres"}))
    #return render_template("accueil.html")
    return render_template('template.html', data = cursor)

@app.route("/recherche_article/", methods=["GET", "POST"])
def recherche_article():
    if request.method == 'POST':
        print("POST RECHERCHE ARTICLE")
        print(request.form['motcle'])
        format_input = request.form['theme'].lower()
        result_by_theme = list(mongo.db.articles.find({"thème":request.form['theme']}))
        result_by_key_word = list(mongo.db.articles.find({"thème":request.form['theme']}))
        marqueur = "ok"
        return render_template('HTML_BarreRecherche.html', data = result_by_key_word, src = marqueur)
    else:
        print("GET RECHERCHE ARTICLE")
        return render_template('HTML_BarreRecherche.html')
    #return render_template("themes.html")


@app.route("/article/", methods=["GET", "POST"])
def show_article():
    return render_template("show_article.html")
    pass
    # if request.method == 'POST':
    #     print(request.form['mot_cle'])
    #     format_input = request.form['theme'].lower()
    #     result_by_theme = list(mongo.db.articles.find({"theme":request.form['theme']}))
    #     result_by_key_word = list(mongo.db.articles.find({"titre":request.form['mot_cle']}))
    #     return render_template('template.html', data = result_by_key_word)
    # else:
    #     return render_template('HTML_BarreRecherche.html')



# @app.route("/fiche/", methods=["GET", "POST"])
# def fillFiche():
#     source = ""
#     if request.method == 'POST':
#         if (fin.finalFunc(request.form['user_name'], request.form['user_prenom'])):
#             source = "ok"
#             return render_template('confirm.html')
#         else:
#                 # flash(u"rentrer donnees valides", 'error')
#             source = "ko"
#             return render_template('form_fp.html', src=source)
#     return render_template('form_fp.html', src=source)




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