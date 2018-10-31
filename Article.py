

class Article:
    #id variable incrémentable
    id = 0
    def __init__(self, statut, titre, texte, theme, auteur, date, commentaires="0", liens_click=0):
        self.statut = statut
        self.titre = titre
        self.texte = texte
        self.theme = theme
        self.auteur = auteur
        self.date = date
        self.commentaires = commentaires
        self.liens_click = liens_click
        self.id += 1


    def getId(self):
        return self.id

    def getStatut(self):
        return self.statut

    def getTitre(self):
        return self.titre

    def getTexte(self):
        return self.texte

    def getTheme(self):
        return self.theme

    def getAuteur(self):
        return self.auteur

    def getDate(self):
        return self.date

    def getCommentaires(self):
        return self.commentaires

    def getLiensClick(self):
        return self.liens_click



    def setStatut(self, statut):
        self.statut = statut

    def setTitre(self, titre):
        self.titre = titre

    def setTexte(self, texte):
        self.texte = texte

    def setTheme(self, theme):
        self.theme = theme

    def setAuteur(self, auteur):
        self.auteur = auteur

    def setDate(self, date):
        self.date = date

    def setCommentaires(self):
        return self.commentaires

    def setLiensClick(self):
        return self.liens_click


    def __repr__(self):
        print("statut : " + self.getStatut())
        print("titre : " + self.getTitre())
        print("texte : " + self.getTexte())
        print("theme : " + self.getTheme())
        print("auteur : " + self.getAuteur())
        print("date : " + str(self.getDate()))
        print("commentaires : " + self.getCommentaires())
        print("Liens cliquables " + str(self.getLiensClick()))


    def createArticle(self):
        pass

    def deleteArticle(self):
        pass

    def editArticle(self):
        pass

    def searchArticle(self):
        pass

    def commentArticle(self):
        pass

    def validateArticle(self):
        pass

#     def __str__()
#         def __repr__()
# # pour représenter un courrier