import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

def info(log):
    print("\033[94m[" + formatted_time + "]\033[0m\033[92m[INFO]\033[0m" + log)
    
def warning(log):
    print("\033[94m[" + formatted_time + "]\033[0m\033[91m[WARN]\033[0m" + log)
    
def error(log):
    print("\033[94m[" + formatted_time + "]\033[0m\033[31m[ERROR]\033[0m" + log)