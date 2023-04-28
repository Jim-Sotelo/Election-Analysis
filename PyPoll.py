#The data we need to retrieve
#1. the total number of votes cast
#2. a complete list of candiates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winnter of the election based on popular vote

import csv
import os



#assign a variable for the file to load and the path

file_to_load=os.path.join("election_results.csv") 

#Open the elction results and read the file.

with open(file_to_load) as election_data:

#To do:perform analysis.

    print(election_data)

#create a filename variable to a direct or indirect path to the file

file_to_save=os.path.join("election_analysis.txt")

#using the open() function with the "w" mode we will write data to the file

open(file_to_save, "w")

#close the file.

election_data.close()


dir(os)



