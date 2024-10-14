Bloobhound Split Script
This script is designed to split a large JSON file containing computer data into smaller chunks. Each chunk will be saved as a separate JSON file.

Prerequisites
Python 3.x
JSON file named 20210312152708_computers.json in the same directory as the script
How to Use
Place the JSON file (20210312152708_computers.json) in the same directory as the script.
Run the script using Python:
Script Details
Input File: The script reads from a JSON file named 20210312152708_computers.json.
Object Type: The script processes objects of type computers.
Object Limit: Each output file will contain up to 10,000 computer objects.
Output
The script will generate multiple JSON files, each containing a subset of the original data.
The output files will be named in the format 20210312152708_computers_X.json, where X is the file count starting from 0.
Example
If the input file contains 25,000 computer objects, the script will generate the following files:

20210312152708_computers_0.json (10,000 objects)
20210312152708_computers_1.json (10,000 objects)
20210312152708_computers_2.json (5,000 objects)
Notes
Ensure the input JSON file is correctly formatted and contains the expected structure.
The script assumes the JSON file has a meta field with a count key indicating the total number of objects.
License
This script is provided "as-is" without any warranty. Use at your own risk.
