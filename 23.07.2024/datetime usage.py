from datetime import datetime

date1 = datetime(2024, 7, 1)
date2 = datetime(2024, 7, 23)
difference = date2 - date1

print("Difference in days:", difference.days)

difference_weeks = difference.days / 7
print("Difference in weeks:", difference_weeks)

today = datetime.now()
print("Today's date:", today)

from dateutil.relativedelta import relativedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 7, 23)
difference_months = relativedelta(end_date, start_date)
print(f"Difference in months: {difference_months.months} months and {difference_months.years} years")
