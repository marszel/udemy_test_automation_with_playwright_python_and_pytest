def test_get_by_role(page):
    page.goto("https://www.automationexercise.com")
    page.get_by_role("link", name=' Signup / Login').click()
    page.get_by_role("button", name="Login").click()

def test_get_by_role_with_id(page):
    page.goto("https://www.bootswatch.com/default/")
    page.locator("#navbarColor01").get_by_role("button", name="Dropdown").click()

def test_get_by_text(page):
    page.goto("https://www.automationexercise.com")
    page.get_by_text("Full-Fledged practice website for Automation Engineers", exact=True).first.click()

def test_get_by_label(page):
    page.goto("https://www.bootswatch.com/default/")
    page.get_by_label("Valid input", exact=True).fill("Test")
    page.get_by_label("Recipient's username", exact=True).fill("Test")

def test_get_by_placeholder(page):
    page.goto("https://www.automationexercise.com/login")
    page.get_by_placeholder("Name").fill("Test")

def test_get_by_title(page):
    page.goto("https://www.bootswatch.com/default/")
    page.get_by_title("Source Title").nth(1).click()

def test_locator_css(page):
    page.goto("https://www.automationexercise.com")
    page.locator("#accordian .panel-title").first.click()

def test_locator_xpath(page):
    page.goto("https://www.automationexercise.com/login")
    page.locator('//*[@id="form"]/div/div/div[1]/div/form/button').click()