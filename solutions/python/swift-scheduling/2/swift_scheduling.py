from datetime import datetime, timedelta, date
import re, calendar

def get_first_working_day(year, month):
    day = date(year, month, 1)

    while day.weekday() >= 5:
        day += timedelta(days=1)

    return day

def get_base_quarter(month):
    return (month - 1) // 3 + 1

def get_last_working_day(year, month):
    day = date(year, month, calendar.monthrange(year, month)[1])

    while day.weekday() >= 5:
        day -= timedelta(days=1)

    return day

def delivery_date(start, description):

    base_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    day_num = base_time.weekday()
    
    match description:
        case "NOW":
            new_time = base_time + timedelta(hours=2)
            return new_time.strftime("%Y-%m-%dT%H:%M:%S")
        case "ASAP":
            start_hour = base_time.hour

            if start_hour < 13 :
                new_time = base_time.replace( hour=17, minute = 0, second = 0, microsecond = 0 )
                return new_time.strftime("%Y-%m-%dT%H:%M:%S")
                
            new_time = base_time + timedelta( days = 1 )
            new_time = new_time.replace( hour = 13, minute = 0, second = 0, microsecond = 0 )
            return new_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        case "EOW":
            if day_num < 3:
                if day_num == 0:
                    new_time = base_time + timedelta ( days = 4 )
                elif day_num == 1:
                    new_time = base_time + timedelta ( days = 3 )
                else:
                    new_time = base_time + timedelta ( days = 2 )
                new_time = new_time.replace( hour=17, minute = 0, second = 0, microsecond = 0 )
                return new_time.strftime("%Y-%m-%dT%H:%M:%S")
            else:
                if day_num == 3:
                    new_time = base_time + timedelta ( days = 3 )
                else:
                    new_time = base_time + timedelta ( days = 2 )
                new_time = new_time.replace( hour=20, minute = 0, second = 0, microsecond = 0 )
                return new_time.strftime("%Y-%m-%dT%H:%M:%S")
            

        case s if re.match(r"^\d+M$", s):
            target_month = int(description[:-1])
        
            if base_time.month < target_month:
                target_year = base_time.year
            else:
                target_year = base_time.year + 1
        
            new_time = get_first_working_day(target_year, target_month)
            new_time = datetime(
                new_time.year,
                new_time.month,
                new_time.day,
                8, 0, 0
            )
        
            return new_time.strftime("%Y-%m-%dT%H:%M:%S")
            

        case s if re.match(r"^Q\d+$", s):
            target_quarter = int(description[1:])
            base_quarter = get_base_quarter(base_time.month)

            if base_quarter <= target_quarter:
                target_year = base_time.year
            else:
                target_year = base_time.year + 1

            target_month = target_quarter * 3

            new_time = get_last_working_day(target_year, target_month)

            new_time = datetime(
                new_time.year,
                new_time.month,
                new_time.day,
                8, 0, 0
            )

            return new_time.strftime("%Y-%m-%dT%H:%M:%S")