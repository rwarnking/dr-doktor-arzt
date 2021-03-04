from calendar import monthrange
import locale

month_data = []

def get_selected_date(date):
    #locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    #locale.setlocale(locale.LC_ALL, 'deu_deu')
    locale.setlocale(locale.LC_TIME, "de_DE")

    return {
        "day_idx" : date.day,
        "day_offset" : monthrange(date.year, date.month)[0],
        "month_idx" : date.month,
        "month_name" : date.strftime("%B"),
        "month_days" : monthrange(date.year, date.month)[1],
        "year" : date.year,
        "complete" : date.strftime("%a %d.%m.%Y"),
    }


def fillmonth():
    for i in range(12):
        days = []
        for j in range(31):
            days.append([
            ["9:30", "Free"], ["10:00", "Free"], ["10:30", "Free"], ["11:00", "Free"],
            ["11:30", "Free"], ["12:00", "Free"], ["12:30", "Free"], ["15:00", "Free"],
            ["15:30", "Free"], ["16:00", "Free"], ["16:30", "Free"], ["17:00", "Free"],
        ])
        month_data.append(days)

fillmonth()
