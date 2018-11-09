import Utilisateur as u
# class Personne:
#     """Classe représentant une personne"""
#
#     def __init__(self, nom):
#         """Constructeur de notre classe"""
#         self.nom = nom
#         self.prenom = "Martin"
#
#     def __str__(self):
#         """Méthode appelée lors d'une conversion de l'objet en chaîne"""
#         return "{0} {1}".format(self.prenom, self.nom)
#
#
# class AgentSpecial(Personne):
#     """Classe définissant un agent spécial.
#     Elle hérite de la classe Personne"""
#
#     def __init__(self, nom, matricule):
#         """Un agent se définit par son nom et son matricule"""
#         # On appelle explicitement le constructeur de Personne :
#         Personne.__init__(self, nom)
#         self.matricule = matricule
#
#     def __str__(self):
#         """Méthode appelée lors d'une conversion de l'objet en chaîne"""
#         return "Agent {0}, matricule {1}".format(self.nom, self.matricule)






class Administrateur(u.Utilisateur):

    id = 0
    def __init__(self, statut, role, pseudo, nom, prenom, email, password, date_inscription, u_articles=0, u_commentaires=0, id_photo=0):
        u.Utilisateur.__init__(self, statut, role, pseudo, nom, prenom, email, password, date_inscription, u_articles=0, u_commentaires=0, id_photo=0)
        self.id += 1


    # def getId(self):
    #     return self.id
    #
    # def getPseudo(self):
    #     return self.pseudo
    #
    # def getNom(self):
    #     return self.nom
    #
    # def getPrenom(self):
    #     return self.prenom
    #
    # def getEmail(self):
    #     return self.email
    #
    #
    # def setPseudo(self, pseudo):
    #     self.pseudo = pseudo
    #
    # def setNom(self, nom):
    #     self.nom = nom
    #
    # def setPrenom(self, prenom):
    #     self.prenom = prenom
    #
    # def setEmail(self, email):
    #     self.email = email

    #
    #
    # def __repr__(self):
    #     print("pseudo : " + self.getPseudo())
    #     print("prenom : " + self.getPrenom())
    #     print("nom : " + self.getNom())
    #     print("email : " + self.getEmail())



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