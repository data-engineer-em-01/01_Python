# File

## Introduction :

La manipulation de fichiers est une tâche courante en programmation, et Python offre de puissantes fonctionnalités pour travailler avec des fichiers de divers types. 

## 1. Gestionnaire de contexte (Context Manager) :

Python offre une syntaxe concise pour travailler avec des fichiers en utilisant des gestionnaires de contexte : `with`. 

Cela garantit que les ressources liées au fichier sont correctement libérées après leur utilisation, même en cas d'erreur. Voici un exemple :

```python
with open("dataset.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
# À ce stade, le fichier est automatiquement fermé, même en cas d'erreur.
```

:rocket: Vous pouvez également gérer les exceptions.

```python
try:
    # Tentative d'ouvrir le fichier
    with open("dataset.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    # Si le fichier n'est pas trouvé, cette exception est gérée ici
    print("Le fichier spécifié n'existe pas.")

```

## 2. Modes d'ouverture de fichiers :

Python offre plusieurs modes d'ouverture de fichiers, selon le type d'opération que vous souhaitez effectuer. Les modes courants incluent :

- `"r"` : Lecture seule.
- `"w"` : Écriture (crée un nouveau fichier ou écrase le fichier existant).
- `"a"` : Ajout (ajoute du contenu à la fin du fichier).
- `"rb"`, `"wb"`, `"ab"` : Ouvrir le fichier en mode binaire (lecture, écriture, ajout).

## 3. Lecture et écriture de fichiers :

- Lecture de tout le contenu d'un fichier :

```python
with open("dataset.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

- Lecture de lignes individuelles :

```python
with open("dataset.txt", "r") as f:
    lignes = f.readlines()
    for ligne in lignes:
        print(ligne)
```

- Écriture dans un fichier :

```python
with open("nouveau_fichier.txt", "w") as f:
    f.write("Bonjour, monde !")
```

## 4. Manipulation de fichiers CSV :

Les fichiers CSV (Comma-Separated Values) sont couramment utilisés pour stocker des données tabulaires, données semi-structurées. Python offre des modules tels que `csv` pour simplifier la manipulation de ces fichiers.

```python
import csv

# Lecture d'un fichier CSV
with open("donnees.csv", "r") as fichier:
    lecteur_csv = csv.reader(fichier)
    for ligne in lecteur_csv:
        print(ligne)

# Écriture dans un fichier CSV
data = [
    ["Nom", "Âge", "Ville"],
    ["Alice", 30, "Paris"],
    ["Bob", 25, "New York"]
]
with open("dataset.csv", "w", newline="") as f:
    writer_csv = csv.writer(f)
    writer_csv.writerows(data)
```

Remarque : si vous utilisez **newline=""**, cela signifie que vous désactivez le traitement spécial des fins de ligne par Python.

Par exemple avec newline='\n', vous spécifiez explicitement que les fins de ligne doivent être des retours à la ligne UNIX, indépendamment du système d'exploitation.

## 5. Manipulation de fichiers JSON :

Le format JSON (JavaScript Object Notation) est largement utilisé pour échanger des données structurées. Python offre le module `json` pour travailler avec des fichiers JSON.

```python
import json

# Lecture d'un fichier JSON
with open("data.json", "r") as f:
    data_json = json.load(f)
    print(data_json)

# Écriture dans un fichier JSON
data = {"nom": "Alice", "age": 30, "ville": "Paris"}
with open("newData.json", "w") as f:
    json.dump(data, f)
```
