import os

location =""
filename = "logfile"
ERROR_COUNT =0
ERROR_MESSAGE = ""
INFO_COUNT =0
INFO_MESSAGE = ""
WARNING_COUNT =0
WARNING_MESSAGE =""

filepath = os.path.join(location,filename)

# Open and read log file
with open(filepath , 'r') as file:
    for each in file:
        if "ERROR" in each:
            ERROR_COUNT+=1
            ERROR_MESSAGE = each

        if "INFO" in each:
            INFO_COUNT+=1
            INFO_MESSAGE = each

        if "WARNING" in each:
            WARNING_COUNT+=1
            WARNING_MESSAGE = each

# print  error count and last error message
print(f'ERROR COUNT {ERROR_COUNT}')
print(f'LATEST ERROR MESSAGE {ERROR_MESSAGE}')

print(f'INFO COUNT {INFO_COUNT}')
print(f'LATEST INFO MESSAGE {INFO_MESSAGE}')

print(f'WARNING COUNT {WARNING_COUNT}')
print(f'LATEST WARNING MESSAGE {WARNING_MESSAGE}')