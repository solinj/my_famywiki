

class Utilisateur:
    #id variable incrémentable
    id = 0
    def __init__(self, statut, role, pseudo, nom, prenom, email, password, date_inscription, u_articles=0, u_commentaires=0, id_photo=0):
        self.statut = statut
        self.role = role
        self.pseudo = pseudo
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.email = email
        self.date_inscription = date_inscription
        self.u_articles = u_articles
        self.u_commentaires = u_commentaires
        self.id_photo = id_photo
        self.id += 1


    def getId(self):
        return self.id

    def getStatut(self):
        return self.statut

    def getRole(self):
        return self.role

    def getPseudo(self):
        return self.pseudo

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getEmail(self):
        return self.email

    def getDateInscription(self):
        return self.date_inscription

    def getUArticles(self):
        return self.u_articles

    def getUCommentaires(self):
        return self.u_commentaires

    def getIdPhoto(self):
        return self.id_photo




    def setStatut(self, statut):
        self.statut = statut

    def setRole(self, role):
        self.role = role

    def setPseudo(self, pseudo):
        self.pseudo = pseudo

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setEmail(self, email):
        self.email = email

    def setDateInscription(self, date_inscription):
        self.date_inscription = date_inscription

    def setUArticles(self, u_articles):
        self.u_articles = u_articles

    def setUCommentaires(self, u_commentaires):
        self.u_commentaires = u_commentaires

    def setIdPhoto(self, id_photo):
        self.id_photo = id_photo



    def __repr__(self):
        print("statut : " + self.getStatut())
        print("role : " + str(self.getRole()))
        print("pseudo : " + self.getPseudo())
        print("prenom : " + self.getPrenom())
        print("nom : " + self.getNom())
        print("email : " + self.getEmail())
        print("id_photo : " + str(self.getIdPhoto()))
        print("contributions articles : " + str(self.getUArticles()))
        print("contributions commentaires : " + str(self.getUCommentaires()))
        print("date inscription : " + str(self.getDateInscription()))


    def createUser(self):
        pass

    def deleteUser(self):
        pass

    def editUser(self):
        pass

    def validateUser(self):
        pass