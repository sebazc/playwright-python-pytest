from playwright.sync_api import Page, expect
from pages.home_page import HomePage

def test_check_home_page(page: Page):
    home_page = HomePage(page)
    expect(page).to_have_title("Home - SHOP")

def test_check_mens_outerwear_page(page: Page):
    home_page = HomePage(page)
    home_page.go_to_mens_outerwear_page()
    expect(page).to_have_title("Men's Outerwear - SHOP")

def test_check_ladies_outerwear_page(page: Page):
    home_page = HomePage(page)
    home_page.go_to_ladies_outerwear_page()
    expect(page).to_have_title("Ladies Outerwear - SHOP")

def test_check_mens_tshirts_page(page: Page):
    home_page = HomePage(page)
    home_page.go_to_mens_tshirts_page()
    expect(page).to_have_title("Men's T-Shirts - SHOP")

def test_check_ladies_tshirts_page(page: Page):
    home_page = HomePage(page)
    home_page.go_to_ladies_tshirts_page()
    expect(page).to_have_title("Ladies T-Shirts - SHOP")
