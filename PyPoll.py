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

# Track winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # print(candidate_votes)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

        # determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print winning candidate's results to the terminal 
    winning_candidate_summary = (
    f"-------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------------\n")

    txt_file.write(winning_candidate_summary)

    #print(winning_candidate_summary)


# Challenge Objectives
# calculate the voter turnout for each county = # votes per county
    # {county: vote }

# calculate percentage of votes from each county from total count %
    # pull county votes / total_votes * 100

# determine county with highest turnout 

#print to console and write to txt file

