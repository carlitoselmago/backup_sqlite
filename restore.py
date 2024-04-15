import os
import shutil

def substitueix_base_dades():
    # Camí al directori de còpies de seguretat
    backup_dir = './backups'
    
    # Llista tots els fitxers en el directori de còpies de seguretat
    fitxers_backup = sorted(os.listdir(backup_dir))
    
    # Mostra els fitxers de còpia de seguretat a l'usuari
    print("Fitxers de còpia de seguretat disponibles:")
    for index, fitxer in enumerate(fitxers_backup):
        print(f"{index + 1}: {fitxer}")
    
    print("**************************")
    print("RESTORE APP")
    print("**************************")

    # Obté el arxiu seleccionat
    eleccio = int(input("Introdueix el número del fitxer que vols restaurar: "))
    
    # Obté el fitxer de còpia de seguretat seleccionat
    fitxer_seleccionat = fitxers_backup[eleccio - 1]
    
    # Camí al fitxer de dades de destinació
    fitxer_destinacio = './data.db'
    
    # Elimina el fitxer data.db existent si existeix
    if os.path.exists(fitxer_destinacio):
        os.remove(fitxer_destinacio)
    
    # Copia i canvia el nom del fitxer de còpia de seguretat seleccionat a data.db
    shutil.copy(os.path.join(backup_dir, fitxer_seleccionat), fitxer_destinacio)
    print(f"Base de dades restaurada correctament des de {fitxer_seleccionat}.")


substitueix_base_dades()
