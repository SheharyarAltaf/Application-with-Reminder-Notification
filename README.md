# Notification Reminder Application

This Python application is designed to remind you of upcoming events by sending desktop notifications. Events are loaded from an Excel file, and the application continuously checks for reminders that need to be sent based on the current time.

## Features

- **Desktop Notifications**: Sends a desktop notification for upcoming events.
- **Excel Integration**: Loads events from an Excel file, making it easy to manage your events.
- **Scheduled Checks**: Automatically checks for upcoming events every minute.

![Notification Example](https://your-image-link.com/Screenshot (94).png)

## Prerequisites

Before running the application, make sure you have the following installed:

| **Python**    | ![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white&color=306998) |<br>
| **Pandas**    | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white&color=150458) |<br>
| **Openpyxl**  | ![Openpyxl](https://img.shields.io/badge/Openpyxl-215732?style=for-the-badge&color=215732) |<br>
| **Schedule**  | ![Schedule](https://img.shields.io/badge/Schedule-0A9396?style=for-the-badge&color=0A9396) |<br>
| **Plyer**     | ![Plyer](https://img.shields.io/badge/Plyer-FF6F61?style=for-the-badge&color=FF6F61) |

You can install the required packages using pip:

```bash
pip install pandas openpyxl schedule plyer
