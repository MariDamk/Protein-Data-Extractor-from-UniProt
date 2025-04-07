import requests
from datetime import datetime

# List of accession numbers (example list, replace with actual values)
accession_numbers = ["P10814", "Q9Y261", "O00327"]

# Base URL for the API (replace with the actual URL)
base_url = "https://www.uniprot.org/uniprot/"

# Output file to save the results
output_file = "protein_data.txt"
error_log = "error_log.txt"

# Counters for summary
success_count = 0
failure_count = 0

# Open output files
with open(output_file, "w") as outfile, open(error_log, "w") as log:

    # Iterate over each accession number
    for accession in accession_numbers:

        ## Making sure that the status code gives a warning in case something is wrong
        try:
            response = requests.get(f"{base_url}{accession}.json")
        except requests.RequestException as e:
            log.write(f"[{datetime.now()}] Error fetching data for {accession}: {e}\n")
            failure_count += 1
            continue

        if response.status_code != 200:
            log.write(f"[{datetime.now()}] Failed to retrieve data for {accession}. Status code: {response.status_code}\n")
            failure_count += 1
            continue

        ## Load response data
        try:
            data = response.json()
        except ValueError:
            log.write(f"[{datetime.now()}] Error parsing JSON for accession {accession}\n")
            failure_count += 1
            continue

        ## Extracting protein info
        protein = data.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "Not Found")

        ## Extracting organism info
        organism = data.get("organism", {}).get("scientificName", "Not Found")

        ## Extracting chromosome info
        ## To find the position of the chromosome, I searched the json file with ctrl+f. 
        ## Then I copy-pasted the part from "title" to the part where the chromosome is to chat gpt 
        ## and asked to find the exact location of the chromosome.
        ## A list is created to save the chromosome(s)
        chromosome = [
            properties.get("value")
            for reference in data.get("uniProtKBCrossReferences", [])
            if reference.get("database") == "Proteomes"
            for properties in reference.get("properties", [])
            if properties.get("key") == "Component"
        ]

        ## In case that the protein is in more than one chromosome (like P10814)
        chromosome_info = ", ".join(chromosome) if chromosome else "Not Found"

        ## Generate timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ## Print and save results
        result = (f"[{timestamp}] For {accession}, the protein name is '{protein}', "
                  f"it is located in '{chromosome_info}', and the scientific name of the organism is '{organism}'.")
        
        print(result)
        outfile.write(result + "\n")
        success_count += 1

    ## Print and save summary
    summary = (f"\nSummary:\nTotal Accessions Processed: {len(accession_numbers)}\n"
               f"Successful Retrievals: {success_count}\n"
               f"Failed Retrievals: {failure_count}\n")
    print(summary)
    outfile.write(summary)
    log.write(summary)

