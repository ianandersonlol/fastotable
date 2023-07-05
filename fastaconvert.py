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
        for protein in proteins:
            writer.writerow([protein[0], protein[1]])

    print("Conversion complete.")
# Usage
fasta_file = 'araD.fasta'
csv_file = 'araD_output.csv'
fasta_to_csv(fasta_file, csv_file)
