from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math
driver = webdriver.Chrome()
# driver.get('https://www.daraz.pk/products/2023-i558705405-s3417661997.html')
driver.get('https://www.daraz.pk/products/o-i550406688-s2562059926.html')
time.sleep(10)
driver.maximize_window()


height = driver.execute_script("return document.body.scrollHeight")

for i in range(1, height, 500):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(1)


total_ratings_text = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[3]').text
total_ratings = int(total_ratings_text.split()[0]) 
total_page = math.ceil(total_ratings / 5)
print(total_page,'total pages')
comments = []
for i in range(1, total_page + 1):
    elements = driver.find_elements(By.CSS_SELECTOR, '.item-content .content')
    for item in elements:
        comments.append(item.text)
    try:
        current_elem = driver.find_element(By.CSS_SELECTOR, ".review-pagination .next-btn.next-btn-normal.next-btn-medium.next-pagination-item.current")
        if current_elem:
            next_elem = current_elem.find_element(By.XPATH, "following-sibling::button[1]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", current_elem)
            time.sleep(10)
            next_elem.click()
            time.sleep(10)
    except:
        break        
print("Total",len(comments))
print(comments)
time.sleep(5)
driver.quit()

