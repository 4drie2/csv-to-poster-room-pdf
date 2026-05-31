# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abidaux <abidaux@student.42lehavre.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/25 18:52:15 by abidaux           #+#    #+#              #
#    Updated: 2026/05/25 18:52:24 by abidaux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# python script.py path/to/file.csv path/to/logo.png -o output.pdf

import csv
import chardet
import argparse
import os
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import SimpleDocTemplate, Image, Spacer, Flowable, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import inch, cm

# Constants for layout and styling
PAGE_MARGIN = 72
AVAILABLE_WIDTH = A4[0] - (2 * PAGE_MARGIN)
HEADER_COLOR = colors.HexColor("#2c3e50")  # Dark blue
TEXT_COLOR = colors.HexColor("#34495e")

class RoomHeader(Flowable):
    """Custom Flowable to create the room header."""
    
    def __init__(self, room_num):
        Flowable.__init__(self)
        self.room_num = room_num
        self.width = AVAILABLE_WIDTH
        self.height = 1.5 * cm

    def draw(self):
        self.canv.setFillColor(HEADER_COLOR)
        self.canv.rect(0, 0, self.width, self.height, fill=1)
        
        # White text for the header
        self.canv.setFont("Helvetica-Bold", 18)
        self.canv.setFillColor(colors.white)
        self.canv.drawCentredString(self.width / 2, self.height / 3, f"ROOM N°{self.room_num}")

class OccupantDisplay(Flowable):
    """Custom Flowable to display the list of occupants."""
    
    def __init__(self, occupants):
        Flowable.__init__(self)
        self.occupants = occupants
        self.width = AVAILABLE_WIDTH * 0.7  # 70% of available width
        self.height = len(occupants) * 1.5 * cm + 0.5 * cm  # Dynamic height

    def draw(self):
        left_padding = -1.5 * cm  # Negative value to shift text to the left
        y_position = self.height - 0.5 * cm
        
        self.canv.setFont("Helvetica-Bold", 16)
        self.canv.setFillColor(TEXT_COLOR)
        
        for first_name, last_name in self.occupants:
            self.canv.drawString(left_padding, y_position, f"{first_name} {last_name.upper()}")
            y_position -= 1.5 * cm

def detect_encoding(file_path):
    """Detects the CSV file encoding by analyzing a chunk."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(10000))
    return result['encoding'] or 'utf-8'

def detect_delimiter(file_path, encoding):
    """Detects the delimiter used in the CSV file."""
    with open(file_path, 'r', encoding=encoding) as f:
        sample = f.read(65536)

    sniffer = csv.Sniffer()
    try:
        dialect = sniffer.sniff(sample, delimiters=',;\t|')
        return dialect.delimiter
    except csv.Error:
        # Fallback: count occurrences of common delimiters in the sample
        candidates = {d: sample.count(d) for d in (',', ';', '\t', '|')}
        return max(candidates, key=candidates.get)

def generate_pdf(csv_path, logo_path, output_path="output.pdf"):
    """Generates a PDF from the CSV data with a logo in the top right."""
    encoding = detect_encoding(csv_path)
    delimiter = detect_delimiter(csv_path, encoding)
    
    print(f"Detected CSV encoding: {encoding} with delimiter: '{delimiter}'")
    
    rooms = {}
    with open(csv_path, 'r', encoding=encoding) as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        for row in csv_reader:
            if not row:  # Skip empty rows
                continue
                
            room_num = row[0].strip()
            if not room_num:  # Skip rows without a room number
                continue
                
            # Extract first/last name pairs (alternating columns)
            occupants = []
            for i in range(1, len(row) - 1, 2):
                first_name = row[i].strip()
                last_name = row[i + 1].strip() if i + 1 < len(row) else ""
                
                if first_name and last_name:
                    occupants.append((first_name, last_name))
            
            rooms[room_num] = occupants
    
    # PDF document configuration
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(A4),
        rightMargin=PAGE_MARGIN, 
        leftMargin=PAGE_MARGIN,
        topMargin=PAGE_MARGIN, 
        bottomMargin=PAGE_MARGIN
    )
    
    elements = []
    room_items = list(rooms.items())
    
    for i, (room_num, occupants) in enumerate(room_items):
        # Add stylish header with room number
        elements.append(RoomHeader(room_num))
        elements.append(Spacer(1, 1 * cm))
        
        # Prepare layout elements
        occupant_display = OccupantDisplay(occupants)
        
        img = Image(logo_path, width=4 * inch, height=4 * inch)
        img.hAlign = 'RIGHT'
        
        # Table layout to split the space (70% text, 30% image)
        layout_data = [[occupant_display, img]]
        layout_table = Table(
            layout_data, 
            colWidths=[AVAILABLE_WIDTH * 0.7, AVAILABLE_WIDTH * 0.3]
        )
        
        layout_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        elements.append(layout_table)
        elements.append(Spacer(1, 1 * cm))
        
        # Add a page break after each room, except the last one
        if i < len(room_items) - 1:
            elements.append(PageBreak())
    
    # Build and save the PDF
    doc.build(elements)
    print(f"PDF successfully generated: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file to a PDF with a custom logo.")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("logo_file", help="Path to the input logo PNG")
    parser.add_argument("-o", "--output", default="output.pdf", help="Output path for the generated PDF")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.csv_file):
        print(f"Error: The CSV file '{args.csv_file}' does not exist.")
        exit(1)
    
    if not os.path.exists(args.logo_file):
        print(f"Error: The logo file '{args.logo_file}' does not exist.")
        exit(1)
    
    generate_pdf(args.csv_file, args.logo_file, args.output)