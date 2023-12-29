# Playwright Python UI Testing Tutorial

## Description

This tutorial shows how to create a basic UI testing architecture for a Latam web page using Playwright in Python.
The idea is exploring basic get elements, interact with them and verify with static and dinamic behaviour in one and more than one page. You can see the use of browsers and context, including the generation of tracking files.

## Getting Started

Use Python 3.8 or higher.
Install the Playwright Python bindings

```bash
pip install pytest-playwright
```

Then install playwright default browers

```bash
playwright install
```

## Running the Tests

If the test include the tracing recorder "context.tracing.start(screenshots=True, snapshots=True)", to run the tests, use the following command:

```bash
pytest -v -s
```

By default, tests with the tracing recorder command open a browser (headless = False) in the browser definition browser = playwright.chromium.launch(headless = False).

To watch tracking file executing, use the following command:

```bash
playwright show-trace [trackingFileName]
```

## Conclusion

This tutorial provides a basic introduction to UI testing with Playwright in Python. For more information, see the [Playwright documentation](https://playwright.dev/python/docs/intro).
If you need to include timeouts, include them as constant in tests/utils/Constansts.py and then import them where you require.

## MIT License

Copyright (c) 2023 David Andres Hernandez Rodriguez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
