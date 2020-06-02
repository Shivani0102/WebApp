"""
This module contains shared fixtures for web UI tests.
For now, only Chrome browser is supported.
"""

import json
import pytest
import allure
import os

from selenium.webdriver import Chrome

CONFIG_PATH = 'resources\config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']

@allure.step('Reading config from json file')
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@allure.step('Configuring browser')
@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@allure.step('Configuring the wait time for browser')
@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

@allure.step('Initializing the configured browser')
@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time, request):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

# @pytest.fixture(scope="function")
# def listener(request):
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             b.execute_script("document.body.bgColor = 'white';")
#
#             allure.attach(b.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#         except:
#             pass # just ignore

# import json
# from ctypes.macholib import framework
#
# import pytest
# import allure
# import os
#
# from pkg_resources import require
# from robot.running.testlibraries import Object
# from selenium.webdriver import Chrome
#
# #CONFIG_PATH = 'resources\config.json'
# Browser_path = "resources\chromedriver.exe"
# CONFIG_PATH = 'resources\config.json'
# DEFAULT_WAIT_TIME = 10
# SUPPORTED_BROWSERS = ['chrome']
#
# @allure.step('Reading config from json file')
# @pytest.fixture(scope='session')
# def config():
#     # Read the JSON config file and returns it as a parsed dict
#     with open(CONFIG_PATH) as config_file:
#         data = json.load(config_file)
#     return data
#
# @allure.step('Configuring browser')
# @pytest.fixture(scope='session')
# def config_browser(config):
#     # Validate and return the browser choice from the config data
#     # To extend the browser support in future
#     if 'browser' not in config:
#         raise Exception('The config file does not contain "browser"')
#     elif config['browser'] not in SUPPORTED_BROWSERS:
#         raise Exception(f'"{config["browser"]}" is not a supported browser')
#     return config['browser']
#
# @allure.step('Configuring the wait time for browser')
# @pytest.fixture(scope='session')
# def config_wait_time(config):
#     # Validate and return the wait time from the config data
#     return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         mode = 'a' if os.path.exists('failures') else 'w'
#         try:
#             with open('failures', mode) as f:
#                 if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
#                     web_driver = item.funcargs['browser']
#                 else:
#                     print('Fail to take screen-shot')
#                     return
#             allure.attach(
#                 web_driver.get_screenshot_as_png(),
#                 name='screenshot',
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             print('Fail to take screen-shot: {}'.format(e))
#
# @allure.step('Initializing the configured browser')
# @pytest.fixture(scope='session')
# def browser(config_browser, config_wait_time, request):
#     # Initialize WebDriver
#     if config_browser == 'chrome':
#         driver = Chrome(Browser_path)
#     else:
#         raise Exception(f'"{config_browser}" is not a supported browser')
#
#     # Wait implicitly for elements to be ready before attempting interactions
#     driver.implicitly_wait(config_wait_time)
#     driver.maximize_window()
#
#     # Return the driver object at the end of setup
#     yield driver
#
#     # For cleanup, quit the driver
#     driver.quit()
#
# # @pytest.fixture(scope="function")
# # def listener(request):
# #     if request.node.rep_call.failed:
# #         # Make the screen-shot if test failed:
# #         try:
# #             b.execute_script("document.body.bgColor = 'white';")
# #
# #             allure.attach(b.get_screenshot_as_png(),
# #                           name=request.function.__name__,
# #                           attachment_type=allure.attachment_type.PNG)
# #         except:
# #             pass # just ignore
#

#
# "use strict";
# Object.defineProperty(exports, "__esModule", { value: true });
# assert_1 = require("assert");
# exports.config = {
#     seleniumAddress: 'http://localhost:4444/wd/hub',
#     capabilities: {
#         'browserName': 'chrome',
#         'goog:chromeOptions': {
#             w3c: false
#         }
#     },
#     framework: 'jasmine',
#     //specs: ['./SamplePOM/**/*.js'],
#     specs: ['./tests/Testhomepage.js'],
#     jasmineNodeOpts: {
#         defaultTimeoutInterval: 200000
#     },
#     onPrepare: function () {
#         var globals = require('protractor');
#         var browser = globals.browser;
#         browser.manage().window().maximize();
#         browser.manage().timeouts().implicitlyWait(5000);
#         // allure.createStep('Outer step', function()
#         //  {
#         // });
#         var AllureReporter = require('jasmine-allure-reporter');
#         jasmine.getEnv().addReporter(new AllureReporter({
#             resultsDir: 'allure-results'
#         }));
#         jasmine.getEnv().afterEach(function (done) {
#             assert_1.ifError(done);
#             {
#                 browser.takeScreenshot().then(function (png) {
#                     allure.createAttachment('Screenshot', function () {
#                         return new Buffer(png, 'base64');
#                     }, 'image/png')();
#                     done();
#                 });
#             }
#         })
#     }
# }
