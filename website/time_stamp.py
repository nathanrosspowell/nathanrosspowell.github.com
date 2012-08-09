from datetime import datetime
from pytz import timezone
import time

def get_w3c_date():
    now = datetime.now()
    date = datetime( now.year, now.month,now.day, now.hour, now.minute, now.second, tzinfo=timezone("UTC") ).isoformat( 'T' ) 
    tz = timezone( time.tzname[ 0 ] ).localize( now ).strftime('%z')
    tz = tz[:-2] + ":" + tz[-2:]
    date = date[ : -6 ] + tz
    return date

if __name__ == "__main__":
    print get_w3c_date()
