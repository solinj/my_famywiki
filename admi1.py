class Administrateur:

    id = 0
    def __init__(self,pseudo, nom, prenom, email, password):

        self.pseudo = pseudo
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.email = email
        self.id += 1


    def getId(self):
        return self.id

    def getPseudo(self):
        return self.pseudo

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getEmail(self):
        return self.email


    def setPseudo(self, pseudo):
        self.pseudo = pseudo

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setEmail(self, email):
        self.email = email



    def __repr__(self):
        print("pseudo : " + self.getPseudo())
        print("prenom : " + self.getPrenom())
        print("nom : " + self.getNom())
        print("email : " + self.getEmail())



    def createAdmi(self):
        pass

    def deleteAdmi(self):
        pass

    def editAdmi(self):
        pass

    def validateAdmi(self):
        pass

# class Administrators (Utilisateur)
# # 	def manage(self)
# # 		print ("je suis l'administrateur")
# # root = Admin(1, 'root', 'toor')
# # root.check_password('toor')
# # True
# # root.manage()
# # I am an über administrator!
# # john = User(2, 'john', '12345')
# # john.manage()
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # AttributeError: 'User' object has no attribute 'manag