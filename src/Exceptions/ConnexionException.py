class ConnexionException(Exception):

    def __init__(self,raison):
        self.raison = raison
    
    def __str__(self):
        return self.raison

