from selenium.webdriver.common.by import By
from behave import given, then

COLORS = (By.XPATH, "//li[starts-with(@id, 'color_name')]")
SELECTED_COLOR = (By.XPATH, "//span[@class='selection']")


@given('Open Amazon Jean {product} page')
def open_amazon_product_page(context, product):
    context.driver.get(f'https://www.amazon.com/gp/product/{product}/')


@then('Verify user can click through colors')
def click_colors(context):
    colors = context.driver.find_elements(*COLORS)

    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        expected_color = color.get_attribute("title").split(" ", 3)[3]
        assert expected_color == selected_color, f"Expected {expected_color}, but got {selected_color}"

