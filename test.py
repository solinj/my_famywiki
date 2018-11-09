import Article as a
import Utilisateur as u
import admi1 as ad

# yolo = a.Article("en cours de validation", "Le Yolo", "le yolo est une expression etc", "langage", "auteur", 2018)
# # self, statut, titre, texte, theme, auteur, date, commentaires="0", liens_click="0"):
# print("yolo")
# yolo.__repr__()

# user = u.Utilisateur("en cours de validation", 1, "mimi", "dupont", "ginette", "gigi@gigi.com", "54321", "2018")
# # statut, role, pseudo, nom, prenom, email, password, date_inscription, u_articles=0, u_commentaires=0, id_photo=0
# #
# user.__repr__()
print("recherche administrateur")
administrator = ad.Administrateur("en cours de validation", 1, "mimi", "dupont", "ginette", "gigi@gigi.com", "54321", "2018")
administrator.__repr__()






# from flask import Flask, render_template
# app = Flask(__name__)
#
#
# @app.route("/")
# def template_test():
#     return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])
#
#
# if __name__ == '__main__':
#     app.run(debug=True)