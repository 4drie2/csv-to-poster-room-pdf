<div align="center">

# 🏨 CSV → PDF Room Card Generator

**Automatically generate printable room occupancy cards as a PDF from a simple CSV file**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red)](https://www.reportlab.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

🇬🇧 **[Read in English — you are here]** · 🇫🇷 **[Lire en français → README.md](README.md)**

</div>

---

> **In one sentence:** This Python script takes a CSV list of rooms and occupants and produces a landscape PDF with one page per room — occupant names in large print and your custom logo — ready to print and pin on the door.

**Typical use cases:** summer camps · school trips · boarding schools · hostels · student residences · sports camps · hotels · group accommodation · youth centers · organized tours · conference housing · retreat centers

---

## 📋 What it does

Given a structured CSV file (room number + occupant first/last names) and a PNG logo, the script produces a **PDF document** where:

- **Each room gets its own dedicated page**, in landscape A4 format
- A **colored header banner** displays the room number in large text
- **Occupant names** are listed on the left in a large, readable font
- Your **logo** appears on the right side of every page
- An **automatic page break** separates each room

The result is a document ready to print, display on doors, hand out to supervisors, or archive.

### Visual output example

```
┌────────────────────────────────────────────────────────────────┐
│                        ROOM N°214                              │  ← Colored banner
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Marie DUPONT                    ┌──────────────────┐        │
│   Jean MARTIN                     │                  │        │
│   Lucie BERNARD                   │      [LOGO]      │        │
│                                   │                  │        │
│                                   └──────────────────┘        │
└────────────────────────────────────────────────────────────────┘
              A4 landscape — one room per page
```

---

## ⚙️ Features

### 🔍 Automatic CSV encoding detection
Uses **`chardet`** to analyze the first bytes of the CSV file and automatically identify its encoding: `UTF-8`, `ISO-8859-1` / Latin-1, `Windows-1252`, `UTF-16`, and more.

> Use a CSV exported from Excel (typically `Windows-1252`), Google Sheets (`UTF-8`), LibreOffice, or any other tool — **no manual conversion needed**.

### 🔍 Automatic delimiter detection
**`csv.Sniffer`** from the Python standard library automatically detects the column separator: comma `,`, semicolon `;`, tab `\t`, etc.

> US format (`,`) or European format (`;`): the script adapts with zero configuration.

### 📐 Dynamic layout
The occupants block height adjusts automatically based on the number of people per room. From 1 to 8+ occupants, the layout stays clean and balanced.

### 🖼️ Custom logo support
Your PNG logo is automatically resized to `4 × 4 inches` and right-aligned. Transparent background or not — any PNG works.

### 📄 Automatic pagination
A page break is inserted between every room. The script handles as many rooms as your CSV contains.

---

## 🗂️ CSV File Format

### Expected structure

Each row = one room. Columns follow this pattern:

```
room_number, first_name_1, last_name_1, first_name_2, last_name_2, ...
```

| Column | Content |
|--------|---------|
| `[0]` | Room number or name |
| `[1]` | First occupant's first name |
| `[2]` | First occupant's last name |
| `[3]` | Second occupant's first name *(optional)* |
| `[4]` | Second occupant's last name *(optional)* |
| `...` | Additional first/last name pairs *(optional)* |

### Valid CSV example

```csv
101,Marie,Dupont,Jean,Martin
102,Lucie,Bernard
214,Alice,Moreau,Emma,Leroy,Sofia,Petit
305,Paul,Durand,Thomas,Girard
```

> ✅ Empty rows are automatically ignored  
> ✅ Variable number of occupants per room (minimum 1)  
> ✅ An orphaned column at the end of a row is silently ignored  
> ✅ Last names are automatically rendered in UPPERCASE, first names in normal case

### Output for `214,Alice,Moreau,Emma,Leroy,Sofia,Petit`

```
ROOM N°214

Alice MOREAU
Emma LEROY
Sofia PETIT          [LOGO]
```

---

## 🔄 Preparing your CSV file

### From Microsoft Excel

1. Open your `.xlsx` file
2. Structure your data (one row = one room)
3. **File → Save As**
4. File type: **CSV UTF-8 (Comma delimited) (*.csv)**
   - ⚠️ Choose the "UTF-8" option when available to avoid accent issues
5. Click Save and confirm any warnings

> 💡 If the UTF-8 option is missing, "CSV (semicolon-delimited)" also works — the script detects the delimiter automatically.

### From Google Sheets

1. Structure your data in the sheet
2. **File → Download → Comma-separated values (.csv)**
3. The downloaded file will be UTF-8 with commas — ideal format

### From LibreOffice Calc

1. **File → Save a Copy** → **Text CSV (.csv)**
2. In the dialog:
   - Character set: **UTF-8**
   - Field delimiter: `,` or `;` (both work)

---

## 🚀 Installation & Usage

### Requirements

- Python **3.7+**
- pip

### Install dependencies

```bash
pip install reportlab chardet
```

### Recommended project structure

```
my-project/
├── script.py       ← The Python script
├── rooms.csv       ← Your CSV file
├── logo.png        ← Your PNG logo
└── output.pdf      ← Generated PDF (created automatically)
```

### Basic usage

```bash
python script.py rooms.csv logo.png
```

This generates `output.pdf` in the current directory.

### Specify output file

```bash
python script.py rooms.csv logo.png -o room_cards.pdf
```

### Full syntax

```bash
python script.py <csv_file> <logo_file> [-o <output_file>]
```

| Argument | Required | Description |
|---------|---------|-------------|
| `csv_file` | ✅ | Path to the input CSV file |
| `logo_file` | ✅ | Path to the PNG logo |
| `-o` / `--output` | ❌ | Output file path (default: `output.pdf`) |

### Advanced examples

```bash
# Files in subfolders
python script.py data/rooms.csv assets/school_logo.png -o exports/room_cards_2024.pdf

# Absolute paths
python script.py /home/user/documents/rooms.csv /home/user/images/logo.png -o /home/user/desktop/result.pdf

# Path with spaces (use quotes)
python script.py "my folder/room list.csv" logo.png
```

---

## 📦 Dependencies

| Library | Version | Role |
|---------|---------|------|
| `reportlab` | ≥ 3.6 | PDF generation (layout, text, images) |
| `chardet` | ≥ 4.0 | Automatic CSV encoding detection |
| `csv` | stdlib | CSV parsing (included with Python) |
| `argparse` | stdlib | Command-line argument handling (included with Python) |

---

## 🛠️ Troubleshooting

### Accented characters display incorrectly in the PDF
The script detects encoding automatically, but if the result looks wrong, re-save your CSV explicitly as **UTF-8** (see "Preparing your CSV file" above).

### Logo is not showing
- Make sure the file is a **PNG** (recommended format)
- Double-check the path is correct and the file exists

### `Error: The CSV file does not exist`
Check the path. If it contains spaces, wrap it in quotes:
```bash
python script.py "my folder/room list.csv" logo.png
```

### Some occupants are missing
Each occupant must occupy **two columns** (first name + last name). An orphaned column at the end of a row is silently skipped.

---

## 📐 Customization

Style constants are defined at the top of the file for easy editing:

```python
PAGE_MARGIN = 72                           # Page margins (in typographic points)
HEADER_COLOR = colors.HexColor("#2c3e50")  # Banner background color
TEXT_COLOR   = colors.HexColor("#34495e")  # Occupant name color
```

Alternative banner colors:

| Color | Hex code |
|-------|---------|
| Red | `#c0392b` |
| Green | `#27ae60` |
| Purple | `#8e44ad` |
| Orange | `#d35400` |
| Navy | `#1a252f` |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or a pull request to:
- Add support for other image formats (JPEG, SVG…)
- Allow custom font selection
- Add portrait page mode
- Support multiple layout templates

---

## 💡 GitHub Topics (suggested)

To maximize discoverability, add these topics to your repository settings:

`python` `pdf` `csv` `pdf-generator` `reportlab` `room-assignment` `hostel` `summer-camp` `boarding-school` `printable` `automation` `cli` `occupancy` `school-trip`

---

<div align="center">

🇫🇷 **Version française → [README.md](README.md)**

*Made with ❤️ and ReportLab*

</div>
