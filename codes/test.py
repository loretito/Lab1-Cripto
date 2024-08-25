import re 
from collections import Counter
from helpers import expected_frequency, common_connectors

def count_frequency(phrase):
    phrase = phrase.upper()
    frequency = Counter(phrase)
    total_letras = sum(frequency.values())
    
    # Normalizar la frequency en porcentaje
    frequency_porcentaje = {letra: (conteo / total_letras) * 100 for letra, conteo in frequency.items() if letra.isalpha()}
    
    return frequency_porcentaje

# Verificación combinada
def evaluate_consistency(phrase):
    # Verificar frequency de letras
    frequency_phrase = count_frequency(phrase)
    desviacion_total = 0
    for letra, porcentaje in frequency_phrase.items():
        esperado = expected_frequency.get(letra, 0)
        desviacion_total += abs(porcentaje - esperado)
    
    promedio_desviacion = desviacion_total / len(frequency_phrase)
    
    # Verificar conectores en la phrase
    phrase_limpia = re.sub(r'[^\w\s]', '', phrase).lower()
    palabras = set(phrase_limpia.split())
    conectores_encontrados = palabras.intersection(common_connectors)
    porcentaje_conectores = (len(conectores_encontrados) / len(palabras)) * 100 if len(palabras) > 0 else 0
    
    if promedio_desviacion < 5 and porcentaje_conectores > 20: 
        return True
    else:
        return False

# Ejemplos
phrase_1 = "criptografia y seguridad en redes"
phrase_2 = "no se que colocar"

print(evaluate_consistency(phrase_1))

print(evaluate_consistency(phrase_2))

