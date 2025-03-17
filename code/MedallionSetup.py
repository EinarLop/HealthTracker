import SnowflakeConnection as sf
import os
import urllib.parse


def bronze_layer_setup():
    cur, con = sf.initiate_connection()
    cur.execute("CREATE STAGE IF NOT EXISTS bronze_layer;")
    response = cur.fetchall()

    print("Bronze Layer Create Status: ", response)

    current_path = os.getcwd()
    current_path = urllib.parse.quote(os.path.abspath(current_path))

    filenames = ["activity_environment_data.csv", "digital_interaction_data.csv", "personal_health_data.csv"]

    for filename in filenames:
        cur.execute(f"PUT file:///{current_path}/../data/{filename} @bronze_layer OVERWRITE=FALSE AUTO_COMPRESS=FALSE;")
        response = cur.fetchall()
        print(f"PUT {filename} to Layer Status: ", response)

    sf.close_connection(cur, con)

bronze_layer_setup()
