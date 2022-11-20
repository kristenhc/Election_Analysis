import csv
import os

# Assign a variable to LOAD a file from a path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

# Assign a variable to SAVE the file to a path.
file_to_save= os.path.join("Election_Analysis", "Resources","analysis","election_analysis.txt")

# Initialize a total vounts counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

candidate_votes = {}

# Open election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        # add to total vote count
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1

print(candidate_votes)

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    print(vote_percentage)

    print(f"{candidate_name}: received {vote_percentage: .2f}% of the vote")
