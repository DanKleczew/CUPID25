EMAIL_TEST = "Dan.Kleczewski1@etu.univ-paris1.fr"


def send_email(*args: int) -> bool:
    """
    Le mail est toujours envoyé à l'adresse mail de Herbaut (ou autre
    hein pour les tests, on va pas vraiment envoyer un mail à herbaut à chaque fois
    qu'on fait un test. Cette adresse mail est gardée dans une CONSTANTE).
    Il y a un fichier qui mappe chaque ID d'action avec un titre et une partie variable du mail.
    Le reste du contenu du mail est tout le temps pareil et aussi défini dans un fichier.
    Args:
        *args : les IDs de chacune des actions réalisées en lien avec l'évènement qui demande un envoi de mail
    Returns:
        bool : success
    """
    return False


def open_shutter() -> bool:
    """
    Ouvre le volet. Raise une exception si il est déjà ouvert.
    Returns:
        bool : success
    """
    return False

def close_shutter() -> bool:
    """
    Ferme le volet. Raise une exception si il est déjà fermé.
    Returns:
        bool : success
    """
    return False


def turn_lamp_on() -> bool:
    """
    Allume la lampe. Raise une exception si elle est déjà allumée.
    Returns:
        bool : success
    """
    return False

def turn_lamp_off() -> bool:
    """
    Éteint la lampe. Raise une exception si elle est déjà éteinte.
    Returns:
        bool : success
    """
    return False

def turn_music_on() -> bool:
    """
    Démarre la musique (LAQUELLE ? SUR QUEL MATÉRIEL ?) Raise une exception si elle joue déjà.
    Returns:
        bool : success
    """
    return False

def turn_music_off() -> bool:
    """
    Arrête la musique. Raise une exception si elle ne joue pas.
    Returns:
        bool : success
    """
    return False

def text_to_speech(text: str) -> bool:
    """
    Args:
        text: Chaîne de charactères du texte à dire
    Returns:
        bool : success
    """
    return False