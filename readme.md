# Web Scraping and Badge Counting Script

This Python script scrapes job listings from the web3.career website and counts the occurrence of badges associated with each job. The script utilizes the BeautifulSoup library for web scraping and Pandas for data manipulation. It also saves the badge counts to a CSV file.

## Prerequisites

Before running this script, make sure you have the following libraries installed:

- `csv`
- `pandas`
- `requests`
- `beautifulsoup4`

You can install these libraries using pip:

```bash
pip install pandas requests beautifulsoup4
```

## Usage

1. Clone or download this repository to your local machine.

2. Run the script using Python:

```bash
python scrap.py
```

The script will fetch job listings from the specified URL and count the badges associated with each job. It will also print the top 50 most common badges and save the badge counts to a CSV file named `badges.csv`.

## Script Explanation

- The script defines a `badges_list` to store badge names and initializes variables for job statistics.

- It calculates the number of pages needed to scrape based on the total number of jobs and jobs per page.

- It then iterates through each page, sending a GET request and parsing the HTML using BeautifulSoup.

- The script extracts job listings and iterates through each job to find badges, adding them to the `badges_list`.

- It defines a function `countOccurrence` to count badge occurrences.

- The script counts badge occurrences and creates a Pandas DataFrame to display the 50 most common badges.

- Finally, it saves the badge counts to a CSV file named `badges.csv`.

Please make sure to adjust the script according to your specific needs and website structure.