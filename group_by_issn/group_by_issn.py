import csv
import argparse
from statistics import median


def read_csv(file_path):
    with open(file_path, mode='r+', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def group_by_issn(data):
    grouped = {}
    for row in data:
        issn = row["ISSN Details"]
        if issn not in grouped:
            grouped[issn] = []
        grouped[issn].append(row)
    return grouped


def calculate_median(values):
    return median(values)


def determine_quartile(journal, medians):
    above_median_count = 0
    metrics = ["Total DOIs", "Median of Total Count of References",
               "Median of Referenced by Count"]
    for metric in metrics:
        if journal[metric] > medians[metric]:
            above_median_count += 1
    if above_median_count == 3:
        return 1
    elif above_median_count == 2:
        return 2
    elif above_median_count == 1:
        return 3
    else:
        return 4


def process_data(grouped_data):
    summarized_data = []
    for issn, records in grouped_data.items():
        doi_count = len(set(record["DOI"] for record in records))
        median_references = calculate_median(
            [int(record["Total Count of References"]) for record in records])
        median_referenced_by = calculate_median(
            [int(record["Referenced by Count"]) for record in records])
        summarized_data.append({
            "ISSN": issn,
            "Total DOIs": doi_count,
            "Median of Total Count of References": median_references,
            "Median of Referenced by Count": median_referenced_by
        })

    medians = {
        "Total DOIs": calculate_median([journal["Total DOIs"] for journal in summarized_data]),
        "Median of Total Count of References": calculate_median([journal["Median of Total Count of References"] for journal in summarized_data]),
        "Median of Referenced by Count": calculate_median([journal["Median of Referenced by Count"] for journal in summarized_data])
    }

    for journal in summarized_data:
        journal["Quartile"] = determine_quartile(journal, medians)
        journal["Difference from Median (DOIs)"] = journal["Total DOIs"] - \
            medians["Total DOIs"]
        journal["Difference from Median (References)"] = journal["Median of Total Count of References"] - \
            medians["Median of Total Count of References"]
        journal["Difference from Median (Referenced by)"] = journal["Median of Referenced by Count"] - \
            medians["Median of Referenced by Count"]
    return summarized_data


def write_to_csv(summarized_data, output_path):
    headers = [
        "ISSN",
        "Total DOIs",
        "Median of Total Count of References",
        "Median of Referenced by Count",
        "Quartile",
        "Difference from Median (DOIs)",
        "Difference from Median (References)",
        "Difference from Median (Referenced by)"
    ]
    with open(output_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for record in summarized_data:
            writer.writerow(record)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Process a CSV of research works and cluster by ISSN.")
    parser.add_argument("-i", "--input_file", type=str,
                        help="Path to the input CSV file.", required=True)
    parser.add_argument("-o", "--output_file", type=str,
                        help="Path to the output CSV file.", default="grouped_by_issn.csv")
    return parser.parse_args()


def main():
    args = parse_arguments()
    data = read_csv(args.input_file)
    grouped_data = group_by_issn(data)
    summarized_data = process_data(grouped_data)
    write_to_csv(summarized_data, args.output_file)


if __name__ == "__main__":
    main()
