# 🏨 CSV to PDF — Générateur de fiches de chambre

Un script Python qui génère automatiquement un **PDF imprimable par chambre** à partir d'un fichier CSV listant les occupants, avec logo personnalisé. Conçu pour les hébergements collectifs : colonies, résidences, hôtels, camps sportifs, internats, etc.

---

## 📋 Ce que fait le script

À partir d'un fichier CSV structuré (numéro de chambre + prénoms/noms des occupants) et d'un logo (PNG), le script produit un **fichier PDF** dans lequel :

- **Chaque chambre occupe une page dédiée**, en format paysage (A4 horizontal)
- Un **bandeau coloré** en haut de page affiche le numéro de chambre en grand
- Les **noms des occupants** s'affichent en colonne à gauche, en grande police lisible
- Le **logo** fourni s'affiche à droite sur chaque page
- Une **page break automatique** sépare chaque chambre

Le résultat est un document prêt à imprimer et à afficher sur les portes, à distribuer aux accompagnateurs, ou à archiver.

### Exemple de rendu par page

```
┌────────────────────────────────────────────────────────┐
│                   ROOM N°214                           │  ← Bandeau bleu foncé
├────────────────────────────────────────────────────────┤
│                                                        │
│  Marie DUPONT              ┌──────────────┐            │
│  Jean MARTIN               │              │            │
│  Lucie BERNARD             │    [LOGO]    │            │
│                            │              │            │
│                            └──────────────┘            │
└────────────────────────────────────────────────────────┘
```

---

## ⚙️ Fonctionnalités

### Détection automatique de l'encodage
Le script utilise la bibliothèque **`chardet`** pour analyser les premiers octets du fichier CSV et déterminer automatiquement son encodage (`UTF-8`, `ISO-8859-1` / Latin-1, `Windows-1252`, etc.).

> Vous pouvez donc utiliser un CSV exporté depuis Excel (souvent en `Windows-1252` ou `Latin-1`), depuis Google Sheets (en `UTF-8`), ou depuis n'importe quel autre outil — **aucune conversion manuelle nécessaire**.

### Détection automatique du délimiteur
Le script utilise **`csv.Sniffer`** de la bibliothèque standard Python pour détecter si votre fichier utilise `;`, `,`, une tabulation `\t`, ou tout autre séparateur courant.

> Que votre CSV soit séparé par des virgules (format américain) ou par des points-virgules (format français/européen), le script s'adapte seul.

### Mise en page dynamique
La hauteur du bloc "occupants" s'ajuste **dynamiquement** en fonction du nombre de personnes par chambre. Qu'il y ait 1 ou 8 occupants, la mise en page reste propre.

### Support de n'importe quel logo PNG
Le logo est redimensionné automatiquement à `4 × 4 pouces` et aligné à droite. Vous pouvez fournir n'importe quelle image PNG (avec ou sans fond transparent).

---

## 🗂️ Format du fichier CSV

### Structure attendue

Chaque ligne du CSV représente **une chambre**, avec la structure suivante :

```
numéro_chambre, prénom_1, nom_1, prénom_2, nom_2, prénom_3, nom_3, ...
```

| Colonne | Contenu |
|--------|---------|
| `[0]` | Numéro (ou nom) de la chambre |
| `[1]` | Prénom du 1er occupant |
| `[2]` | Nom du 1er occupant |
| `[3]` | Prénom du 2ème occupant *(optionnel)* |
| `[4]` | Nom du 2ème occupant *(optionnel)* |
| `...` | Paires prénom/nom supplémentaires *(optionnelles)* |

### Exemple de fichier CSV valide

```csv
101,Marie,Dupont,Jean,Martin
102,Lucie,Bernard
214,Alice,Moreau,Emma,Leroy,Sofia,Petit
305,Paul,Durand,Thomas,Girard
```

> ✅ Les lignes vides et les lignes sans numéro de chambre sont ignorées automatiquement.  
> ✅ Le nombre d'occupants par chambre est variable (minimum 1).  
> ✅ Si un prénom est présent sans nom correspondant (nombre impair de colonnes), la dernière entrée incomplète est ignorée.

### Ce que le script affiche

Pour la ligne `214,Alice,Moreau,Emma,Leroy,Sofia,Petit` :

```
ROOM N°214

Alice MOREAU
Emma LEROY
Sofia PETIT          [LOGO]
```

> Les noms sont automatiquement affichés en **MAJUSCULES**, les prénoms en casse normale.

---

## 🔄 Préparer votre fichier CSV

### Depuis Microsoft Excel

1. Ouvrez votre fichier `.xlsx`
2. Structurez vos données selon le format décrit ci-dessus (une ligne = une chambre)
3. Cliquez sur **Fichier → Enregistrer sous**
4. Dans le menu déroulant "Type de fichier", choisissez **CSV UTF-8 (délimité par des virgules) (*.csv)**
   - ⚠️ Privilégiez l'option "UTF-8" si elle est disponible pour éviter les problèmes d'accents
