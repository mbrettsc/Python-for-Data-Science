from datetime import datetime

timestamp = datetime.now().timestamp()
formatted_time = "{:,.4f}".format(timestamp)
scientific_time = "{:.2e}".format(timestamp)

print(f"Seconds since January 1, 1970: {formatted_time} or {scientific_time} in scientific notation")

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%b %d %Y")
print(formatted_date)