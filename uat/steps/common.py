from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import time


timeout = 10
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)


########################################################################################################################
########################################################################################################################
def selector_visible(context, _element, _type):
    if _type == "selector":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, _element))
            )
    
    elif _type == "id":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.ID, _element))
            )

    elif _type == "xpath":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.XPATH, _element))
            )
    
    elif _type == "text":
        xsearch = "//*[text()=" + '"' + _element + '"' + "]"
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.XPATH, xsearch))
            )

    elif _type == "name":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located((By.NAME, _element))
            )
        
    return selected_element


##################################
##################################
def selector_invisible(context, _element, _type, timeout=timeout):
    if _type == "selector":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, _element))
            )
    
    elif _type == "id":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located((By.ID, _element))
            )

    elif _type == "xpath":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located((By.XPATH, _element))
            )
    
    elif _type == "text":
        xsearch = "//*[text()=" + '"' + _element + '"' + "]"
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located((By.XPATH, xsearch))
            )

    elif _type == "name":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located((By.NAME, _element))
            )
        
    return selected_element

##################################
##################################
def selector_clickable(context, _element, _type):
    if _type == "selector":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, _element))
            )
    
    elif _type == "id":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.ID, _element))
            )

    elif _type == "xpath":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH, _element))
            )
    
    elif _type == "text":
        xsearch = "//*[text()=" + '"' + _element + '"' + "]"
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.XPATH, xsearch))
            )

    elif _type == "name":
        selected_element = WebDriverWait(context.browser, timeout, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable((By.NAME, _element))
            )
        
    return selected_element


#####################################
##################################### 
def find_all_elements(context, _element, _type):
    if _type == "selector":
        selected_elements = context.driver.find_elements(By.CSS_SELECTOR, _element)
    
    elif _type == "id":
        selected_elements = context.driver.find_elements(By.ID, _element)

    elif _type == "xpath":
        selected_elements = context.driver.find_elements(By.XPATH, _element)
    
    elif _type == "text":
        xsearch = "//*[text()=" + '"' + _element + '"' + "]"
        selected_elements = context.driver.find_elements(By.XPATH, xsearch)

    elif _type == "name":
        selected_elements = context.driver.find_elements(By.NAME, _element)
        
    return selected_elements

