from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

url = "https://www.bikereg.com/Confirmed/72109"
#offsetParent
try:
    # Initialize Chrome driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(2)
    
    # Find and click the header using multiple strategies (like Puppeteer's race)
    wait = WebDriverWait(driver, 10)
    
    # Try XPath first (most reliable from the record)
    try:
        click_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='confirmedcontent']/div[2]/div[13]/table/thead/tr/th/div[2]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", click_element)
        # Use JavaScript click to bypass overlay issues
        driver.execute_script("arguments[0].click();", click_element)
        print("Clicked using XPath (JavaScript)")
    except:
        # Fallback: find by text content
        try:
            click_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'WAITLISTS - 62 mile - Men')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", click_element)
            driver.execute_script("arguments[0].click();", click_element)
            print("Clicked using text content (JavaScript)")
        except Exception as e:
            print(f"Could not find clickable element: {e}")
            raise
    
    # Wait for the table to load after clicking
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.XPATH, "///*[@id='confirmedcontent']/div[2]/div[13]/table/thead/tr/th/div[2]")))
    
    # Parse the loaded HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table_element = soup.find('table')
    
    if table_element:
        rows = table_element.find_all('tr')[1:]  # Skip header row
        print(f"Found {len(rows)} rows in the table")
        
        for index, row in enumerate(rows, 1):
            cells = row.find_all('td')
            if cells and len(cells) > 0:
                name = cells[0].get_text(strip=True)
                if 'August Miller' in name or 'miller' in name.lower():
                    print(f"August Miller found at position: {index}")
                    break
        else:
            print("August Miller not found in the waitlist")
    else:
        print("Table not found after clicking header")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()