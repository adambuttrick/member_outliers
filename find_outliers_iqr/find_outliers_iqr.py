import csv
import argparse


def load_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def calculate_iqr(values):
    values.sort()
    q1 = values[int(len(values) * 0.25)]
    q3 = values[int(len(values) * 0.75)]
    iqr = q3 - q1
    return iqr, q1, q3


def identify_outliers(journal_metrics, works):
    outliers = []
    journal_dict = {journal["ISSN"]: journal for journal in journal_metrics}

    # Get the IQR, lower and upper bounds for referenced_by
    referenced_by = [float(work["Referenced by Count"]) for work in works]
    iqr_referenced_by, q1_referenced_by, q3_referenced_by = calculate_iqr(
        referenced_by)

    for work in works:
        issn = work["ISSN Details"]
        ref_by_value = float(work["Referenced by Count"])
        quartile = int(journal_dict[issn]["Quartile"]
                       ) if issn in journal_dict else None

        # Set the IQR multipliers based on the quartile
        if quartile == 1:
            lower_multiplier, upper_multiplier = 2, 2
        elif quartile in [2, 3]:
            lower_multiplier, upper_multiplier = 1.5, 1.5
        else:
            lower_multiplier, upper_multiplier = 1, 1

        # Determine if values are outside IQR bounds for referenced_by
        if ref_by_value < q1_referenced_by - lower_multiplier * iqr_referenced_by or \
           ref_by_value > q3_referenced_by + upper_multiplier * iqr_referenced_by:
            outliers.append(work)
    return outliers


def save_to_csv(data, headers, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Identify outlier works from a CSV dataset using IQR method on 'Referenced by Count'.")
    parser.add_argument("-j", "--journal_metrics", type=str,
                        help="Path to the journal metrics CSV file.", required=True)
    parser.add_argument("-w", "--works", type=str,
                        help="Path to the works CSV file.", required=True)
    parser.add_argument("-o", "--output", type=str,
                        help="Path to save the outliers CSV file.", default='outliers.csv')
    return parser.parse_args()


def main():
    args = parse_arguments()
    works = load_data(args.works)
    journal_metrics = load_data(args.journal_metrics)
    outliers = identify_outliers(journal_metrics, works)
    headers = works[0].keys() if works else []
    save_to_csv(outliers, headers, args.output)

    print(f"Outliers saved to {args.output}")


if __name__ == "__main__":
    main()
