from playwright.sync_api import expect

def test_click_right_button(page):
    page.goto("https://www.automationexercise.com/")
    page.pause()
    page.get_by_role("link", name="Website for automation").click(button="right")
    page.pause()

def test_click_position_parameter(page):
    page.goto("https://www.automationexercise.com/")
    page.pause()
    page.get_by_role("link", name="Website for automation").click(position={"x":10, "y":10})
    page.pause()

def test_click_modifiers_parameter(page):
    page.goto("https://www.automationexercise.com/")
    page.get_by_role("link", name="(5) H&M").click(modifiers=["Control"])
    page.pause()

def test_click_force(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_role("button", name="Primary").nth(1).click(force=True)

def test_click_timeout(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_role("button", name="Primary").nth(1).click(timeout=5000)

def test_fill(page):
    page.goto("https://www.automationexercise.com/login")
    page.pause()
    page.get_by_role("textbox", name="Name").fill("Katarzyna", timeout=10000)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("kkowalska@test.com")
    page.get_by_role("button", name="Signup").click()

def test_check_uncheck(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").check()
    page.get_by_role("checkbox", name="Default checkbox").uncheck()

def test_select_option(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_label("Example select").select_option("2")
    page.get_by_label("Example multiple select").select_option(["2", "3"])

def test_press(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_placeholder("name@example.com").fill("kkowalska@test.com")
    page.get_by_placeholder("name@example.com").press("Tab")
    page.keyboard.type("1234")

def test_press_multiple(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_role("textbox", name="Example textarea").fill("This is an example text")
    page.get_by_role("textbox", name="Example textarea").press("Control+A")
    page.get_by_role("textbox", name="Example textarea").press("Control+C")
    page.get_by_placeholder("name@example.com").press("Control+V")
    page.pause()

def test_type(page):
    page.goto("https://www.bootswatch.com/default/")
    page.pause()
    page.get_by_role("textbox", name="Example textarea").type("This is an example text to be typed.", delay=150)

def test_hover(page):
    page.goto("https://www.automationexercise.com/")
    page.pause()
    page.locator(".single-products:visible").filter(has_text = "Madame Top For Women").hover()
    page.locator("div:nth-child(9) > .product-image-wrapper > .single-products > .productinfo > .btn").click()

def test_dblclick(page):
    page.goto("https://www.automationexercise.com/login")
    page.pause()
    page.locator(".login-form h2").dblclick()

def test_expect(page):
    page.goto("https://www.automationexercise.com/")
    #page.pause()
    page.locator(".single-products:visible").filter(has_text="Madame Top For Women").hover()
    page.locator("div:nth-child(9) > .product-image-wrapper > .single-products > .productinfo > .btn").click()
    expect(page.locator("#cartModal")).to_contain_text("Your product has been added to cart.", timeout=10000)
    expect(page.get_by_role("button", name="Continue Shopping")).to_be_visible()
    expect(page.get_by_role("button", name="Continue Shopping")).to_be_enabled()
    page.get_by_role("button", name="Continue Shopping").click()
    expect(page.locator("#cartModal")).not_to_be_visible()