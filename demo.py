import requests
import time

LOGIN_URL = 'https://www.instagram.com/accounts/login/?hl=en'

def login(username, password):
    session = requests.Session()
    payload = {'username': username, 'password': password}
    try:
        response = session.post(LOGIN_URL, data=payload)
        response.raise_for_status()
        print("Login successful.")
        return session
    except requests.exceptions.RequestException as e:
        print("Login failed:", e)
        return None

def report_user(session, user_id):
    REPORT_URL = f'https://www.instagram.com/users/{user_id}/report/'
    payload = {'source_name': 'profile', 'reason_id': 1, 'frx_context': ''}
    try:
        response = session.post(REPORT_URL, data=payload)
        response.raise_for_status()
        print("Report submitted successfully for user:", user_id)
    except requests.exceptions.RequestException as e:
        print("Report submission failed for user:", user_id, e)

if __name__ == "__main__":
    your_username = ' your account'
    your_password = 'ypur account password '
    
    user_id_to_report = 'target account '
    num_reports = 1000#number of reports 

    session = login(your_username, your_password)

    if session:
        for i in range(num_reports):
            report_user(session, user_id_to_report)
            print(f"Report {i + 1} completed.")
            time.sleep(2)

        print("All reports completed.")
    else:
        print("Login failed. Cannot proceed with reporting.")
