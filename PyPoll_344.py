#The data we need to retrieve
#A complete list of candididates who received votes
#The percentage of votes each candidate won
#The total number of votes eacj candidiate won
#The winner of the eleaction based on popular votes

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:

#Read the file object with the reader function
    file_reader = csv.reader(election_data)

#Print the header row.
    headers = next(file_reader)
    print(headers)

#Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

 # Write three counties to the file.
#outfile.write("Arapahoe, Denver, Jefferson")
#outfile.write("Arapahoe\nDenver\nJefferson")

#Print each row in the CSV file
for row in file_reader:
        print(row)

#Print the file object
#print(election_data.read())
    
#Close file
election_data.close()
