<div align="center">

# CSV → PDF Room Card Generator
### Automatically generate printable room occupancy cards as a PDF from a CSV file

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red)](https://www.reportlab.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/)

🇬🇧 **[English — you are here]** · 🇫🇷 **[Français → README.md](README.md)**

</div>

---

Python script that generates a **landscape A4 PDF** from a CSV file: one page per room, room number displayed in a colored header banner, occupant names in large print, and your custom logo. Ready to print and pin on doors.

**Use cases:** summer camps · school trips · boarding schools · hostels · student residences · sports camps · hotels · group accommodation · youth centers · organized tours · conference housing · retreat centers

---

## Preview

![PDF room cards generated from CSV — room number, occupant list and custom logo](exemple.png)

---

## Features

| | | Details |
|--|--|---------|
| 🔍 | Encoding detection | `chardet` auto-detects UTF-8, Windows-1252, Latin-1, UTF-16… — no manual conversion needed |
| 🔍 | Delimiter detection | `csv.Sniffer` detects `,` `;` `\t` — US and European formats both supported |
| 📐 | Dynamic layout | Occupant block height adjusts per room (1 to 8+ people) |
| 🖼️ | Custom logo | PNG auto-resized to 4×4 inches, right-aligned (transparent background supported) |
| 📄 | Auto pagination | One page break per room — handles as many rooms as the CSV contains |

---

## CSV File Format

Each row = one room:

```
room_number, first_name_1, last_name_1, first_name_2, last_name_2, ...
```

| Column | Content |
|--------|---------|
| `[0]` | Room number or name |
| `[1]` / `[2]` | First / last name of occupant 1 |
| `[3]` / `[4]` | First / last name of occupant 2 *(optional)* |
| `…` | Additional pairs *(optional)* |

```csv
101,Marie,Dupont,Jean,Martin
102,Lucie,Bernard
214,Alice,Moreau,Emma,Leroy,Sofia,Petit
305,Paul,Durand,Thomas,Girard
```

> Empty rows ignored · variable number of occupants (min. 1) · orphaned column silently skipped · last names rendered in UPPERCASE, first names in normal case

---

## Preparing Your CSV

### From Microsoft Excel (xlsx → csv)

1. Open the `.xlsx` file and structure your data *(one row = one room)*
2. **File → Save As** → type: **CSV UTF-8 (Comma delimited) (\*.csv)**
   - If the UTF-8 option is missing, "CSV (semicolon-delimited)" also works — the script auto-detects the delimiter.
3. Click Save and confirm any warnings.

### From Google Sheets

**File → Download → Comma-separated values (.csv)**  
The exported file is UTF-8 with commas — ideal format.

### From LibreOffice Calc

**File → Save a Copy** → **Text CSV (.csv)**  
In the dialog: character set **UTF-8** · field delimiter `,` or `;`

---

## Installation & Usage

**Requirements: Python 3.7+**

```bash
pip install reportlab chardet
```

```
my-project/
├── script.py
├── rooms.csv
├── logo.png
└── output.pdf          ← generated automatically
```

```bash
# Basic usage — generates output.pdf in the current directory
python script.py rooms.csv logo.png

# Specify output file
python script.py rooms.csv logo.png -o room_cards.pdf

# Files in subfolders
python script.py data/rooms.csv assets/school_logo.png -o exports/room_cards_2024.pdf

# Absolute paths
python script.py /home/user/documents/rooms.csv /home/user/images/logo.png -o /home/user/desktop/result.pdf

# Path with spaces (quotes required)
python script.py "my folder/room list.csv" logo.png
```

| Argument | Required | Description |
|---------|---------|-------------|
| `csv_file` | ✅ | Path to the CSV file |
| `logo_file` | ✅ | Path to the PNG logo |
| `-o` / `--output` | ❌ | Output path (default: `output.pdf`) |

---

## Dependencies

| Library | Version | Role |
|---------|---------|------|
| `reportlab` | ≥ 3.6 | PDF generation (layout, text, images) |
| `chardet` | ≥ 4.0 | Automatic CSV encoding detection |
| `csv`, `argparse` | stdlib | Included with Python |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Accented characters display incorrectly | Re-save the CSV as UTF-8 (see *Preparing Your CSV*) |
| Logo not showing | Verify it is a PNG file and the path is correct |
| `The CSV file does not exist` | Wrap the path in quotes if it contains spaces |
| Some occupants missing | Each occupant requires **two columns** (first name + last name) |

---

## Customization

```python
PAGE_MARGIN  = 72                            # Page margins (typographic points)
HEADER_COLOR = colors.HexColor("#2c3e50")   # Banner background color
TEXT_COLOR   = colors.HexColor("#34495e")   # Occupant name color
```

Alternative banner colors: `#c0392b` red · `#27ae60` green · `#8e44ad` purple · `#d35400` orange · `#1a252f` navy

---

## GitHub Topics

Add these topics to your repository for maximum discoverability:

`python` `pdf` `csv` `pdf-generator` `reportlab` `room-assignment` `hostel` `summer-camp` `boarding-school` `printable` `automation` `cli` `occupancy` `school-trip`

---

## Contributing

Issues and pull requests welcome: JPEG/SVG support · custom fonts · portrait mode · multiple layout templates.

---

<div align="center">

🇫🇷 **[Français → README.md](README.md)**  
*Made with ❤️ and ReportLab*

</div>
