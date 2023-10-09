### Description:
Parse data from JSON files returned by the `get_member_works_by_year.py` script and convert them into a single consolidated CSV file. 


### How to Run:
   ```bash
   python parse_json.py -d <DIRECTORY_PATH> -o <OUTPUT_CSV_PATH>
   ```

### Arguments:

- `-d` or `--directory`: Directory containing the JSON files to be parsed. (Required)
- `-o` or `--output_csv`: Path where the generated CSV file will be saved. (Required)

### Output:
The script will produce a CSV file with the following headers:

1. Title
2. Authors
3. DOI
4. Creation Date
5. Related References (DOIs)
6. Total Count of References
7. Referenced by Count
8. Journal Title
9. Links
10. Publication Date
11. ISSN Details
