### Description:
This script processes a CSV file containing outlier research works, as identified by the `find_outliers_iqr.py` script. It counts occurrences of each ISSN and the associated journal title, providing insights into which journals have the most outlier works. The results are saved in a new CSV file.

### How to Run:
   ```bash
   python outliers_issn_counts.py -i <INPUT_CSV_PATH> -o <OUTPUT_CSV_PATH>
   ```

### Arguments:

- `-i` or `--input_file`: Path to the input CSV file containing outlier works. (Required)
- `-o` or `--output_file`: Path where the ISSN counts CSV file will be saved. Default is `outliers_issn_counts.csv`. (Optional)

### Output:
The script will produce a CSV file with the following headers:

1. ISSN
2. Journal Title
3. Count (number of outlier works for the ISSN)
