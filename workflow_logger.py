import datetime

with open('workflow_logs.txt', "a") as file:
    file.write(datetime.datetime.now().strftime("%d-%m-%y %H:%M") + "\n")

