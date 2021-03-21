
#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

#Open the election results and read the file.
with open(file_to_load) as election_data:

#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

#Print the header row.
    headers = next(file_reader)
    
#Print each row in the CSV file.
    for row in file_reader:
        #Add the total vote count.
        total_votes += 1
        
        #Print the candidate name for each row.
        candidate_name = row[2]

#If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
                

#Print the candidate list.
print(candidate_options)
    
#Close file
#election_data.close()
