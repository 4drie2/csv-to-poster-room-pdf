<div align="center">

# 🏨 CSV → PDF Room Card Generator

**Génère automatiquement des fiches de chambre imprimables en PDF à partir d'un fichier CSV**  
*Automatically generate printable room occupancy cards as a PDF from a CSV file*

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red)](https://www.reportlab.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

🇫🇷 **[Lire en français — vous êtes ici]** · 🇬🇧 **[Read in English → README.en.md](README.en.md)**

</div>

---

> **En une phrase :** Ce script Python prend une liste chambre/occupants en CSV et produit un PDF paysage avec une page par chambre, les noms en grand et votre logo — prêt à imprimer et afficher sur les portes.

**Cas d'usage typiques :** colonies de vacances · séjours scolaires · internats · auberges de jeunesse · résidences étudiantes · camps sportifs · hôtels · centres de loisirs · hébergements de groupe · voyages organisés

---

## 📋 Ce que fait le script

À partir d'un fichier CSV structuré (numéro de chambre + prénoms/noms des occupants) et d'un logo PNG, le script produit un **fichier PDF** dans lequel :

- **Chaque chambre occupe une page dédiée**, en format paysage (A4 horizontal)
- Un **bandeau coloré** en haut de page affiche le numéro de chambre en grand
- Les **noms des occupants** s'affichent en colonne à gauche, en grande police lisible
- Le **logo** s'affiche à droite sur chaque page
- Une **saut de page automatique** sépare chaque chambre

Le résultat est un document prêt à imprimer, à afficher sur les portes, à distribuer aux accompagnateurs, ou à archiver.

### Exemple de rendu par page

```
┌────────────────────────────────────────────────────────────────┐
│                        ROOM N°214                              │  ← Bandeau coloré
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Marie DUPONT                    ┌──────────────────┐        │
│   Jean MARTIN                     │                  │        │
│   Lucie BERNARD                   │      [LOGO]      │        │
│                                   │                  │        │
│                                   └──────────────────┘        │
└────────────────────────────────────────────────────────────────┘
             page A4 paysage — une chambre par page
```

---

## ⚙️ Fonctionnalités

### 🔍 Détection automatique de l'encodage du CSV
La bibliothèque **`chardet`** analyse les premiers octets du fichier pour identifier automatiquement son encodage : `UTF-8`, `ISO-8859-1` / Latin-1, `Windows-1252`, `UTF-16`, etc.

> Utilisez un CSV exporté depuis Excel (souvent `Windows-1252`), Google Sheets (`UTF-8`), LibreOffice ou tout autre outil — **aucune conversion manuelle n'est nécessaire**.

### 🔍 Détection automatique du délimiteur
**`csv.Sniffer`** de la bibliothèque standard Python détecte automatiquement le séparateur utilisé : virgule `,`, point-virgule `;`, tabulation `\t`, etc.

> Format américain (`,`) ou européen (`;`) : le script s'adapte sans configuration.

### 📐 Mise en page dynamique
La hauteur du bloc occupants s'ajuste selon le nombre de personnes par chambre. De 1 à 8 occupants, la mise en page reste propre et équilibrée.

### 🖼️ Logo personnalisable
Le logo PNG est redimensionné automatiquement (`4 × 4 pouces`) et aligné à droite. Transparent ou non, n'importe quel PNG fonctionne.

### 📄 Pagination automatique
Un saut de page est inséré entre chaque chambre. Le script traite autant de chambres que votre CSV en contient.

---

## 🗂️ Format du fichier CSV

### Structure attendue

Chaque ligne = une chambre. Les colonnes suivent ce schéma :

```
numéro_chambre, prénom_1, nom_1, prénom_2, nom_2, prénom_3, nom_3, ...
```

| Colonne | Contenu |
|--------|---------|
| `[0]` | Numéro ou nom de la chambre |
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

> ✅ Lignes vides ignorées automatiquement  
> ✅ Nombre d'occupants variable par chambre (minimum 1)  
> ✅ Colonne orpheline en fin de ligne ignorée silencieusement  
> ✅ Noms affichés automatiquement en MAJUSCULES, prénoms en casse normale

### Résultat pour `214,Alice,Moreau,Emma,Leroy,Sofia,Petit`

```
ROOM N°214

Alice MOREAU
Emma LEROY
Sofia PETIT          [LOGO]
```

---

## 🔄 Préparer votre fichier CSV

### Depuis Microsoft Excel

1. Ouvrez votre fichier `.xlsx`
2. Structurez vos données (une ligne = une chambre)
3. **Fichier → Enregistrer sous**
4. Type de fichier : **CSV UTF-8 (délimité par des virgules) (*.csv)**
   - ⚠️ Préférez l'option "UTF-8" pour éviter les problèmes d'accents
5. Enregistrer et confirmer les avertissements

> 💡 Si l'option UTF-8 est absente, "CSV séparé par des points-virgules" fonctionne aussi.

### Depuis Google Sheets

1. Structurez vos données dans la feuille
2. **Fichier → Télécharger → Valeurs séparées par des virgules (.csv)**
3. Le fichier sera en UTF-8 avec virgules — format idéal

### Depuis LibreOffice Calc

1. **Fichier → Enregistrer une copie** → format **Texte CSV (.csv)**
2. Dans la boîte de dialogue :
   - Jeu de caractères : **UTF-8**
   - Séparateur : `,` ou `;` (les deux fonctionnent)

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
├── logo.png           ← Votre logo PNG
└── output.pdf         ← Le PDF généré (créé automatiquement)
```

### Commande de base

```bash
python script.py chambres.csv logo.png
```

Génère `output.pdf` dans le répertoire courant.

### Spécifier le fichier de sortie

```bash
python script.py chambres.csv logo.png -o fiches_chambres.pdf
```

### Syntaxe complète

```bash
python script.py <fichier_csv> <fichier_logo> [-o <fichier_sortie>]
```

| Argument | Obligatoire | Description |
|---------|------------|-------------|
| `fichier_csv` | ✅ | Chemin vers le fichier CSV |
| `fichier_logo` | ✅ | Chemin vers le logo PNG |
| `-o` / `--output` | ❌ | Fichier de sortie (défaut : `output.pdf`) |

### Exemples avancés

```bash
# Fichiers dans des sous-dossiers
python script.py data/listes.csv assets/logo_ecole.png -o exports/fiches_2024.pdf

# Chemins absolus
python script.py /home/user/documents/chambres.csv /home/user/images/logo.png -o /home/user/bureau/resultat.pdf

# Chemin avec espaces (utiliser des guillemets)
python script.py "mon dossier/liste chambres.csv" logo.png
```

---

## 📦 Dépendances

| Bibliothèque | Version | Rôle |
|-------------|---------|------|
| `reportlab` | ≥ 3.6 | Génération PDF (mise en page, texte, images) |
| `chardet` | ≥ 4.0 | Détection automatique de l'encodage CSV |
| `csv` | stdlib | Lecture CSV (inclus dans Python) |
| `argparse` | stdlib | Arguments en ligne de commande (inclus dans Python) |

---

## 🛠️ Dépannage

### Les accents s'affichent mal dans le PDF
Le script détecte l'encodage automatiquement. Si le résultat est incorrect, réenregistrez votre CSV explicitement en **UTF-8** (voir section "Préparer votre fichier CSV").

### Le logo ne s'affiche pas
- Vérifiez que c'est bien un **PNG** (format recommandé)
- Vérifiez que le chemin est correct et que le fichier existe

### `Error: The CSV file does not exist`
Vérifiez le chemin. Si le chemin contient des espaces, entourez-le de guillemets :
```bash
python script.py "mon dossier/chambres.csv" logo.png
```

### Certains occupants n'apparaissent pas
Chaque occupant doit occuper **deux colonnes** (prénom + nom). Une colonne orpheline en fin de ligne est ignorée silencieusement.

---

## 📐 Personnalisation

Les constantes de style sont définies en haut du fichier :

```python
PAGE_MARGIN = 72                           # Marges (en points typographiques)
HEADER_COLOR = colors.HexColor("#2c3e50")  # Couleur du bandeau
TEXT_COLOR   = colors.HexColor("#34495e")  # Couleur des noms
```

Quelques couleurs alternatives pour le bandeau :
| Couleur | Code hex |
|---------|---------|
| Rouge | `#c0392b` |
| Vert | `#27ae60` |
| Violet | `#8e44ad` |
| Orange | `#d35400` |
| Bleu marine | `#1a252f` |

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une *issue* ou une *pull request* pour :
- Ajouter le support d'autres formats d'image (JPEG, SVG…)
- Permettre la personnalisation de la police
- Ajouter un mode portrait
- Supporter des templates de mise en page multiples

---

<div align="center">

🇬🇧 **English version → [README.en.md](README.en.md)**

*Made with ❤️ and ReportLab*

</div>
