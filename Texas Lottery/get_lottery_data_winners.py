import pandas as pd
from sodapy import Socrata
from datetime import date, timedelta

# Define the API endpoint and access parameters
domain = 'data.texas.gov'
dataset_id = '54pj-3dxy'
app_token = 'YOUR-APP-TOKEN-HERE'  # Optional: Replace with your actual app token. Visit Texas Open Data for token.
#username = 'YOUR_USERNAME'    # Optional: Replace with your Socrata username
#password = 'YOUR_PASSWORD'    # Optional: Replace with your Socrata password

# Create a client for the Socrata API
client = Socrata(domain, app_token) 

# Calculate the date range for filtering
date_today = date.today()
years_ago = date_today - timedelta(days=365 * 3)

# Format the dates as strings in the draw date format "YYYY-MM-DD"
date_today_str = date_today.strftime("%Y-%m-%d")
years_ago_str = years_ago.strftime("%Y-%m-%d")

# Define the filter parameters
filters = {
    "$where": f"(claim_paid_date >= '{years_ago_str}')",
    "$limit": 999999 
}

# Fetch the data from the Socrata API with filters
results = client.get(dataset_id, where=filters["$where"], limit=filters["$limit"])

# Create a DataFrame from the fetched data
results_df = pd.DataFrame.from_records(results)

results_df.to_csv("TexasLotteryData", sep=',')