from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

# Function to wait until element appear
def waitForElement(e):
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(e)
    )

def waitForElementClickable(e):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(e)
    )

# Variable and Dictionary
author = 'J.K. Rowling'
quotesDict = {
    author: {
        'birth_date': '',
        'born': '',
        'description': '',
        'quotes': []
    }
}

try:
    # Connection net
    options= webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get('http://quotes.toscrape.com/')

    waitForElement((By.CLASS_NAME, 'quote'))

    page, lastPage = 1, False

    # Page for page, searching for author's quotes
    while True:
        driver.get(f'https://quotes.toscrape.com/page/{page}/')
        
        # If won't exists "next" button, then finished quotes
        try:
            driver.find_element(By.XPATH, '//li[@class="next"]/a').text
        except NoSuchElementException:
            lastPage = True
    
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')
        
        waitForElement((By.CLASS_NAME, 'text'))
        
        for qn, q in enumerate(quotes):
            #print(q.text)
            if q.text.find(author) >= 0:
                #print(q.text)
                if len(quotesDict[author]['birth_date']) == 0:      # If (about) is empty...
                    waitForElementClickable((By.TAG_NAME, 'a')) # Wait Time
                    q.find_element(By.TAG_NAME, 'a').click()    # Click (about) section
                    waitForElement((By.CLASS_NAME, 'author-born-date')) # Wait Time
                    # Storing (about) on dict
                    quotesDict[author]['birth_date'] = driver.find_element(By.CLASS_NAME, 'author-born-date').text
                    quotesDict[author]['born'] = driver.find_element(By.CLASS_NAME, 'author-born-location').text
                    quotesDict[author]['description'] = driver.find_element(By.CLASS_NAME, 'author-description').text
                    # Get back
                    driver.back()
                # Get quote
                waitForElement((By.CLASS_NAME, 'text'))
                quote = q.find_element(By.CLASS_NAME, 'text').text
                # Get Tags
                tags = []
                waitForElement((By.CLASS_NAME, 'tag'))
                for tag in q.find_elements(By.CLASS_NAME, 'tag'):
                    tags.append(tag.text)
                # Storing quote and tags on dict
                quotesDict[author]['quotes'].append({'text':quote, 'tags':tags})

        if lastPage:
            break

        page += 1

    print('\n\n==========RESULTADO==========\n')
    print(quotesDict)

    driver.quit()
    print('\n\n~~~~~~~~~ Fim do programa ~~~~~~~~~\n')
except KeyboardInterrupt:
    print('\n\n~~~~~~~~~ Fim do programa ~~~~~~~~~\n')
except Exception as err:
    print('ERRO: ', str(err))