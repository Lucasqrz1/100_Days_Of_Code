import time
from datetime import datetime, timedelta
from typing import List, Dict
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


class FlightDeals:
    ORIGIN_CITY_IATA = "LON"
    SLEEP_DURATION = 2
    MONTHS_AHEAD = 6

    def __init__(self):
        self.data_manager = DataManager()
        self.flight_search = FlightSearch()
        self.notification_manager = NotificationManager()

    def update_iata_codes(self, sheet_data: List[Dict]) -> None:
        for row in sheet_data:
            if not row["iataCode"]:
                row["iataCode"] = self.flight_search.get_destination_code(row["city"])
                time.sleep(self.SLEEP_DURATION)
        self.data_manager.destination_data = sheet_data
        self.data_manager.update_destination_codes()

    def get_date_range(self) -> tuple:
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(self.MONTHS_AHEAD * 30))
        return tomorrow, six_month_from_today

    def send_notifications(self, flight, destination: Dict, customer_emails: List[str]) -> None:
        message = self._create_message(flight, destination)
        print(f"Lower price flight found to {destination['city']}!")
        self.notification_manager.send_whatsapp(message_body=message)
        self.notification_manager.send_emails(email_list=customer_emails, email_body=message)

    def _create_message(self, flight, destination: Dict) -> str:
        base_msg = (
            f"Low price alert! Only GBP {flight.price} to fly "
            f"from {flight.origin_airport} to {flight.destination_airport}, "
        )
        if flight.stops == 0:
            base_msg += "direct "
        else:
            base_msg += f"with {flight.stops} stop(s) "

        return base_msg + (
            f"departing on {flight.out_date} and returning on {flight.return_date}."
        )

    def run(self):
        try:
            sheet_data = self.data_manager.get_destination_data()
            self.update_iata_codes(sheet_data)

            start_date, end_date = self.get_date_range()
            customer_emails = [
                row["whatIsYourEmail?"]
                for row in self.data_manager.get_customer_emails()
            ]

            for destination in sheet_data:
                print(f"Getting flights for {destination['city']}...")
                try:
                    flights = self.flight_search.check_flights(
                        self.ORIGIN_CITY_IATA,
                        destination["iataCode"],
                        from_time=start_date,
                        to_time=end_date
                    )
                    cheapest_flight = find_cheapest_flight(flights)
                    print(f"{destination['city']}: £{cheapest_flight.price}")
                    time.sleep(self.SLEEP_DURATION)

                    if (cheapest_flight.price != "N/A" and
                            cheapest_flight.price < destination["lowestPrice"]):
                        self.send_notifications(
                            cheapest_flight,
                            destination,
                            customer_emails
                        )
                except Exception as e:
                    print(f"Error processing {destination['city']}: {str(e)}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    flight_deals = FlightDeals()
    flight_deals.run()


if __name__ == "__main__":
    main()