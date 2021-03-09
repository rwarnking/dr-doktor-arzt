from calendar import monthrange
import locale

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
