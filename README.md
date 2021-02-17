
# RIS Extractor

## Description
This is a script that extracts selected records from a .ris file (Bibliography file) based on the Acession Number of the record. The lis of records to extract is stored in an input file in the following format (one id per line)

```sh
1118
1054
...
```

## Installation

This script uses the Python 3.6+ Rispy Reader/writer for RIS files [Rispy](https://pypi.org/project/rispy/#description). To install the library, run
```sh
python3 -m pip install rispy 
```
or
```sh
 pip install rispy 
 ```
 
 ## Usage
 The script takes 3 input arguments 
 
 | arg | Description |
| ------ | ------ |
| -i | The path to the file that contains the accession numbers to search for |
| -d | The path to the data file. Should be in .ris format |
| -o | The path to the output file for records taht match. Will be in .ris format |

 ```sh
  python3 ris_extractor.py -i file_with_ds.prn -d data_file.ris -o output_file.ris
 ```
 
 ## Notes
 The script stores the records found in a list before outputting them at the end, so if there are a lot of records in the id file, this cound be an issue.