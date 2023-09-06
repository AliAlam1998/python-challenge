# Dependencies
import os
import csv

# Set the path to the election data CSV file
csvpath = "Resources\\election_data.csv"

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through the rows
    for row in csvreader:
        # Extract data from the row
        voter_id = row[0]
        candidate = row[2]
        
        # Calculate the total votes
        total_votes += 1
        
        # Track candidates and their votes
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 1
        else:
            votes_per_candidate[candidate] += 1

# Initialize variables for the winner
winner = ""
winning_votes = 0

# Print results to the terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Check for the winner
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Export results to a text file
output_path = "Analysis\\Election_results.txt"
with open(output_path, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("----------------------------\n")
    for candidate in candidates:
        votes = votes_per_candidate[candidate]
        percentage = round((votes / total_votes) * 100, 3)
        textfile.write(f"{candidate}: {percentage}% ({votes})\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("----------------------------\n")
