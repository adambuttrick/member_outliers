### Description:
Process the CSV file returned by the `parse_json.py` containing member works, group these works by their respective ISSN, and then generate summarized metrics for each ISSN. The metrics include the total number of DOIs, the median of references, the median of 'referenced by count', and their respective quartile rankings.

### How to Run:

   ```bash
   python group_by_issn.py -i <INPUT_CSV_PATH> -o <OUTPUT_CSV_PATH>
   ```

### Arguments:

- `-i` or `--input_file`: Path to the input CSV file that contains research works details. (Required)
- `-o` or `--output_file`: Path where the summarized CSV file will be saved.

### Output:
The script will produce a CSV file with the following headers:

1. ISSN
2. Total DOIs
3. Median of Total Count of References
4. Median of Referenced by Count
5. Quartile
6. Difference from Median (DOIs)
7. Difference from Median (References)
8. Difference from Median (Referenced by)

### How the Quartile is Determined:
The script uses three metrics (Total DOIs, Median of Total Count of References, and Median of Referenced by Count) to determine the quartile for each ISSN. 

- If a journal is above the median for all three metrics, it is placed in Quartile 1.
- If it is above the median for two metrics, it is in Quartile 2.
- If it's above the median for only one metric, it's in Quartile 3.
- Otherwise, it's in Quartile 4.
