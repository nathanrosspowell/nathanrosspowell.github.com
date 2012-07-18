from datetime import datetime
from pytz import timezone

def get_w3c_date():
    now = datetime.now()
    return datetime( now.year, now.month,now.day, now.hour, now.minute, now.second, tzinfo=timezone("UTC") ).isoformat( 'T' ) 

if __name__ == "__main__":
    print get_w3c_date()
