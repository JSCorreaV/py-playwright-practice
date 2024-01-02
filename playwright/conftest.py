import pytest
from playwright.sync_api import Playwright, BrowserType
from typing import Dict
from dotenv import load_dotenv

import os

PROJECT_ROOT_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="session")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict
):
    context = browser_type.launch_persistent_context("./foobar", **{
        **browser_type_launch_args,
        **browser_context_args,
    })
    yield context
    context.close()


@pytest.fixture(scope="session")
def setup(playwright: Playwright):
    load_dotenv(override=True)
    browser = {
        "base_url": os.getenv("BASE_URL"),
        "headless": os.getenv("HEADLESS").lower() == "true"
    }

    p_browser = playwright.chromium.launch(headless=browser["headless"], slow_mo=500)
    browser["browser"] = p_browser
    return browser
