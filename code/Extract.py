"""
It is necessary to add the Kaggle API key to user/.kaggle folder
It is necessary to stage the CSV to @my_stage in Snowflake UI
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

current_path = os.getcwd()
current_path = os.path.join(current_path, "../data")

filenames = ["activity_environment_data.csv","digital_interaction_data.csv","personal_health_data.csv" ]

for filename in filenames:
    api.dataset_download_file('manideepreddy966/wearables-dataset', path=current_path, file_name=filename)

print(f"Dataset downloaded to: {current_path}")
