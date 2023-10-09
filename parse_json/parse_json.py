import argparse
import json
import csv
import os
import glob


def get_all_json_files(directory):
    return glob.glob(os.path.join(directory, "*.json"))


def extract_data_from_json(json_path):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    extracted_data = []
    for item in data["message"]["items"]:
        title = item.get("title", [""])[0]
        authors = "; ".join([f"{author.get('given', '')} {author.get('family', '')}" for author in item.get("author", [])])
        doi = item.get("DOI", "")
        creation_date = item.get("created", {}).get("date-time", "")
        related_references = "; ".join(
            [ref["DOI"] for ref in item.get("reference", []) if "DOI" in ref])
        total_references = len(item.get("reference", []))
        is_referenced_by = item.get("is-referenced-by-count", 0)
        journal_title = item.get("container-title", [""])[0]
        links = "; ".join([link.get("URL", "")
                           for link in item.get("link", [])])
        publication_date = item.get("published", {}).get(
            "date-parts", [[""]])[0][0]
        issn_details = "; ".join([issn.get("value", "")
                                  for issn in item.get("issn-type", [])])
        if journal_title:
            extracted_data.append([title, authors, doi, creation_date, related_references, total_references,
                                   is_referenced_by, journal_title, links, publication_date, issn_details])
    return extracted_data


def write_data_to_csv(data, csv_path):
    headers = ["Title", "Authors", "DOI", "Creation Date", "Related References (DOIs)",
               "Total Count of References", "Referenced by Count", "Journal Title", "Links", "Publication Date", "ISSN Details"]
    with open(csv_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(data)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert JSON files from a directory into a single CSV file.")
    parser.add_argument("-d", "--directory",
                        help="Directory containing JSON files.")
    parser.add_argument("-o", "--output_csv",
                        help="Path to save the generated CSV file.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    all_json_files = get_all_json_files(args.directory)
    all_data = []
    for json_file in all_json_files:
        all_data.extend(extract_data_from_json(json_file))
    write_data_to_csv(all_data, args.output_csv)


if __name__ == "__main__":
    main()
