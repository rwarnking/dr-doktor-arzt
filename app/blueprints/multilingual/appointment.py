from calendar import monthrange

days = []

def filldays():
    for i in range(31):
        days.append([
        ["9:30", "Free"], ["10:00", "Free"], ["10:30", "Free"], ["11:00", "Free"],
        ["11:30", "Free"], ["12:00", "Free"], ["12:30", "Free"], ["15:00", "Free"],
        ["15:30", "Free"], ["16:00", "Free"], ["16:30", "Free"], ["17:00", "Free"],
    ])

filldays()

def days_per_month(year, month):
    return monthrange(year, month)[1]
