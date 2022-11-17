import csv
import os

# Assign a variable to LOAD a file from a path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

# Assign a variable to SAVE the file to a path.
file_to_save= os.path.join("Election_Analysis", "Resources","analysis","election_analysis.txt")

# Open election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

