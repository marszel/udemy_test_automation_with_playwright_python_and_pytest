def test_open_google(page):
    page.goto("https://www.google.com")
    page.pause()
    print(page.title())
    assert "Google" in page.title()