import sys
import os
import csv

def fasta_to_csv(fasta_file, csv_file):
    proteins = []
    current_protein = ""
    current_sequence = ""

    # Read the FASTA file
    with open(fasta_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_protein:
                    proteins.append((current_protein, current_sequence))
                current_protein = line[1:]
                current_sequence = ""
            else:
                current_sequence += line

        # Append the last protein
        if current_protein:
            proteins.append((current_protein, current_sequence))

    # Write to CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Protein Name', 'Sequence'])
        for i, protein in enumerate(proteins, start=1):
            writer.writerow([protein[0], protein[1]])
            print(f"[{i}/{len(proteins)}] Protein '{protein[0]}' written to CSV.")

    print("Conversion complete.")

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.fasta")
    else:
        input_file = sys.argv[1]
        output_file = os.path.splitext(os.path.basename(input_file))[0] + "_table.csv"
        fasta_to_csv(input_file, output_file)
