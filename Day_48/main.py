from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://produto.mercadolivre.com.br/MLB-5138317934-cortina-box-banheiro-antimofo-varo-extensivel-110-a-2m-_JM?searchVariation=182018788272#polycard_client=bookmarks")

#  TO DO:FIGURE OUT HOW TO RETRIVE THE REDUCED PRICE, NOT THE ORIGINAL
# State variables for price
price_dollar = driver.find_element(By.CLASS_NAME, value="andes-money-amount__fraction")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"the price is {price_dollar.text}")

# Close singular tab
# driver.close()

# Closes entire tab
driver.quit()