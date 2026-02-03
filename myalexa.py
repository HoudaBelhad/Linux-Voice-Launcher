import os
import sys
import time
import speech_recognition as sr

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def notifier(message):
    os.system(f'notify-send "Assistant Vocal" "{message}" -i microphone-sensitivity-medium')

def executer_commande(vocal_input):
    commandes = {
        "brave": ["brave", "brothers", "brother", "navigateur"],
        "obsidian": ["obsidian", "notes", "obsidienne"],
        "vscode": ["code", "visual studio", "studio code", "éditeur"]
    }
    
    executables = {
        "brave": "brave-browser",
        "obsidian": "flatpak run md.obsidian.Obsidian",
        "vscode": "code"
    }
    
    texte_recu = vocal_input.lower()
    for app, declencheurs in commandes.items():
        if any(mot in texte_recu for mot in declencheurs):
            os.system(f"{executables[app]} &")
            notifier(f"Lancement de {app.upper()}")
            return True
    return False

r = sr.Recognizer()
debut_programme = time.time()
commande_reussie = False

with sr.Microphone() as source:
    notifier("Je t'écoute, tu peux parler...")
    
    while (time.time() - debut_programme) < 20:
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            temps_restant = 20 - (time.time() - debut_programme)
            if temps_restant <= 0: break
            
            print(f"Écoute en cours... (Temps restant : {int(temps_restant)}s)")
            audio = r.listen(source, timeout=temps_restant, phrase_time_limit=4)
            phrase = r.recognize_google(audio, language="fr-FR")
            
            if executer_commande(phrase):
                commande_reussie = True
                break 
            else:
                notifier(f"Pas compris '{phrase}', réessaie...")
                
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            
            if (time.time() - debut_programme) < 20:
                notifier("Je n'ai pas entendu, je réécoute...")
            continue 
        except Exception as e:
            print(f"Erreur : {e}")
            break

if not commande_reussie:
    notifier("Temps écoulé, arrêt de l'assistant.")
