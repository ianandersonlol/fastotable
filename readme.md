# Documentation for fastaconvert.py

The `fastaconvert.py` is a Python script used to convert a FASTA format file into a CSV (Comma-Separated Values) format file. The CSV file will contain the names of proteins and their corresponding sequences.

## Table of Contents

- [Dependencies](#dependencies)
- [Functions](#functions)
  - [fasta_to_csv](#fasta_to_csv)
- [Usage](#usage)
- [Example](#example)

## Dependencies

To use this script, make sure you have Python installed along with the `csv` module. The `csv` module is part of Python's standard library so you don't need to install it separately.

## Functions

### fasta_to_csv

**Description**

The function `fasta_to_csv(fasta_file, csv_file)` is used to convert a FASTA file into a CSV file.

**Parameters**

- `fasta_file` (str): The path to the FASTA format file.
- `csv_file` (str): The path where the CSV format file will be saved.

**Return**

The function doesn't return any value, it writes the proteins and their sequences into a CSV file.

## Usage

To use the `fasta_to_csv` function, you need to provide the paths to the FASTA and CSV files. The FASTA file is the input and the CSV file is the output.

Here is the basic usage:

```python
fasta_file = 'path_to_your_fasta_file.fasta'
csv_file = 'path_to_your_csv_file.csv'
fasta_to_csv(fasta_file, csv_file)
```

Replace `'path_to_your_fasta_file.fasta'` and `'path_to_your_csv_file.csv'` with the paths to your FASTA and CSV files respectively.

## Example

Here is an example of how to use the `fasta_to_csv` function:

```python
fasta_file = 'araD.fasta'
csv_file = 'araD_output.csv'
fasta_to_csv(fasta_file, csv_file)
```

In this example, the script reads the file `araD.fasta` and converts it into a CSV file `araD_output.csv`. The CSV file will contain two columns: 'Protein Name' and 'Sequence'.