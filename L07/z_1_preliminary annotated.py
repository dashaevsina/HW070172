import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml"
vars = yaml.load(open(settingsFile)) # The variables can then be opened simply
                                     # by running 'input'

###########################################################
# FUNCTIONS ###############################################
###########################################################

# Analyse bibTeX data; identify what needs to be fixed

def bibAnalyze(bibTexFile): # This function loads the BibTex file

    tempDic = {} # Creates a holder for the data, which is an  empty dictionary

    with open(bibTexFile, "r", encoding="utf8") as f1: # Explicitly declares the encoding
        records = f1.read() # Reads everything into one big string.
        records = records.split("\n@") # Splits into records on new line and @.
                                       # Generates a list of strings
        #Alternatively, can also be written in 1 line as: records = f1.read().split("\n@").

        for record in records[1:]: # Starts looping through results, one record at a time. 
                                   # NB: each record is a string that needs to be converted.
                                   # [1:] skips the very first element in the list (which
                                   # is an empty space)
            # Allow the processing of ONLY those records that have PDFs
            if ".pdf" in record.lower():
                record = record.strip() # Takes each record, strips it (to remove all 
                                        # whitespaces).
                record = record.split("\n")[:-1] # Splits each record on new line. 
                                                 # [:-1] drops the last element the list.

# Look through every item in that list and process it.

                for r in record[1:]: # Only analyses the fields in the data
                    r = r.split("=")[0].strip() # Splits on the '=' sign (which is what 
                                                # appears with key = value). [0] takes the 
                                                # very first element (always 0 in Python) 
                                                # and then strips it (removes whitespaces).

# Item has been collected, now edit the temperate dictionary by calculating the frequency.

                    if r in tempDic:
                        tempDic[r] += 1 # Checks if the item is already in the dictionary
                                        # then increases value by 1.
                    else:
                        tempDic[r] = 1 # If not, then edits and adds 1 as a value.
                        # Each time this is done, the dictionary is updated and the frequency 
                        # of the item is amended. This loop collects all the frequencies.

# Create a frequency dictionary

    results = [] # Uses an empty list
    for k,v in tempDic.items(): # Looks through the keys and values. k and v are used most commonly.
                                # It creates a printable result for each one of them.
        result = "%010d\t%s" % (v, k) # Adds 0s in front of the digits and puts the digits in the 
                                      # first row and now the second. Converts numbers into strings
                                      # (because there's a 0 in front of the numbers).
# NB: For a frequency list to be useful, it needs to be sorted (in either ascending or descending order).
        results.append(result)

    results = sorted(results, reverse=True) # The collected results are sorted.
                                            # reverse=True places the highest values at the top and 
                                            # the lowest at the bottom. After sorting it'll be one big
                                            # string again.
    results = "\n".join(results) # The list is now sorted.

    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9: # Saves these results for analysis. 
                                    # Loads the variables to pull out the file to process (bibtex_analysis.txt)
        f9.write(results) # Goes to folder to see the results.

bibAnalyze(vars['bib_all']) # Runs the script.



