from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

timeout = 10
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
########################################################################################################################
########################################################################################################################
def selector_visible(context, _element, _type):
    if _type == "selector":
        selected_element = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, _element))
            )
    
    elif _type == "id":
        selected_element = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.ID, _element))
            )

    elif _type == "xpath":
        selected_element = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.XPATH, _element))
            )
    
    elif _type == "text":
        xsearch = "//*[text()=" + '"' + _element + '"' + "]"
        selected_element = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.XPATH, xsearch))
            )

    elif _type == "name":
        selected_element = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.NAME, _element))
            )
        
    return selected_element



@when(u'scrolling has stopped')
# function that waits until scrolling down the page has stopped
def step_impl(context):
    initial_scroll_position = context.driver.execute_script("return window.scrollY;")

    seconds = 0.0
    _scrolling = True
    while _scrolling and seconds < timeout:
        if initial_scroll_position:
            _scrolling = False
        after_click_scroll_position = context.driver.execute_script("return window.scrollY;")
        initial_scroll_position = after_click_scroll_position
        seconds += 0.1
        time.sleep(0.1)




########################################################################################################################
########################################################################################################################
def download_wait(fname_start, fname_end, path_to_downloads = os.getcwd()):
    seconds = 0
    dl_wait = True
    time.sleep(1)
    while dl_wait and seconds < timeout:
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.startswith(fname_start) and fname.endswith(fname_end):
                dl_wait = True
        seconds += 1
    return seconds

def download_delete(fname_start, fname_end, path_to_downloads = os.getcwd()):
    for fname in os.listdir(path_to_downloads):
        if fname.startswith(fname_start) and fname.endswith(fname_end):
            os.remove(fname)



@then(u'I can download the displayed video "{video_name}"')
def step_impl(context, video_name):
    video_name = video_name.split('.')
    # get link to video download
    download_link = WebDriverWait(context.driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'video'))
        ).get_attribute('src')
    # download video
    context.driver.get(download_link)    
    download_wait(video_name[0], video_name[1])
    # delete downloaded video
    download_delete(video_name[0], video_name[1])



@when(u'I swipe left on a button')
def step_impl(context, _element, _type):
    _selected_element = selector_visible(context, _element, _type)
    download_button = context.driver.find_element(By.XPATH, _selected_element)
    actions = ActionChains(context.driver)
    actions.drag_and_drop_by_offset(download_button, -80, 0)
    actions.perform()
