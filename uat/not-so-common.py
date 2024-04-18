########################################################################################################################
########################################################################################################################

@when(u'scrolling has stopped')
# function that waits until scrolling down the page has stopped
def step_impl(context):
    initial_scroll_position = context.driver.execute_script("return window.scrollY;")

    seconds = 0.0
    _scrolling = True
    while _scrolling and seconds < timeout:
        after_click_scroll_position = context.driver.execute_script("return window.scrollY;")
        initial_scroll_position = after_click_scroll_position
        if initial_scroll_position:
            _scrolling = False
        seconds += 0.1
        time.sleep(0.1)






########################################################################################################################
########################################################################################################################
def download_wait(fname_start, fname_end, path_to_downloads = os.getcwd()):
    seconds = 0
    dl_wait = True
    time.sleep(1)
    while dl_wait and seconds < timeout:
        # time.sleep(1)
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
    download_link = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'video'))
        ).get_attribute('src')
    # download video
    context.browser.get(download_link)    
    download_wait(video_name[0], video_name[1])
    # delete downloaded video
    download_delete(video_name[0], video_name[1])