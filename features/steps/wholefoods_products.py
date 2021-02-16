from selenium.webdriver.common.by import By
from behave import given, then

# Select products only in the bottom section
PRODUCTS = (By.XPATH, "//ul[contains(@class, 's-col-3')]//div[contains(@class, 'a-padding-extra')]")


@given('Open the Wholefoods page')
def open_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify every product has a text "{text}" and a product name')
def check_products(context, text):
    products = context.driver.find_elements(*PRODUCTS)
    for product in products:
        regular_price = product.find_element(By.XPATH, ".//span[contains(@class, 'regular-price')]").text
        assert text in regular_price, f"A product doesn't have a text '{text}'"

        name = product.find_elements(By.XPATH, ".//span[contains(@class, 'product-name')]")
        assert name, "A product name has been not found"

