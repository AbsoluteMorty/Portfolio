import csv
import os

#assign a variable for the file to load and the path
fileToLoad = os.path.join("Resources", "election_results.csv")
election_data = open(fileToLoad, 'r')


# initialize total vote counter
total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

print("\n")
# open the election result and read the file
with open(fileToLoad) as election_data:

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    # print each row of the CSV file
    for row in file_reader:
        
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the new file as a txt file
with open(file_to_save, "w") as txt_file:

    # write three counties to the file
    election_results = (
    f"  Election Results!\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    txt_file.write("--------------------------\n")
    winning_candidate_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    txt_file.write(winning_candidate_summary)

