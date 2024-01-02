from playwright.sync_api import sync_playwright


class UIPage:
    def __init__(self, browser_details):
        print(browser_details)
        self.browser = browser_details["browser"]
        self.base_url = browser_details["base_url"]

        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(self.base_url)
        print(f"Navigated to {self.base_url}")
        self.page.wait_for_load_state()

        self.origin_input = "input#txtInputOrigin_field"
        self.destination_input = "input#txtInputDestination_field"
        self.round_trip_date_input = "Selecciona"
        self.day_picker_next_button = '.DayPickerNavigation_button>>nth=1'
        self.option = 'option'
        self.search_button = "button#btnSearchCTA"
        self.flight_card_expander = "[class^=cardFlightstyle__CardExpander]"
        self.chose_button = "bundle-detail-0-flight-select"
        self.passenger_seat_info = "passenger-button-0"
        self.next_flight_button = "btn-confirm-cart-section"
        self.cannot_chose_seats_in_this_flight_msg = '[class^=CodeShareMessage__CodeShareMessageWrapper] span'
        self.luggage_continue_button = "BAGS-continue-button"
        self.cart_confirm_button = "button-cart-confirm--button"

    def get_page(self):
        return self.page

    def get_browser(self):
        return self.browser

    def get_context(self):
        return self.context

    def type_origin(self, origin):
        self.page.locator(self.origin_input).type(origin)

    def type_destination(self, destination):
        self.page.locator(self.destination_input).type(destination)

    def select_dropdown_option(self, option):
        self.page.get_by_role(self.option, name=option).click()

    def select_round_trip_dates(self, coming_date, return_date):
        self.page.get_by_placeholder(self.round_trip_date_input).click()
        self.page.locator(self.day_picker_next_button).click(click_count=7, delay=200)
        self.page.get_by_label(coming_date).click()
        self.page.get_by_label(return_date).click()

    def click_search_button(self):
        with self.page.expect_popup() as page2_info:
            self.page.locator(self.search_button).click()
        self.page = page2_info.value

    def get_first_most_economical_flight(self):
        self.page.locator(self.flight_card_expander).first.click()
        self.page.get_by_test_id(self.chose_button).click()
        self.page.wait_for_timeout(2000)

    def click_go_to_seats_button(self):
        self.page.get_by_test_id("button9--button").click()

    def select_seat(self, seat_number):
        self.page.locator(f'button[data-seat-number="{seat_number}"]').click()

    def get_passenger_seat_info(self):
        return self.page.get_by_test_id(self.passenger_seat_info)

    def click_next_flight_button(self):
        self.page.get_by_test_id(self.next_flight_button).click()

    def get_seat_map_page(self):
        return self.page.locator(self.cannot_chose_seats_in_this_flight_msg)

    def click_luggage_continue_button(self):
        self.page.get_by_test_id(self.luggage_continue_button).click()

    def click_cart_confirm_button(self):
        self.page.get_by_test_id(self.cart_confirm_button).click()
