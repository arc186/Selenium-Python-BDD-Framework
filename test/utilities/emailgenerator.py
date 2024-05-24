from datetime import datetime


def get_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_S")
    return "lmnop" + time_stamp + "@gmail.com"