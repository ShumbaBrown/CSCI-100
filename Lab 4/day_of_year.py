def GetDayOfYear(month, day):
    if month == 'january':
        return day
    elif month == 'february':
        return 31 + day
    elif month == 'march':
        return 59 + day
    elif month == 'april':
        return 90 + day
    elif month == 'may':
        return 120 + day
    elif month == 'june':
        return 151 + day
    elif month == 'july':
        return 181 + day
    elif month == 'august':
        return 212 + day
    elif month == 'september':
        return 243 + day
    elif month == 'october':
        return 273 + day
    elif month == 'november':
        return 304 + day
    elif month == 'december':
        return 334 + day

