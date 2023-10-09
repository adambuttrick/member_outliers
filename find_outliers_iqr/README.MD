### Description:
Identifies outlier research works from two provided CSV datasets using the Interquartile Range (IQR) method, specifically on the 'Referenced by Count' metric. It then saves these outliers to a new CSV file. Outliers are determined differently based on the quartile of the journal in which the work is published.


### How to Run:
   ```bash
   python find_outliers_iqr.py -j <JOURNAL_METRICS_CSV> -w <WORKS_CSV> -o <OUTPUT_CSV_PATH>
   ```

### Arguments:

- `-j` or `--journal_metrics`: Path to the CSV file containing journal metrics. (Required)
- `-w` or `--works`: Path to the CSV file containing individual works details. (Required)
- `-o` or `--output`: Path where the outliers CSV file will be saved. Default is `outliers.csv`.

### Output:
The script will produce a CSV file that lists the outlier works. The structure of this CSV will be similar to the `works` CSV file input.

### Outliers Identification:
The script uses the Interquartile Range (IQR) method on the 'Referenced by Count' metric to determine outliers. Depending on the quartile of the journal in which a work is published, the boundaries for outlier detection may vary:

1. Quartile 1: Multipliers of 2 for both upper and lower bounds.
2. Quartile 2 & 3: Multipliers of 1.5 for both bounds.
3. Quartile 4: Multipliers of 1 for both bounds.

A work is considered an outlier if its 'Referenced by Count' value falls below the lower bound or above the upper bound calculated using the above multipliers.

