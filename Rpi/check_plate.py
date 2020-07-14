import sqlite3 as lite
import sys
con = lite.connect('cars.db')
 
#cur.execute("CREATE TABLE Users(Plaka TEXT, Ad TEXT,Telefon INT ,TC INT)")
def check_plate(plate):
    with con:
        cur = con.cursor()    
        cur.execute("SELECT Users.Plaka")
        rows = cur.fetchall()
        for row in rows:
            if plate == row[1]:
                pass

    conn.commit()
    conn.close()
 