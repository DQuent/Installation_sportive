class Util_String:

	@staticmethod
	def convertString(phrase):
		"""
        Methode qui permet d'enlever les caractères spéciaux
        """
		phrase = phrase.replace('é','e')
		phrase = phrase.replace('è','e')
		phrase = phrase.replace('ê','e')
		phrase = phrase.replace('à','a')
		phrase = phrase.replace('â','a')
		phrase = phrase.replace('ç','c')
		phrase = phrase.replace('@','a')
		phrase = phrase.replace('ù','u')
		phrase = phrase.replace('û','u')
		phrase = phrase.replace('î','i')
		phrase = phrase.replace('ï','i')
		phrase = phrase.replace('ô','o')
		return phrase

	# Methode fonctionnant sur python2.7 et non sur python3.4 permettant de convertir une string en format Unicode
	#def suppAccent(str):
    #return unicodedata.normalize('NFD', unicode(str,'utf-8')).encode('ascii', 'ignore')
	

