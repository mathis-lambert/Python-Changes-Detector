from cx_Freeze import setup, Executable

base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("Lextan_URL_Teams.py", copyright="Copyright (C) 2022 Lextan", base=base, icon="C:/Users/Mathis/Desktop/fetch_url/icon.ico", shortcutName="Lextan_URL_Teams", shortcutDir="Lextan.exe")]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "URL_Checker_Lextan",
    options = options,
    version = "1.6",
    description = 'Récuperer URL du fichier json pour ouvrir le lien teams mis a jour',
    executables = executables
)