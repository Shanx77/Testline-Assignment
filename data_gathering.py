import requests 
import pandas as pd 
import warnings

warnings.filterwarnings("ignore", message="unverified HTTPS request")

current_quiz_url = "https://jsonkeeper.com/b/LLQT"
quiz_submission_url = "https://api.jsonserve.com/rJvd7g"
historical_quiz_url = "https://api.jsonserve.com/XgAgFJ"

def fetch_data(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"failed to fetch data from {url}")
    
current_quiz_data = fetch_data(current_quiz_url)
quiz_submission_data = fetch_data(quiz_submission_url)
historical_quiz_data = fetch_data(historical_quiz_url)

current_quiz_df = pd.DataFrame(current_quiz_data)
historical_quiz_df = pd.DataFrame(historical_quiz_data)

#####
#dealing with quiz_submission data seperately 

main_data = pd.json_normalize(quiz_submission_data)

response_map_df = pd.DataFrame.from_dict(quiz_submission_data["response_map"], orient ="index", columns=["selected_option"]).reset_index().rename(columns={"index":"question_id"}) 

#merge the response map dictionary dataframe to the other main data dataframe
main_data["user_id"] = quiz_submission_data["user_id"]
response_map_df["user_id"] = quiz_submission_data["user_id"]
combined_df = pd.merge(response_map_df, main_data, on="user_id", how="left")    

#print("combined dataframe")
#print(combined_df.head())
##                                                          


print("current quiz data")
#print(current_quiz_df.head())
current_quiz_df.to_csv("current_quiz_data.csv")

print("quiz submission data")
#print(combined_df.head())
combined_df.to_csv("submission.csv")

print("historical quiz data")
#print(historical_quiz_df.head())
historical_quiz_df.to_csv("historical.csv")