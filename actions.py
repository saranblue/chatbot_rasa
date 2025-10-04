# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# # Dummy monthly attendance data
# ATTENDANCE_DATA = {
#     "January": (20, 22), "February": (18, 20), "March": (21, 22),
#     "April": (19, 22), "May": (22, 22), "June": (20, 22),
#     "July": (21, 22), "August": (18, 22), "September": (20, 22),
#     "October": (21, 22), "November": (19, 22), "December": (22, 22)
# }

# class ActionCheckAttendance(Action):
#     def name(self) -> Text:
#         return "action_check_attendance"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         month = tracker.get_slot("month")
#         if not month:
#             dispatcher.utter_message(text="Please tell me the month you want to check.")
#             return []

#         month = month.capitalize()
#         if month in ATTENDANCE_DATA:
#             attended, total = ATTENDANCE_DATA[month]
#             dispatcher.utter_message(text=f"You attended {attended} out of {total} days in {month}.")
#         else:
#             dispatcher.utter_message(text=f"Sorry, I don't have attendance data for {month}.")

#         return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionCheckAttendance(Action):

#     def name(self) -> Text:
#         return "action_check_attendance"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:

#         # Get the slot value "month"
#         month = tracker.get_slot("month")

#         if not month:
#             dispatcher.utter_message(text="Please tell me which month you want to check attendance for.")
#             return []

#         # Dummy data (you can connect to DB or API later)
#         attendance_data = {
#             "january": "18 out of 20 days",
#             "february": "15 out of 18 days",
#             "march": "20 out of 22 days",
#             "april": "19 out of 21 days",
#             "may": "21 out of 22 days",
#             "june": "17 out of 20 days",
#             "july": "20 out of 22 days",
#             "august": "19 out of 22 days",
#             "september": "20 out of 22 days",
#             "october": "21 out of 23 days",
#             "november": "18 out of 20 days",
#             "december": "16 out of 19 days"
#         }

#         month_lower = month.lower()

#         if month_lower in attendance_data:
#             attendance = attendance_data[month_lower]
#             dispatcher.utter_message(
#                 text=f"You attended {attendance} in {month.capitalize()}."
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"Sorry, I don't have attendance data for {month}."
#             )

#         return []


# import random
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher



# MONTH_MAP = {
#     "1": "January",
#     "2": "February",
#     "3": "March",
#     "4": "April",
#     "5": "May",
#     "6": "June",
#     "7": "July",
#     "8": "August",
#     "9": "September",
#     "10": "October",
#     "11": "November",
#     "12": "December"
# }


# class ActionCheckAttendance(Action):

#     def name(self) -> Text:
#         return "action_check_attendance"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:

#         month = tracker.get_slot("month")

#         if not month:
#             dispatcher.utter_message(text="Please tell me which month you want to check attendance for.")
#             return []

#         month = month.capitalize()

#         # Simulate total working days between 18-25
#         total_days = random.randint(18, 25)

#         # Simulate attended days (between 60% and 100% of total)
#         attended_days = random.randint(int(total_days * 0.6), total_days)

#         # Calculate percentage
#         percentage = round((attended_days / total_days) * 100, 2)

#         dispatcher.utter_message(
#             text=f"You attended {attended_days} out of {total_days} days in {month} ({percentage}%)."
#         )

#         return []


# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import random

# class ActionCheckAttendance(Action):

#     def name(self) -> str:
#         return "action_check_attendance"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict):

#         month = tracker.get_slot("month")

#         if not month:
#             dispatcher.utter_message(text="Please specify a month (e.g., January, May).")
#             return []

#         # Normalize input (capitalize first letter)
#         month = month.capitalize()

#         # Dummy dynamic data (random attendance per month)
#         total_days = random.randint(20, 23)
#         attended_days = random.randint(15, total_days)
#         percentage = (attended_days / total_days) * 100

#         response = f"You attended {attended_days} out of {total_days} days in {month} ({percentage:.2f}%)."
#         dispatcher.utter_message(text=response)

#         return []



# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import random

# class ActionCheckAttendance(Action):

#     def name(self) -> str:
#         return "action_check_attendance"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: dict):

#         month = tracker.get_slot("month")

#         if not month:
#             dispatcher.utter_message(text="Please specify a month (e.g., January, May).")
#             return []

#         # Normalize month using mapping
#         month_map = {
#             "jan": "January", "january": "January", "1": "January", "1st": "January", "first": "January",
#             "feb": "February", "february": "February", "2": "February", "2nd": "February", "second": "February",
#             "mar": "March", "march": "March", "3": "March", "3rd": "March", "third": "March",
#             "apr": "April", "april": "April", "4": "April", "4th": "April", "fourth": "April",
#             "may": "May", "5": "May", "5th": "May", "fifth": "May",
#             "jun": "June", "june": "June", "6": "June", "6th": "June", "sixth": "June",
#             "jul": "July", "july": "July", "7": "July", "7th": "July", "seventh": "July",
#             "aug": "August", "august": "August", "8": "August", "8th": "August", "eighth": "August",
#             "sep": "September", "sept": "September", "september": "September", "9": "September", "9th": "September", "ninth": "September",
#             "oct": "October", "october": "October", "10": "October", "10th": "October", "tenth": "October",
#             "nov": "November", "november": "November", "11": "November", "11th": "November", "eleventh": "November",
#             "dec": "December", "december": "December", "12": "December", "12th": "December", "twelfth": "December"
#         }

#         month_key = month.lower()
#         normalized_month = month_map.get(month_key, month.capitalize())

#         # Dummy dynamic data (random attendance per month)
#         total_days = random.randint(20, 23)
#         attended_days = random.randint(15, total_days)
#         percentage = (attended_days / total_days) * 100

#         response = f"You attended {attended_days} out of {total_days} days in {normalized_month} ({percentage:.2f}%)."
#         dispatcher.utter_message(text=response)

#         return []


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

class ActionCheckAttendance(Action):
    def name(self):
        return "action_check_attendance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        month = tracker.get_slot("month")

        # If no month provided, ask user
        if not month:
            dispatcher.utter_message(
                text="For which month do you want to check your attendance? 😊"
            )
            return []

        # Normalize month (capitalize first letter only)
        month = month.capitalize()

        try:
            # Connect to DB
            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()

            # Query attendance
            cursor.execute("SELECT present_days, total_days FROM attendance WHERE month=?", (month,))
            row = cursor.fetchone()
            conn.close()

            if row:
                present_days, total_days = row
                percent = (present_days / total_days) * 100
                response = f"You attended {present_days} out of {total_days} days in {month} ({percent:.2f}%)."
            else:
                response = f"Sorry, I don’t have attendance data for {month}."

        except Exception as e:
            response = f"⚠️ Error fetching data: {str(e)}"

        dispatcher.utter_message(text=response)
        return []
