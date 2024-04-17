"""
a company wants to track to track the usage of its mobile app by recording users login times and dates. the company stores the login information in a 2D array of string, logs, which contains data in the format ["username<user_id>", "login_time", "login_date"].

they need a fucntion to process the logs and output a 2D array of strings, sorted lexicographyically, that displays the number of times each user log in per day in the format ["username<user_id>", "login_date", "login_count"].
it must filter invalid data in the input array rather than write it to the output array.

user should be sorted in lexicographic order based on their user_id. each usre's informtaion should be sorted by the login date in ascending order. the date and time are provided in YYYY-MM-DD and HH:MM:SS format, and the user has the format "userX" where X is an integer.

example: logs = [["user1", "09:00:00", "2021-01-01"], ["user1", "13:00:00", "2021-01-01"], ["user2", "14:00:00", "2021-01-01"], ["user1", "20:00:00", "2021-01-02", "user2", "21:00:00", "2021-01-01"]

in the case , the function should output the login count in the format [["user1", "2021-01-01", "2"], ["user1", "2021-01-02", "1", "user2", "2021-01-01", "2"]]
"""
from collections import defaultdict

def process_logs_1(logs):  
    # Create a dictionary to store the login counts for each user and date  
    login_counts = {}  
      
    # Loop through the logs and update the login counts dictionary  
    for log in logs:  
        # Check if the log has valid data  
        if len(log) != 3 or not log[0].startswith("user"):  
            continue  
          
        # Extract the user ID and login date from the log  
        user_id = log[0]  
        login_date = log[2]  
          
        # Update the login counts for the user and date  
        key = (user_id, login_date)   
        login_counts[key] = login_counts.get(key, 0) + 1  
        # login_counts[key] += 1
    # Convert the login counts dictionary to a list of sorted strings  
    result = []  
    for key, value in sorted(login_counts.items()):  
        user_id, login_date = key  
        result.append([user_id, login_date, str(value)])  
      
    return result  
  
def process_logs_2(logs):  
    # Create a defaultdict to store the login counts for each user and date  
    login_counts = defaultdict(int)  
      
    # Loop through the logs and update the login counts dictionary  
    for log in logs:  
        # Check if the log has valid data  
        if len(log) != 3 or not log[0].startswith("user"):  
            continue  
          
        # Extract the user ID and login date from the log  
        user_id = log[0]  
        login_date = log[2]  
          
        # Update the login counts for the user and date  
        key = (user_id, login_date)  
        login_counts[key] += 1  
      
    # Convert the login counts dictionary to a list of sorted strings  
    result = []  
    for key, value in sorted(login_counts.items()):  
        user_id, login_date = key  
        result.append([user_id, login_date, str(value)])  
      
    return result

logging = [["user1", "09:00:00", "2021-01-01"], ["user1", "13:00:00", "2021-01-01"], ["user2", "14:00:00", "2021-01-01"], ["user1", "20:00:00", "2021-01-02"], ["user2", "21:00:00", "2021-01-01"]]
print(process_logs_1(logging))