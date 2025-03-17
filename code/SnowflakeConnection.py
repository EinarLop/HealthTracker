import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

def initiate_connection():
    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA"),
        )

        cur = conn.cursor()


        print("Connection established")

        return cur, conn

    except Exception as e:
        print(f"Connection failed: {e}")
        return None, None


def close_connection(cur, conn):
    cur.close()
    conn.close()
    print("Connection closed")