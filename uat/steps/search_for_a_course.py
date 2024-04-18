from behave import given, when, then
from selenium.webdriver.common.by import By

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get("https://www.griffith.edu.au/")
    context.execute_steps(u'then I wait for the element/type "{_element}"/"{_type}" to load'.format(_element="div.logo.logo-nav-b", _type="selector"))

@when(u'I go to the study page')
def step_impl(context):
    context.execute_steps(u'when I use actionChain to click on the button with the element/type "{_element}"/"{_type}"'.format(_element="Study", _type="text"))

@when(u'I search for courses using the search term "{search_term}"')
def step_impl(context, search_term):
    context.execute_steps(u'when I use actionChain to send the text "{_text}" to the element/type "{_element}"/"{_type}"'.format(_text=search_term, _element="searchtextbox", _type="id"))
    context.execute_steps(u'then I use actionChain to click on the button with the element/type "{_element}"/"{_type}"'.format(_element="input.search-icon", _type="selector"))

@then(u'I can see a list of computing courses with titles that contain the term "{term_1}" or "{term_2}"')
def step_impl(context, term_1, term_2):  
    # get all degree titles
    titles = context.driver.find_elements(By.CSS_SELECTOR, "p.degree")
    # check that one of the search terms are in each title
    for i in range(len(titles)):
        assert(term_1 in titles[i].text.lower() or term_2 in titles[i].text.lower())

