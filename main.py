import pandas as pd
from datetime import datetime, timedelta
import schedule
import time
from plyer import notification

# Function to load events from Excel
def load_events(file_path='events.xlsx'):
    try:
        events = pd.read_excel(file_path)
        events['DateTime'] = pd.to_datetime(events['Date'].astype(str) + ' ' + events['Time'].astype(str))
        return events
    except Exception as e:
        print(f"Error loading events from {file_path}: {e}")
        return None

# Function to check reminders and send notifications
def check_reminders(events):
    now = datetime.now()
    for _, event in events.iterrows():
        try:
            event_time = event['DateTime']
            
            if now >= event_time:
                send_notification(event['Event'], event_time)
                print(f"Notification sent for event: {event['Event']}")
        except Exception as e:
            print(f"Error processing event '{event['Event']}': {e}")

# Function to send desktop notification
def send_notification(event_name, event_time):
    notification.notify(
        title='Reminder',
        message=f'Upcoming Event: {event_name}\nTime: {event_time.strftime("%Y-%m-%d %H:%M")}',
        timeout=10
    )

# Main function to run the reminder application
def main():
    # Load events from Excel file
    events = load_events('events.xlsx')
    if events is None:
        print("Exiting due to error loading events.")
        return
    
    # Schedule check_reminders to run every minute
    schedule.every(1).minutes.do(check_reminders, events=events)
    
    print("Reminder application is running...")

    # Loop to keep the script running and checking reminders
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
