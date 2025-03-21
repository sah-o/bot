import time

def log_activity(user_id, username, command):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('logs.txt', 'a') as f:
        f.write(f"{timestamp} - User ID: {user_id}, Username: {username}, Command: {command}\n")
