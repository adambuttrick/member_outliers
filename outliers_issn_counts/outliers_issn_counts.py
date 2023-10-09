import csv
import argparse


def read_csv(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)
    return headers, data


def extract_and_count_issn(headers, data):
    issn_index = headers.index("ISSN Details")
    journal_index = headers.index("Journal Title")
    issn_counts = {}
    for row in data:
        issns = row[issn_index].strip()
        journal = row[journal_index]
        if issns:
            key = (issns, journal)
            issn_counts[key] = issn_counts.get(key, 0) + 1  
    return issn_counts


def generate_csv(output_file, issn_counts):
    with open(output_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ISSN", "Journal Title", "Count"])
        for (issn, journal), count in issn_counts.items():
            writer.writerow([issn, journal, count])


def parse_args():
    parser = argparse.ArgumentParser(description='Process a CSV to count ISSN occurrences.')
    parser.add_argument('-i','--input_file', required=True, help='Path to the input CSV file.')
    parser.add_argument('-o','--output_file', default='outliers_issn_counts.csv', help='Path to the output CSV file.')
    return parser.parse_args()


def main():
    args = parse_args()
    headers, data = read_csv(args.input_file)
    issn_counts = extract_and_count_issn(headers, data)
    generate_csv(args.output_file, issn_counts)


if __name__ == "__main__":
    main()