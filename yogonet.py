import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from bs4 import BeautifulSoup
import time
from google.cloud import bigquery
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("yogonet_scraper.log"), logging.StreamHandler()],
)

# Google Cloud authentication and BigQuery setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "yogonet-scraper-project-6f172d39e329.json"
client = bigquery.Client()
TABLE_ID = "yogonet-scraper-project.scraper_dataset.scraper_table"  # Replace with your table ID

# Selenium setup
CHROME_DRIVER_PATH = r"C:\Users\USUARIO\Desktop\chromedriver-win64\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Data storage
scraped_data = []


def scrape_section(section_url):
    """
    Scrapes all pages of a given section on Yogonet.

    Args:
        section_url (str): URL of the section to scrape.
    """
    try:
        driver.get(section_url)
        time.sleep(2)

        logging.info(f"Starting scraping for section: {section_url}")

        while True:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            news_items = soup.find_all("div", class_="item_noticias")

            for item in news_items:
                try:
                    kicker_raw = item.find("div", class_="volanta_item_listado_noticias").get_text(strip=True) if item.find("div", class_="volanta_item_listado_noticias") else None
                    date = kicker_raw[:10] if kicker_raw and len(kicker_raw) >= 10 and kicker_raw[:10].count('-') == 2 else None
                    kicker = kicker_raw[10:].strip() if kicker_raw else None

                    title_element = item.find("h2", class_="titulo_item_listado_noticias")
                    title = title_element.get_text(strip=True) if title_element else None
                    href = title_element.find("a")["href"] if title_element and title_element.find("a") else None

                    image_element = item.find("div", class_="imagen_item_listado_noticias")
                    image_url = image_element.find("img")["src"] if image_element and image_element.find("img") else None

                    scraped_data.append({
                        "Section": section_url,
                        "Date": date,
                        "Kicker": kicker,
                        "Title": title,
                        "Href": href,
                        "Image_URL": image_url,
                    })
                except Exception as e:
                    logging.error(f"Error processing item: {e}")

            # Find the "Next" button and navigate to the next page
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, ".pagination .next a")
                next_button.click()
                time.sleep(2)
                logging.info("Navigated to the next page.")
            except NoSuchElementException:
                logging.info(f"No more pages to scrape for section: {section_url}")
                break

    except Exception as e:
        logging.error(f"Error scraping section {section_url}: {e}")
