import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################

settingsFile = "z_config.yml" # Loads the settings, essentially just the files
settings = yaml.safe_load(open(settingsFile))
bibKeys = yaml.safe_load(open("zotero_biblatex_keys.yml")) # Loads the BibTex keys, which is the file
                                                           # that was just created to easily update the keys.

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile): # Loads the BibTex file

    bibDic = {} # Creates empty dictionary

    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read().split("\n@") # Splits on new line and @.

        for record in records[1:]:
            # Allow the processing of ONLY those records that have PDFs
            if ".pdf" in record.lower(): # Only loads the data that has PDFs

                record = record.strip().split("\n")[:-1] # Splits the record into a list, 
                                                         # drops the last element in the list.

# Loop through the list of "key-value" pairs

                rType = record[0].split("{")[0].strip() # Takes care of the first element of 
                                                        # that list. 
                                                        # Grabs list element (record) with index 0.
                rCite = record[0].split("{")[1].strip().replace(",", "")
                                                        # Splits list element on the '{' character 
                                                        # to get the type and edition key.

                bibDic[rCite] = {} # Adds an empty record into the dictionary by using the citationKey [rCite]
                                   # as a key value.
                bibDic[rCite]["rCite"] = rCite # Adds recordCite into the record.
                bibDic[rCite]["rType"] = rType # Adds recordType into the newly created record.

# Process the rest of the record.

                for r in record[1:]: # Loops through the elements in the record starting with 1.
                                     # [1:] skips the first element since it has already been processed.
                    key = r.split("=")[0].strip() # Splits every element on '=' sign.
                                                  # Takes the first key, gets the value.
                    val = r.split("=")[1].strip()
                    val = re.sub("^\{|\},?", "", val) # Removes the '{'.

                    fixedKey = bibKeys[key] # Adds the key-value pair into the dictionary.
                                            # Takes the file and swaps the key that was found in the 
                                            # record with the key that actually needs to be used.

                    bibDic[rCite][fixedKey] = val # Updates the record. Through the fixed key it adds
                                                  # the value that was extracted from it. 


    print("="*80)
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic)) # Since it's a loop, it prints the 
                                                                 # number of records processed in 
                                                                 # the bibliography.
    print("="*80)
    return(bibDic) # Returns the dictionary that was created. 

# CONVERSION FUNCTIONS
# Saves dictionary into CSV, JSON, YAML.

import json
def convertToJSON(bibTexFile): # Takes the bibliography file as a variable.
    data = bibLoad(bibTexFile) # Loads the BibTex file into the dictionary
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9: # Saves it as a JSON file
                                 # Replaces .bib extension with .json, it's given a key to write, states
                                 # the encoding.    
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False) # The data is saved into variable f9.
                            # Last part sorts the data alphabetically by keys, indent=4 will create a readable JSON.
                            # When saving unicode data, the special characters will need to be displayed. 


import yaml # Same as JSON conversion.
def convertToYAML(bibTexFile):
    data = bibLoad(bibTexFile)
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:
        yaml.dump(data, f9)

# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    data = bibLoad(bibTexFile)
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date'] # A header needs to be created and the
                 # fields to be saved need to be determined. Insufficient, may need to be updated.
    header = "\t".join(headerList) # Creates the header, changes it into a string and each item
            # is separated with a tab.

    dataNew = [header] # The first element is the header.

    for k,v in data.items(): # Starts looking through the key value pairs.
        citeKey = k # citeKey is the key in the dictionary.

        if 'rType' in v: # When unsure if the record actually has the types.
            rType = v['rType'] # If rType is a value then it'll pull out that value.
        else:
            rType = "NA" # If not, no data is created

        if 'author' in v: # The above is repeated for each of the values.
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"

        tempVal = "\t".join([citeKey, rType, author, title, date]) # Creates a temporary value, 
            # a list (in the same order) and adds the values to the tab.
        dataNew.append(tempVal) # Appends that value to data

    finalData = "\n".join(dataNew) # Appends that value to data
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:
        # Converts the list of new data into a big string. Replaces the .bib extension with .csv
        # and runs it. File name remains the same, just a different extension (same data, different format)
        f9.write(finalData)


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

convertToJSON(settings["bib_all"]) # This converts the file into .json
convertToYAML(settings["bib_all"]) # Converts the file into .yaml
convertToCSV(settings["bib_all"])  # Converts the file into .csv


print("Done!")