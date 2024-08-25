common_connectors = set([
    # Conjunciones
    "y", "e", "o", "u", "ni", "pero", "aunque", "sino", "mas", "sin embargo", 
    "porque", "ya que", "puesto que", "a fin de que", "para que", "de manera que",
    "mientras", "cuando", "antes de", "despues de", "hasta que", "donde", "como",
    
    # Adverbios y frases adverbiales
    "ademas", "tambien", "incluso", "sin embargo", "por lo tanto", 
    "por consiguiente", "entonces", "asi que", "por eso", "por otra parte", 
    "de hecho", "en cambio", "por ejemplo", "no obstante", "a pesar de", 
    "en consecuencia", "al contrario", "de modo que", "en resumen", 
    "en conclusión", "por un lado", "por otro lado", "es decir", "o sea", 
    "debido a", "gracias a", "a causa de", "en cuanto", "con respecto a", 
    "en relación con", "hasta que", "si bien", "tal vez", "quizas", 
    "en realidad", "por supuesto", "claro que", "obviamente",
    
    # Preposiciones
    "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", 
    "durante", "en", "entre", "hacia", "hasta", "mediante", "para", 
    "por", "según", "sin", "sobre", "tras", "versus", "via",
    
    # Artículos
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    
    # Pronombres
    "yo", "tu", "el", "ella", "nosotros", "nosotras", "vosotros", "vosotras", 
    "ellos", "ellas", "me", "te", "se", "nos", "os", "mi", "ti", "si", 
    "mi", "tu", "su", "nuestro", "nuestra", "vuestro", "vuestra", "mio", 
    "tuyo", "suyo", "nuestro", "vuestro", "este", "esta", "estos", 
    "estas", "ese", "esa", "esos", "esas", "aquel", "aquella", 
    "aquellos", "aquellas", "lo",
    
    # Otros
    "que", "como", "donde", "cuando", "cual", "quien", "cuanto",  
    "porque", "por que", "si", "no", "muy", "mas" "menos", 
    "ya", "aun", "todavia", "nunca", "siempre", "tambien", "tampoco",
    "casi", "poco", "mucho", "varios", "algunos", "ninguno", 
    "cada", "ambos", "todo", "otro", "igual", "distinto", "cierto"
])


expected_frequency = {
    'E': 13.68, 'A': 12.53, 'O': 8.68, 'S': 7.98, 'R': 6.87,
    'N': 6.71, 'I': 6.25, 'L': 4.97, 'D': 4.67, 'C': 3.87,
    'T': 4.63, 'U': 3.93, 'M': 3.15, 'P': 2.51, 'B': 1.49,
    'V': 1.05, 'Y': 1.01, 'Q': 0.88, 'H': 0.71, 'G': 0.69,
    'F': 0.69, 'Z': 0.52, 'J': 0.44, 'Ñ': 0.31, 'X': 0.14,
    'K': 0.00, 'W': 0.00
}