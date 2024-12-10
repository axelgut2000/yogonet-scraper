# Yogonet Web Scraper

A Python-based project to scrape articles and metadata from the Yogonet platform, process the data, and export it to Google BigQuery for further analysis.

---

## Features

- Extracts articles, images, titles, and metadata.
- Handles pagination to scrape all available pages.
- Processes data to compute word and character counts.
- Exports processed data to Google BigQuery.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Common Issues](#common-issues)
6. [License](#license)

---

## Requirements

- Python 3.10+
- Google Cloud account with BigQuery setup.
- Dependencies:
  - `selenium`
  - `pandas`
  - `google-cloud-bigquery`

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yogonet-scraper.git
   cd yogonet-scraper

---

## Usage

1. **Run the Script**:
   To execute the scraper, use the following command:
   ```bash
   python yogonet.py

What It Does:

1. **Scrapes**:
    Articles, titles, images, and metadata from the Yogonet platform.

2. **Handles Pagination**:
    Navigate through all pages in a section to scrape comprehensive data.

3. **Processes Data**:
    Computes word count and character count in titles.
    Extracts capitalized words from titles.
   
4. **Exports to BigQuery**:
    Project: yogonet-scraper-project
    Dataset: scraper_dataset
    Table: scraper_table
   
5. **Logs Progress**:
    The script generates a log file (yogonet_scraper.log) that tracks:
    Sections are being scraped.
    Errors encountered.
    Progress through pagination.

---

## File Structure
  ```plaintext
    yogonet/
    ├── yogonet.py               # Main script for scraping and exporting data
    ├── requirements.txt         # Python dependencies
    ├── README.md                # Project documentation
    ├── yogonet_scraper.log      # Log file (generated after running the script)
    └── .gitignore               # Files to ignore (e.g., credentials, environment)
```

**Explanation of Key Files**
1. yogonet.py: The main Python script for web scraping and exporting data to BigQuery.
2. requirements.txt: Lists all Python dependencies required for the project.
3. README.md: Project documentation, including setup and usage instructions.
4. yogonet_scraper.log: Log file that tracks the script’s progress and errors.
5. .gitignore: Excludes unnecessary files (e.g., credentials, virtual environments) from version control.

---

## Common Issues

1. Authentication Error:

Ensure the JSON key file path is correctly set in the GOOGLE_APPLICATION_CREDENTIALS environment variable.

2. BigQuery Permissions:

Confirm the service account has the required permissions (BigQuery Data Editor).

---

## License

This project is licensed under the MIT License. Feel free to use and modify as needed.




