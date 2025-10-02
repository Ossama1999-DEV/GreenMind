"""
utils.py : fonctions utilitaires pour GreenMind
"""

def normalize_sensor_data(temp, humid, light):
    """ Normalise les données capteurs entre 0 et 1 """
    return [
        temp / 40.0,   # température max 40°C
        humid / 100.0, # humidité max 100%
        light / 2000.0 # luminosité max ~2000 lux
    ]
