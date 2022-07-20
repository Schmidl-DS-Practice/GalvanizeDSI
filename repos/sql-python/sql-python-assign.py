#snapshot should have, 'userid, reg_date, last_login, logins_7d, logins_7d_mobile, logins_7d_web,
# opt_out', as columns

# userid: user id
# reg_date: registration date
# last_login: date of last login
# logins_7d: number of the past 7 days for which the user has logged in (should be a value 0-7)
# logins_7d_mobile: number of the past 7 days for which the user has logged in on mobile
# logins_7d_web: number of the past 7 days for which the user has logged in on web
# opt_out: whether or not the user has opted out of receiving email

import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia', user='postgres', password='password', host='localhost', port=5432)
c = conn.cursor()
today = '2014-08-14'


# This is not strictly necessary but demonstrates how you can convert a date to another format
#ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")
#COUNT(*) AS cnt,
#timestamp %(ts)s AS datr_7d ->%(ts) ->GROUP BY userid;''', {'ts': ts}

c.execute(
    '''SELECT logins.userid,
               registrations.tmstmp as reg_date
               logins.tmstmp as last_login_date
    FROM logins
    JOIN registrations
    ON logins.userid = registrations.userid
    WHERE logins.tmstmp > timestamp '2014-08-14' - interval '7 days'
    LIMIT 10;
    '''
)

conn.commit()
conn.close()