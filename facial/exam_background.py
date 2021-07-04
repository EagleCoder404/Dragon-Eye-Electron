import time
import os
count = 1

def proctoring_is_on():
    with open(os.getcwd()+"/stop_proctoring_features") as config:
        config_content = config.read()
        if config_content == "false":
            return True
        else:
            return False

while True:
    if not proctoring_is_on():
        break
    print(count)
    count += 1
    time.sleep(1)
