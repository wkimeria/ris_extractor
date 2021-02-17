#!/usr/bin/env python3
import os
import rispy
import argparse
import sys
 
# Make sure rispy is installed via python3 -m pip install rispy          
def main():  
    
    # Get input arguments
    parser = argparse.ArgumentParser(description='Given a list of accession numbers in a file, extract records that match those ids')
    
    parser.add_argument("-i", "--input_file", type=str, help="The path to the file that contains the accession numbers to search for", required=True)
    parser.add_argument("-d", "--data_file", type=str, help="The path to the data file. Should be in .ris format", required=True)
    parser.add_argument("-o", "--output_file", type=str, help="The path to the output file for records taht match. Will be in .ris format", required=True)
    
    input_file = ''
    data_file = ''
    output_file = ''
    
    try:
        args = parser.parse_args()
        
        input_file = args.input_file
        data_file = args.data_file
        output_file = args.output_file
        
    except:
        parser.print_help()
        sys.exit(0)
        
    # Get list of accession ids from input file
    accession_no_list = []
    try:
        accession_no_list = [line.strip() for line in open(input_file)]
    except:
        print(f'Unable to open input file {input_file}')
        sys.exit(0)
        
    # Interate over data file and if ids is one specificed in the id file add to list
    selected_records = []
    try:
        with open(data_file, 'r') as bibliography_file:
            entries = rispy.load(bibliography_file)
            for entry in entries:
                if entry['accession_number'] in accession_no_list:
                    selected_records.append(entry)         
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
    # This is pretty inefficient. We are storing the selected records to a list
    # and this list could get huge!
    try:
        with open(output_file, 'w') as output_file:
            rispy.dump(selected_records, output_file)
    except OSError as err:
        print("OS error: {0}".format(err))
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__": main()