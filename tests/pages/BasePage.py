class BasePageClass:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state()