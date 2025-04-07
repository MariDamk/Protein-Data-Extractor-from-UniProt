**Protein Data Extractor from UniProt**

**_Overview_**
Protein Data Extractor from UniProt is a Python-based tool designed to efficiently retrieve protein information from the UniProt database using accession numbers. This script automates the process of extracting key protein details, including the protein name, organism name, and chromosome information.

This project was developed during the Master's classes in Applied Bioinformatics as a practical exercise to demonstrate efficient data extraction and error handling from public biological databases.

_**Key Features**_

    Automated Data Retrieval: Fetches protein name, organism name, and chromosome location from UniProt.

    Error Handling: Gracefully handles network issues and JSON parsing errors.

    Logging: Records failed retrievals and errors in a separate log file for traceability.

    Timestamped Output: Saves successful results with timestamps to a text file for organized data management.

    Summary Report: Displays a summary of successful and failed data extractions after processing.

_**Installation**_    

Clone the repository:

git clone https://github.com/yourusername/protein-data-fetcher.git
cd protein-data-fetcher

Install required packages: This script uses the requests library. Install it via pip:

pip install requests
  
_**Usage**_

    Prepare a list of accession numbers:

        Update the accession_numbers list in the script with your desired UniProt accession numbers.

    Run the script:

    python protein_data_fetcher.py

    Output:

        Successful retrievals are saved in protein_data.txt.

        Errors and failed retrievals are logged in error_log.txt.

        A summary report is displayed on the console and saved in the output file.

_**Example Output**_

Console:

[2025-04-07 15:45:23] For P10814, the protein name is 'Myoglobin', it is located in 'Chromosome 3', and the scientific name of the organism is 'Homo sapiens'.
[2025-04-07 15:45:23] For Q9Y261, the protein name is 'Hemoglobin subunit alpha', it is located in 'Chromosome 16', and the scientific name of the organism is 'Homo sapiens'.

Summary:
Total Accessions Processed: 3
Successful Retrievals: 2
Failed Retrievals: 1

Output File (protein_data.txt):

[2025-04-07 15:45:23] For P10814, the protein name is 'Myoglobin', it is located in 'Chromosome 3', and the scientific name of the organism is 'Homo sapiens'.

Error Log (error_log.txt):

[2025-04-07 15:45:24] Error fetching data for Q9Y261: Connection error.

_**Customization**_

    To change the list of accession numbers, edit the following line:

accession_numbers = ["P10814", "Q9Y261", "O00327"]

To modify the output file names:

    output_file = "protein_data.txt"
    error_log = "error_log.txt"

_**Contributing**_

Contributions are welcome! Feel free to fork the project, make improvements, and submit a pull request. For major changes, please open an issue first to discuss your ideas.
