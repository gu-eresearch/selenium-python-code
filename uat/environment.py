from behave import fixture, use_fixture
from selenium import webdriver
import logging
import os
from selenium.common.exceptions import NoSuchElementException
import re

work_dir = os.getcwd()

@fixture
def add_check_exists_by_xpath_func(context):
    def check_exists_by_xpath(xpath):
        try:
            context.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    context.check_exists_by_xpath = check_exists_by_xpath

@fixture
def selenium_driver_chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()

@fixture
def selenium_driver_chrome_headless(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') # sometimes docker does weird thing with the driver when running in a pipeline
    options.add_argument('window-size=2000,1600')
    prefs = {"download.default_directory": work_dir}
    options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=options)
    yield context.driver
    context.driver.quit()

@fixture
def selenium_driver_firefox(context):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=2000,1600')
    context.driver = webdriver.Firefox(options=options)
    yield context.driver
    context.driver.quit()

def before_all(context):
    driver = os.getenv("BEHAVE_DRIVER", "chrome")
    fixture_func = globals().get("selenium_driver_{}".format(driver.lower().strip()), None)
    if fixture_func is None:
        raise LookupError("No such driver fixture: selenium_driver_{}".format(driver.lower().strip()))
    logging.info("Using driver '{}'".format(driver))
    use_fixture(fixture_func, context)
    use_fixture(add_check_exists_by_xpath_func, context)


def after_all(context):
    context.driver.quit()

def slugify(text):
    slug = text.replace(" ", "_")
    return re.sub(r'(?u)[^-\w.]', '', slug)

def after_step(context, step):
    if step.status == 'failed':
        try:
            step_str = step.name
            scen_str = context.scenario.name
            filename = slugify("{}-{}".format(scen_str, step_str))
            context.driver.save_screenshot("{}.png".format(filename))
        except Exception as e:
            print(f"Saving screenshot failed: {str(e)}")