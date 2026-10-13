# def test_new_window(page):
#     page.goto("https://demoqa.com/browser-windows")
#     with page.expect_popup() as window_info:
#         page.locator("#windowButton").click()
#
#     new_window = window_info.value
#     new_window.wait_for_load_state()
#
#     new_window.screenshot(path="new_window.png")
#
#     new_window.close()

def test_new_window(page):
    page.goto("https://demoqa.com/browser-windows")
    page.locator("#windowButton").click()
    page.locator("#windowButton").click()
    page.locator("#windowButton").click()
    page.wait_for_timeout(2000)
    context = page.context #from the context we have access to all windows or tabs we open in our browser

    print(context.pages)

    new_window = context.pages[3]

    new_window.screenshot(path="new_window.png")
    new_window.close()
