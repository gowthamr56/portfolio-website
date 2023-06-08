import datetime, pytz

# IST Time Zone
tz = pytz.timezone("Asia/Kolkata")

with open('workflow_logs.txt', "a") as file:
    utc_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
    ist_time = datetime.datetime.now(tz=tz).strftime("%d-%m-%y %H:%M")
    file.write(f"{utc_time} | {ist_time}\n")

