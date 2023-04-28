#add our dependencies

import csv
import os

#assign a variable to load a file from the path

file_to_load=os.path.join("election_results.csv")

#assign a variable to save the file to a path

file_to_save=os.path.join("election_analysis.txt")

# 1. Initialize a total vote counter.

total_votes=0

# Candidate options

candidate_options=[]

#create dictionary 

candidate_votes={}

# winning candidate and Winning count tracker
winning_candidate=""

winning_count=0

winning_percentage=0


#open the election results and read the file

with open(file_to_load) as election_data:

   
    # Read the file object with reader function

    file_reader=csv.reader(election_data)

# Read the header row

    headers= next(file_reader)
    #print each row in the csv file

    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1

        #print the candidate name from each row

        candidate_name=row[2]

         #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                
            #add it to the list of candidates.

            candidate_options.append(candidate_name)

            #track vote count
            candidate_votes[candidate_name]=0

        #add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1 

# Save results to our text file.
with open(file_to_save,"w") as txt_file:

    #print the final vote count to the terminal.
    election_results=(
        f"\nelection_results\n"
        f"--------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"--------------------------\n")
                    
    print(election_results, end="")

    #save the final vlote count to the text file.

    txt_file.write(election_results)

    # Iterate through the candidate list

    for candidate_name in candidate_votes:
        #2. retrieve the vote count of a candidate
        votes=candidate_votes[candidate_name]
        #3. calculate the percentage of votes 

        vote_percentage=float(votes)/float(total_votes)*100

        # To do: print out each candidate's name, vote count, and percentgage of

        #votes to the terminal.

        candidate_results=(
            f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n")

        # print each candidate, their voter count, and percentage to the terminal

        print(candidate_results)

        #save the candidate results to a txt file

        txt_file.write(candidate_results)
        
        #determine winning vote count, winning percentage and winning candidate.

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true then set winning_count=votes and winning_percent=

            winning_count=votes

            winning_candidate=candidate_name

            winning_percentage=vote_percentage

    #print out the winning candidate, vote count and percentage

    winning_candidate_summary=(
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------\n")

    print(winning_candidate_summary)

    # save the winning candidate's results to the text file.

    txt_file.write(winning_candidate_summary)


    




