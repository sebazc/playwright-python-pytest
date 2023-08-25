class HomePage:
    
    def __init__(self, page):
        self.page = page
        self.shop_mens_outerwear_field = self.page.locator('div:nth-child(2) > shop-button > a')
        self.shop_ladies_outerwear_field = self.page.locator('div:nth-child(3) > shop-button > a')
        self.shop_mens_tshirts_field = self.page.locator('div:nth-child(4) > shop-button > a')
        self.shop_ladies_tshirts_field = self.page.locator('div:nth-child(5) > shop-button > a')
    
    def go_to_mens_outerwear_page(self):
        self.shop_mens_outerwear_field.click()

    def go_to_ladies_outerwear_page(self):
        self.shop_ladies_outerwear_field.click()

    def go_to_mens_tshirts_page(self):
        self.shop_mens_tshirts_field.click()

    def go_to_ladies_tshirts_page(self):
        self.shop_ladies_tshirts_field.click()
