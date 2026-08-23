"""
Behave environment hooks: start/stop a Playwright browser around the
whole test run, and give each scenario a fresh page/context so tests
don't leak state (cookies, local storage) between scenarios.
"""

import os

from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("BASE_URL", "https://www.saucedemo.com")
HEADLESS = os.environ.get("HEADLESS", "true").lower() != "false"


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=HEADLESS)
    context.base_url = BASE_URL


def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")
        context.page.screenshot(path=f"{screenshot_dir}/{safe_name}.png")
    context.page.close()
    context.browser_context.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
