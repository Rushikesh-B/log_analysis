# Rushikesh Bichewar


#-------------------NPA / NSclient log analyzer--------------------------#
import pathlib
import os
import re
import inquirer
#-------------------------------------------------------------------------------
foldernames = os.listdir('/Users/rbichewar/Documents/caselog/')
print(foldernames)

questions = [
 inquirer.List("foldername",  message="Please select folder",
                choices= foldernames,
            ),
]

folder = inquirer.prompt(questions)
print folder["foldername"]

folder11 = (folder["foldername"])
folder_pa = '/Users/rbichewar/Documents/caselog'
folder_path = os.path.join(folder_pa,folder11)

# define the path
currentDirectory = pathlib.Path('*')
# define the pattern
currentPattern = "*.log"

filenames = os.listdir(folder_path)
print(filenames)

# file selection------------------------------------------------------------------
questions = [
 inquirer.List("filename",  message="Please select file",
                choices= filenames,
            ),
]
filename_1 = inquirer.prompt(questions)
print filename_1["filename"]

    
# error list-------------if looking for specific data--------------

#questions = [
# inquirer.List("select",  message="Please select term (all gives output for all terms)",
#                choices=['all', 'error','Set clientId', 'gateway.npa.goskope.com','Resolved', 'keepalive','handleDataFromGw','tunneling','timeout','search'],
#            ),
#]
#answers = inquirer.prompt(questions)
#print answers["select"]


#date = raw_input ('enter date (ex.2020/07/15 05:42:39) :')
#--------------------------------------------------------------------------------


# select error message to filter from data
#if answers["Select"] == all:
#   line_regex = re.compile('error' or 'Set clientId' or 'gateway.npa.goskope.com' or 'Resolved' or 'keepalive' or 'handleDataFromGw' or 'tunneling' or 'timeout')
#elif answers['select'] == sea:
#   user_input = raw_input("add data")
#   line_regex = re.compile(user_input)
#else:
#    line_regex = re.compile(answers["select"])
 
line_regex = re.compile('Set clientId' or 'gateway.npa.goskope.com' or 'Resolved' or 'timeout' or 'dppool' or 'TCP connect' or 'failed')



#from datetime import datetime
#match = re.search(r'\d{4}-\d{2}-\d{2}', filename_1["filename"])
#date = date.strptime(match.group(),  '%Y-%m-%d').date()

#--------------------------------------------------------------------------------   
filename = (filename_1["filename"])
file_path = os.path.join(folder_path,filename)
print(file_path)

# Output file, where the matched loglines will be copied to

output_filename = os.path.normpath("/Users/rbichewar/Documents/npalogresult/npatest.log")

# Overwrites the file, ensure we're starting out with a blank file

with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode-------------------------

with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open(file_path, "r") as in_file:
        # Loop over each log line
         for line in in_file:
#            if re.match(date, line) and (line_regex.search(line)):
#                print (line)
            # If log line matches our regex, print to console, and output file
            if (line_regex.search(line)):
                print (line)
                out_file.write(line)
