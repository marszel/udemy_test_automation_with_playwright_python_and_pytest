import os


def test_download_files(page):
    page.goto("https://www.transfernow.net/en/cld?utm_source=20261009jyzWVmVZ")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download all").click()
    download = download_info.value
    final_path = f"stores/test_register_new_user/{download.suggested_filename}"
    download.save_as(final_path)
    page.pause()
    assert os.path.exists(final_path), "I did not find the downloaded file."