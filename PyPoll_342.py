#The data we need to retrieve
#A complete list of candididates who received votes
#The percentage of votes each candidate won
#The total number of votes eacj candidiate won
#The winner of the eleaction based on popular votes


import csv
import os

#Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:

#To do: perform analysis
   print(election_data.read())
    
#Close file
#election_data.close()
