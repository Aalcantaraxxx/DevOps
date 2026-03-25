#Traductor de  3 idiomas, 10 palabras cada uno, español, inglés y francés
print("Bienvenido al traductor de español, inglés y francés")
palabras = {
    "hola": {"ingles": "hello", "frances": "bonjour"},
    "adiós": {"ingles": "goodbye", "frances": "au revoir"},
    "gracias": {"ingles": "thank you", "frances": "merci"},
    "por favor": {"ingles": "please", "frances": "s'il vous plaît"},
    "lo siento": {"ingles": "sorry", "frances": "pardon"},
    "sí": {"ingles": "yes", "frances": "oui"},
    "no": {"ingles": "no", "frances": "non"},
    "amigo": {"ingles": "friend", "frances": "ami"},
    "familia": {"ingles": "family", "frances": "famille"},
    "comida": {"ingles": "food", "frances": "nourriture"}
}

palabra = input("Ingrese una palabra en español para traducir: ").lower()
if palabra in palabras:
    traduccion_ingles = palabras[palabra]["ingles"]
    traduccion_frances = palabras[palabra]["frances"]
    print(f"La traducción de {palabra} en inglés es: {traduccion_ingles}")
    print(f"La traducción de {palabra} en francés es: {traduccion_frances}")
else:    
    print(f"La palabra {palabra} no se encuentra en el diccionario de traducción.")

 