#####################################
##################################### 
def check_element_located(context, _type, element):
    # _type are: selector, id, text (uses xpath search), xpath
    if _type == "selector":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "id":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_element_located((By.ID, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "xpath":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_element_located((By.XPATH, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "text":
        xsearch = "//*[text()=" + '"' + element + '"' + "]"
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_element_located((By.XPATH, xsearch))
                )
        except TimeoutException:
            return False
        return True

    if _type == "name":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.visibility_of_element_located((By.NAME, element))
                )
        except TimeoutException:
            return False
        return True

#####################################
#####################################    
def check_clickable_by_element(context, _type, element):
    # _type are: selector, id, text (uses xpath search), xpath
    if _type == "selector":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "id":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.element_to_be_clickable((By.ID, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "xpath":
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.element_to_be_clickable((By.XPATH, element))
                )
        except TimeoutException:
            return False
        return True
    
    if _type == "text":
        xsearch = "//*[text()=" + '"' + element + '"' + "]"
        try:
            WebDriverWait(context.browser, 0.1, ignored_exceptions=ignored_exceptions).until(
                EC.element_to_be_clickable((By.XPATH, xsearch))
                )
        except TimeoutException:
            return False
        return True
    
########################################################################################################################
########################################################################################################################      
@when(u'I wait for the element/type "{element}"/"{_type}" to load')
@then(u'I wait for the element/type "{element}"/"{_type}" to load')
# _type are: selector, id, text (uses xpath search), xpath
# element is the name of the selector, id ect
def step_impl(context, _type, element, timeout=timeout):
    seconds = 0.0
    _wait = True
    while _wait and seconds < timeout:
        if check_element_located(context, _type, element):
            _wait = False
        seconds += 0.1
        time.sleep(0.1)
    # if it timesout, assert if the statment is true
    time.sleep(0.2)
    assert(_type)

########################################################################################################################
########################################################################################################################
@when(u'I wait for the element/type "{element}"/"{_type}" to be clickable')
# _type are: selector, id, text (uses xpath search), xpath
# element is the name of the selector, id ect
def step_impl(context, _type, element, timeout=timeout):
    seconds = 0.0
    _wait = True
    while _wait and seconds < timeout:
        if check_clickable_by_element(context, _type, element):
            _wait = False
        seconds += 0.1
        time.sleep(0.1)
    # if it timesout, assert if the statment is true
    time.sleep(0.2)
    assert(_type)

########################################################################################################################
########################################################################################################################
@when(u'The element/type "{_element}"/"{_type}" is visible')
@then(u'The element/type "{_element}"/"{_type}" is visible')
def step_impl(context, _element, _type):
    selector_visible(context, _element, _type)

########################################################################################################################
########################################################################################################################
@then(u'The element/type "{_element}"/"{_type}" is invisible')
def step_impl(context, _element, _type):
    selector_invisible(context, _element, _type, timeout=45)

########################################################################################################################
##############################         Send text to element         ####################################################
##############################         Send text to element         ####################################################
########################################################################################################################
@when(u'I send the text "{_text}" to the element/type "{_element}"/"{_type}"')
@then(u'I send the text "{_text}" to the element/type "{_element}"/"{_type}"')
def step_impl(context, _text, _element, _type):
    context.execute_steps(u'when I wait for the element/type "{element}"/"{_type}" to load'.format(element=_element, _type=_type))
    _selected_element = selector_visible(context, _element, _type)

    context.browser.execute_script("arguments[0].scrollIntoView();", _selected_element)
    
    _selected_element.send_keys(_text)

########################################################################################################################
########################################################################################################################
@when(u'I use actionChain to send the text "{_text}" to the element/type "{_element}"/"{_type}"')
@then(u'I use actionChain to send the text "{_text}" to the element/type "{_element}"/"{_type}"')

@when(u'I select the value "{_text}" from the dropdown with the element/type "{_element}"/"{_type}"')
@then(u'I select the value "{_text}" from the dropdown with the element/type "{_element}"/"{_type}"')

def step_impl(context, _text, _element, _type):
    context.execute_steps(u'when I wait for the element/type "{element}"/"{_type}" to load'.format(element=_element, _type=_type))
    
    _selected_element = selector_visible(context, _element, _type)

    actions = ActionChains(context. browser)
    actions.move_to_element(_selected_element)
    actions.click().perform()

    actions.send_keys(_text)
    actions.send_keys(Keys.RETURN)
    actions.perform()

########################################################################################################################
##############################          click on a button           ####################################################
##############################          click on a button           ####################################################
########################################################################################################################
@when(u'I use actionChain to click on the button with the element/type "{_element}"/"{_type}"')
@then(u'I use actionChain to click on the button with the element/type "{_element}"/"{_type}"')
def step_impl(context, _element, _type):
    context.execute_steps(u'when I wait for the element/type "{element}"/"{_type}" to load'.format(element=_element, _type=_type))
    
    _selected_element = selector_visible(context, _element, _type)

    context.browser.execute_script("arguments[0].scrollIntoView();", _selected_element)

    actions = ActionChains(context. browser)
    actions.move_to_element(_selected_element)
    actions.click().perform()

########################################################################################################################
########################################################################################################################
@when(u'I scroll too, and click on the button that contains the element/type "{_element}"/"{_type}"')
@then(u'I scroll too, and click on the button that contains the element/type "{_element}"/"{_type}"')
def step_impl(context, _element, _type):
    context.execute_steps(u'when I wait for the element/type "{_element}"/"{_type}" to be clickable'.format(_element=_element, _type=_type))
    _selected_element = selector_clickable(context, _element, _type)

    context.driver.execute_script("arguments[0].scrollIntoView();", _selected_element)
    _selected_element.click()

########################################################################################################################
########################################################################################################################
# this function doesn't contain js scrollIntoView(), as sometimes the scroll moves the targeted element out of view of selenium
@when(u'I click on the button that contains the element/type "{_element}"/"{_type}"')
@then(u'I click on the button that contains the element/type "{_element}"/"{_type}"')
def step_impl(context, _element, _type):
    context.execute_steps(u'when I wait for the element/type "{_element}"/"{_type}" to be clickable'.format(_element=_element, _type=_type))
    _selected_element = selector_clickable(context, _element, _type)

    _selected_element.click()

########################################################################################################################
##############################              Clear text              ####################################################
##############################              Clear text              ####################################################
########################################################################################################################
@when(u'I clear the text from the field that contains the element/type "{_element}"/"{_type}"')
def step_impl(context, _element, _type):

    context.execute_steps(u'when The element/type "{_element}"/"{_type}" is visible'.format(_element=_element, _type=_type))
    _field = selector_visible(context, _element, _type)
    context.browser.execute_script("arguments[0].scrollIntoView();", _field)
    _field.clear()
    time.sleep(1)

    #  wait for field to be empty
    seconds = 0.0
    _wait = True
    while _wait and seconds < timeout:
        if _field.text == "":
            _wait = False
        seconds += 0.1
        time.sleep(0.1)


########################################################################################################################
########################################################################################################################
@when(u'The text located in the element/type "{_element}"/"{_type}" is equal to the text "{_equal_to_text}"')
@then(u'The text located in the element/type "{_element}"/"{_type}" is equal to the text "{_equal_to_text}"')
def step_impl(context, _element, _type, _equal_to_text):
    context.execute_steps(u'when I wait for the element/type "{element}"/"{_type}" to load'.format(element=_element, _type=_type))
    _selected_element = selector_visible(context, _element, _type)

    context.browser.execute_script("arguments[0].scrollIntoView();", _selected_element)
    
    assert(_selected_element.text == _equal_to_text)
