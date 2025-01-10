from flask import Flask, request, redirect, render_template
import requests
import urllib3
from pymongo import MongoClient

# Connection with local MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client["Strava_db"]
collection = db["Activities"]

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Flask App
app = Flask(__name__)

# Strava API credentials
CLIENT_ID = "131992"
CLIENT_SECRET = "cec6a810ac33424190f46eff61685c70c1ca54e8"
REDIRECT_URI = "https://5af0-89-74-126-40.ngrok-free.app/exchange_token"
STRAVA_AUTH_URL = "https://www.strava.com/oauth/authorize"
STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"
STRAVA_ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"


@app.route('/')
def home():
    strava_url = (
        f"{STRAVA_AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&"
        "scope=activity:read_all&approval_prompt=auto"
    )
    return f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Strava Login</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }}
            .container {{
                max-width: 600px;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #fc4c02;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.1rem;
                color: #333;
                margin-bottom: 20px;
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                font-size: 1.2rem;
                color: #fff;
                background-color: #fc4c02;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }}
            .button:hover {{
                background-color: #e03e01;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Trener personalny</h1>
            <p>
                Aby zalogować się do serwisu trenera personalnego prosimy wcisnąć przycisk poniżej
            </p>
            <a href="{strava_url}" class="button">Log in with Strava</a>
        </div>
    </body>
    </html>
    """



@app.route('/exchange_token')
def exchange_token():
    # Step 1: Capture authorization code from URL parameters
    code = request.args.get('code')
    if not code:
        return "Error: Authorization code not received"

    print(f"Authorization code received: {code}")

    # Step 2: Exchange authorization code for access token
    token_exchange_payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }

    response = requests.post(STRAVA_TOKEN_URL, data=token_exchange_payload)

    if response.status_code != 200:
        return f"Error fetching token: {response.content}"

    token_response_json = response.json()
    access_token = token_response_json['access_token']

    print(f"Access token received: {access_token}")

    # Redirect to fetch activities using the access token
    return redirect(f'/fetch_activities?access_token={access_token}')


# Other routes like /fetch_activities would go here


@app.route('/fetch_activities')
def fetch_activities():
    # Get access token from the URL parameters
    access_token = request.args.get('access_token')

    # Fetch activities using the access token
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}

    print("Fetching activities from Strava API...")
    activities_response = requests.get(STRAVA_ACTIVITIES_URL, headers=header, params=param)
    activities = activities_response.json()

    # Fetch comments for each activity and save them to MongoDB
    for activity in activities:
        activity_id = activity['id']
        comments = get_comments(access_token, activity_id)
        activity['comments'] = comments

        # Insert the activity into MongoDB
        collection.insert_one(activity)

    return "Activities and comments have been successfully fetched and stored in MongoDB!"


def get_comments(access_token, activity_id):
    # Fetch comments for a specific activity
    comments_url = f"https://www.strava.com/api/v3/activities/{activity_id}/comments"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(comments_url, headers=headers)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
