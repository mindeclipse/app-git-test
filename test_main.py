import unittest
from datetime import date, timedelta
from main import get_upcoming_birthdays

class TestUpcomingBirthdays(unittest.TestCase):
    def test_birthday_today(self):
        today = date(2024, 1, 10) # Wednesday
        users = [{"name": "User1", "birthday": date(1990, 1, 10)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "User1")
        self.assertEqual(result[0]["congratulation_date"], "2024.01.10")

    def test_birthday_tomorrow(self):
        today = date(2024, 1, 10) # Wednesday
        users = [{"name": "User1", "birthday": date(1990, 1, 11)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["congratulation_date"], "2024.01.11")

    def test_birthday_in_7_days(self):
        today = date(2024, 1, 10) # Wednesday
        users = [{"name": "User1", "birthday": date(1990, 1, 17)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["congratulation_date"], "2024.01.17")

    def test_birthday_in_8_days(self):
        today = date(2024, 1, 10) # Wednesday
        users = [{"name": "User1", "birthday": date(1990, 1, 18)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 0)

    def test_birthday_yesterday(self):
        today = date(2024, 1, 10) # Wednesday
        users = [{"name": "User1", "birthday": date(1990, 1, 9)}]
        result = get_upcoming_birthdays(users, today=today)
        # Should be next year, so not in upcoming list for now
        self.assertEqual(len(result), 0)

    def test_weekend_saturday(self):
        today = date(2024, 1, 8) # Monday
        # Jan 13 2024 is Saturday
        users = [{"name": "User1", "birthday": date(1990, 1, 13)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        # Should be moved to Monday Jan 15
        self.assertEqual(result[0]["congratulation_date"], "2024.01.15")

    def test_weekend_sunday(self):
        today = date(2024, 1, 8) # Monday
        # Jan 14 2024 is Sunday
        users = [{"name": "User1", "birthday": date(1990, 1, 14)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        # Should be moved to Monday Jan 15
        self.assertEqual(result[0]["congratulation_date"], "2024.01.15")
    
    def test_weekend_past_but_congratulation_future(self):
        # If birthday was Saturday (yesterday), but today is Sunday. 
        # Congratulation date is Monday (tomorrow). Should be included.
        today = date(2024, 1, 14) # Sunday
        # Jan 13 was Saturday
        users = [{"name": "User1", "birthday": date(1990, 1, 13)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["congratulation_date"], "2024.01.15")

    def test_year_transition(self):
        today = date(2023, 12, 28)
        # Jan 2 2024 is Tuesday
        users = [{"name": "User1", "birthday": date(1990, 1, 2)}]
        result = get_upcoming_birthdays(users, today=today)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["congratulation_date"], "2024.01.02")

if __name__ == '__main__':
    unittest.main()
