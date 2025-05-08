import csv
from datetime import datetime

CSV_FILE = 'data/sightings.csv'

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value

def main():
    print("\n🛰️ Add a New Drone Sighting Entry\n")

    # Auto-fill date/time if user presses Enter
    date = get_input(f"Date [YYYY-MM-DD] (default today): ", required=False)
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    time = get_input(f"Time [HH:MM] (default now): ", required=False)
    if not time:
        time = datetime.now().strftime("%H:%M")

    location = get_input("Location (e.g., Sialkot border): ")
    latitude = get_input("Latitude (e.g., 32.4945): ")
    longitude = get_input("Longitude (e.g., 74.5229): ")
    drone_type = get_input("Drone Type (e.g., ISR fixed-wing, loitering munition): ")
    source = get_input("Source (e.g., ISPR, Dawn News, Telegram): ")

    # Write to CSV
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, location, latitude, longitude, drone_type, source])

    print("\n✅ Entry added successfully!")

if __name__ == '__main__':
    main()

