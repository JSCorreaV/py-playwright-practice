import pytest
from playwright.sync_api import expect

from classes.uipage import UIPage
from support.helpers import load_fixtures


@pytest.fixture
def flight_data():
    flight_scheduling_data = load_fixtures('flight_schedule_data.json')
    origin = flight_scheduling_data["origin"]
    origin_dropdown_option = flight_scheduling_data["dropdown_options"]["origin"]
    destination = flight_scheduling_data["destination"]
    destination_dropdown_option = flight_scheduling_data["dropdown_options"]["destination"]
    going_date = flight_scheduling_data["going_date"]
    return_date = flight_scheduling_data["return_date"]
    seat_number = flight_scheduling_data["seat_number"]
    no_seats_messages = flight_scheduling_data["no_seats_messages"]

    return [origin, destination, origin_dropdown_option, destination_dropdown_option, going_date, return_date, seat_number, no_seats_messages]


def test_flight_scheduler(setup, flight_data):
    origin, destination, origin_dropdown_option, destination_dropdown_option, going_date, return_date, seat_number, no_seat_messages = flight_data
    flight_scheduler_page = UIPage(setup)

    flight_scheduler_page.type_origin(origin)
    flight_scheduler_page.select_dropdown_option(origin_dropdown_option)
    flight_scheduler_page.type_destination(destination)
    flight_scheduler_page.select_dropdown_option(destination_dropdown_option)
    flight_scheduler_page.select_round_trip_dates(going_date, return_date)

    flight_scheduler_page.click_search_button()

    flight_scheduler_page.get_first_most_economical_flight()
    flight_scheduler_page.get_first_most_economical_flight()
    flight_scheduler_page.click_go_to_seats_button()

    flight_scheduler_page.select_seat(seat_number)

    expect(flight_scheduler_page.get_passenger_seat_info()).to_be_visible()
    flight_scheduler_page.click_next_flight_button()

    seat_map_page = flight_scheduler_page.get_seat_map_page()
    expect(seat_map_page).to_contain_text(no_seat_messages)
    flight_scheduler_page.click_next_flight_button()

    expect(seat_map_page).to_contain_text(no_seat_messages)
    flight_scheduler_page.click_next_flight_button()

    expect(seat_map_page).to_contain_text(no_seat_messages)
    flight_scheduler_page.click_next_flight_button()

    expect(seat_map_page).to_contain_text(no_seat_messages)

    flight_scheduler_page.click_next_flight_button()
    flight_scheduler_page.select_seat(seat_number)
    expect(flight_scheduler_page.get_passenger_seat_info()).to_be_visible()

    flight_scheduler_page.click_next_flight_button()

    flight_scheduler_page.click_luggage_continue_button()
    flight_scheduler_page.click_cart_confirm_button()
