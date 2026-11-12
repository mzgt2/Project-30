# 🎂 Birthday Wisher

A Python script that checks a CSV of birthdays and emails a birthday message with a random quote to anyone whose birthday is today.

## Features

- 📅 Checks today's date against a birthday list
- 📧 Sends an email through Yahoo's SMTP server
- 💬 Includes a random quote from a text file
- 📊 Reads birthday data with pandas

## Requirements

```bash
pip install pandas
```

> `smtplib`, `datetime`, and `random` are part of Python's standard library.

## Setup

1. Clone or download the project.
2. Install dependencies:
```bash
pip install pandas
```
3. Create a `birthdays.csv` file (format below).
4. Create a `quotes.txt` file with one quote per line, and update the path in `send_email()` to match where you saved it.
5. Open the script and set your email and password:
```python
my_email = "your_email@yahoo.com"
password = "your_app_password"
```
6. Run it:
```bash
python main.py
```

## birthdays.csv Format

```csv
name,email,year,month,day
Alex,alex@example.com,1990,6,15
Jordan,jordan@example.com,1985,11,12
```

The script matches on `month` and `day`, so the year doesn't affect who gets an email.

## File Structure

birthday-wisher/
├── main.py # Main script
├── birthdays.csv # Names, emails, and birthdays
└── quotes.txt # One quote per line


## How It Works

1. Gets today's month and day.
2. Reads `birthdays.csv` into a dictionary of names and dates.
3. Compares each person's birthday to today.
4. For each match, picks a random quote and sends an email via SMTP (`smtp.mail.yahoo.com`, port 587, TLS).

## Notes

- Yahoo requires an **app password** for SMTP login. Generate one in your Yahoo account security settings, since your normal password won't work.
- **Never commit your real email or password to GitHub.** Keep the placeholder values in the repo, or load credentials from environment variables.
- The script runs once and exits. To send emails automatically every day, schedule it with cron (Linux/macOS) or Task Scheduler (Windows).

## Possible Improvements

- Load credentials from environment variables
- Pass the recipient into `send_email()` instead of using a global variable
- Rotate between multiple message templates
- Add error handling for failed email sends
- Run on a schedule (cron or systemd timer)

## License

Free to use for personal and educational purposes.
