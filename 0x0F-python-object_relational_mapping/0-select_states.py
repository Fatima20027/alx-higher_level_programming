#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        # Fetch all rows and print each row tuple
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        sys.exit(1)

    except Exception as e:
        sys.exit(1)

    sys.exit(0)
