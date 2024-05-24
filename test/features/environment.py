import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import configreader


def before_scenario(context, scenario):

    browser_name = configreader.read_configuration("basic info", "browser")

    if browser_name.__eq__("Chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(configreader.read_configuration("basic info","url"))


def after_scenario(context, scenario):
    context.driver.quit()

def after_step(context,step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name= "failed_test_case", attachment_type=AttachmentType.PNG)