from playwright.sync_api import expect

def test_iframe(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

    iframe = page.frame_locator("#iframeResult")
    inner_iframe = iframe.frame_locator("[src='demo_iframe.htm']")
    expect(inner_iframe.locator("h1")).to_have_text("This page is displayed in an iframe")
