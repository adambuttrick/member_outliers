### Description:
Fetch and save the works of a specified member from the Crossref API for a given year.


### Requirements:
   ```bash
   pip install -r requirements.txt
   ```

### How to Run:
   ```bash
   python get_member_works_by_year.py -m <MEMBER_ID> -y <YEAR>
   ```

### Arguments:

- `-m` or `--member_id`: The ID of the member whose works you want to fetch. (Required)
- `-y` or `--year`: The publication year of the works you want to fetch. (Required)
- `-u` or `--user_agent`: The User Agent for the request. This should be in the format `mailto:name@email`. (Optional, but strongly recommended to avoid potential request limitations or blocks)
- `-t` or `--token`: The Crossref Metadata Plus API token, if you have one. (Optional)

### Output:
The script will create a directory named `member_<MEMBER_ID>_<YEAR>` in your current working directory. Inside this directory, the data will be saved in multiple JSON files named `page_<PAGE_NUMBER>.json`.

### Notes:
- The script automatically waits 1 second between consecutive requests to avoid overloading the server or hitting rate limits.
