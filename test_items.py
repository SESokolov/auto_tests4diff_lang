import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(15)
    # find add to basket button
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"), "Button not found"