5. Cliquez sur **Enregistrer** et confirmez les avertissements

> 💡 Si Excel n'affiche pas l'option "UTF-8", choisissez simplement "CSV (séparé par des points-virgules)" — le script détectera le délimiteur automatiquement.

### Depuis Google Sheets

1. Ouvrez votre feuille de calcul
2. Structurez vos données selon le format attendu
3. Cliquez sur **Fichier → Télécharger → Valeurs séparées par des virgules (.csv)**
4. Le fichier téléchargé sera en UTF-8 avec des virgules comme délimiteur — parfait pour le script

### Depuis LibreOffice Calc

1. Ouvrez votre fichier
2. Cliquez sur **Fichier → Enregistrer une copie**
3. Choisissez le format **Texte CSV (.csv)**
4. Dans la boîte de dialogue qui s'ouvre, choisissez :
   - Jeu de caractères : **UTF-8**
   - Séparateur de champ : `,` ou `;` (au choix, le script s'adapte)

---

## 🚀 Installation et utilisation

### Prérequis

- Python **3.7+**
- pip

### Installation des dépendances

```bash
pip install reportlab chardet
```

### Structure des fichiers recommandée

```
mon-projet/
├── script.py          ← Le script Python
├── chambres.csv       ← Votre fichier CSV
├── logo.png           ← Votre logo en PNG
└── output.pdf         ← Le PDF généré (créé automatiquement)
```

### Commande de base

```bash
python script.py chambres.csv logo.png
```

Cela génère un fichier `output.pdf` dans le répertoire courant.

### Spécifier un nom de fichier de sortie

```bash
python script.py chambres.csv logo.png -o fiches_chambres.pdf
```

### Syntaxe complète

```bash
python script.py <fichier_csv> <fichier_logo> [-o <fichier_sortie>]
```

| Argument | Obligatoire | Description |
|--------|------------|-------------|
| `fichier_csv` | ✅ Oui | Chemin vers le fichier CSV d'entrée |
| `fichier_logo` | ✅ Oui | Chemin vers le logo PNG |
| `-o`, `--output` | ❌ Non | Chemin du PDF généré (défaut : `output.pdf`) |

### Exemples avancés

```bash
# Fichiers dans des sous-dossiers
python script.py data/listes.csv assets/logo_ecole.png -o exports/fiches_2024.pdf

# Chemin absolu
python script.py /home/user/documents/chambres.csv /home/user/images/logo.png -o /home/user/bureau/resultat.pdf
```

---

## 📦 Dépendances

| Bibliothèque | Version recommandée | Rôle |
|-------------|-------------------|------|
| `reportlab` | ≥ 3.6 | Génération du PDF (mise en page, texte, images) |
| `chardet` | ≥ 4.0 | Détection automatique de l'encodage du CSV |
| `csv` | stdlib | Lecture du CSV (inclus dans Python) |
| `argparse` | stdlib | Gestion des arguments en ligne de commande (inclus dans Python) |

---

## 🛠️ Dépannage

### Les accents s'affichent mal dans le PDF
Le script détecte l'encodage automatiquement, mais si le résultat est incorrect, vérifiez que votre CSV est bien enregistré en **UTF-8** (voir la section "Préparer votre fichier CSV" ci-dessus).

### Le logo ne s'affiche pas
- Vérifiez que le fichier est bien un **PNG** (les JPEG sont aussi supportés par ReportLab mais non testés ici)
- Vérifiez que le chemin fourni est correct et que le fichier existe

### "Error: The CSV file does not exist"
Le script vérifie l'existence des fichiers avant de démarrer. Vérifiez le chemin et les guillemets si le chemin contient des espaces :
```bash
python script.py "mon dossier/liste chambres.csv" logo.png
```

### Certains occupants n'apparaissent pas
Le script ignore les paires prénom/nom incomplètes. Assurez-vous que chaque occupant occupe bien **deux colonnes** (prénom ET nom). Une colonne orpheline en fin de ligne est silencieusement ignorée.

---

## 📐 Personnalisation du code

Les principales constantes de style sont définies en haut du fichier pour une modification facile :

```python
PAGE_MARGIN = 72                          # Marges de la page (en points)
HEADER_COLOR = colors.HexColor("#2c3e50") # Couleur du bandeau (bleu foncé)
TEXT_COLOR = colors.HexColor("#34495e")   # Couleur du texte des noms
```

Pour changer la couleur du bandeau, remplacez le code hexadécimal par la couleur de votre choix. Par exemple :
- Rouge : `"#c0392b"`
- Vert : `"#27ae60"`
- Violet : `"#8e44ad"`
