from playwright.sync_api import expect


def test_import_file(page):
    page.goto("https://www.transfernow.net/en")
    page.get_by_role("button", name="Reject").click()
    with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="Start").click()
    file_chooser = fc_info.value
    file_chooser.set_files("stores/test_register_new_user/test1234.txt")
    page.get_by_role("button", name="Create a link").click()
    page.get_by_role("textbox", name="Your email address").fill("test643647@test.com")
    page.get_by_role("button", name="Get a link").click()
    expect(page.get_by_text("Your link is ready!")).to_be_visible()

def test_import_multiple_files(page):
    page.goto("https://www.transfernow.net/en")
    page.get_by_role("button", name="Reject").click()
    with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="Start").click()
    file_chooser = fc_info.value
    file_chooser.set_files(["stores/test_register_new_user/test1234.txt",
                           "stores/test_register_new_user/test4321.txt"])
    page.get_by_role("button", name="Create a link").click()
    page.get_by_role("textbox", name="Your email address").fill("test643647@test.com")
    page.get_by_role("button", name="Get a link").click()
    expect(page.get_by_text("Your link is ready!")).to_be_visible()