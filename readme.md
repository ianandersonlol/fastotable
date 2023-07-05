# FastoTable Documentation

FastoTable is a Python script that converts FASTA files (a common format for DNA and protein sequence data) into CSV files. The script reads a FASTA file and writes out a CSV file containing two columns: 'Protein Name' and 'Sequence'.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [How to Use](#how-to-use)
3. [Function Documentation](#function-documentation)

## Prerequisites
<a name="prerequisites"></a>

Ensure that you have Python installed on your system. The script is written in Python and no additional libraries are needed.

## How to Use
<a name="how-to-use"></a>

To use the script, you need to pass the path to the FASTA file as a command-line argument.

Usage:

```bash
python fastotable.py input.fasta
```

Where `input.fasta` should be replaced with the path to your FASTA file.

The script will create a CSV file in the same directory as the FASTA file, with the same name but a "_table.csv" suffix. For example, if your FASTA file is named "sequences.fasta", the CSV file will be "sequences_table.csv".

## Function Documentation
<a name="function-documentation"></a>

### fasta_to_csv function

```python
def fasta_to_csv(fasta_file, csv_file):
```

This function takes in the path to a FASTA file and a CSV file, reads the FASTA file, and writes the data to a CSV file.

**Parameters:**

- `fasta_file` (str): The path to the FASTA file.
- `csv_file` (str): The path to the output CSV file.

This function does not return any value. It writes the data directly to the CSV file.

The CSV file has two columns: 'Protein Name' and 'Sequence'. 'Protein Name' is the header line in the FASTA file (the line that starts with ">"), and 'Sequence' is the sequence of characters that follow the header line.