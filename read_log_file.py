ERROR_COUNT =0
ERROR_MESSAGE = ""
INFO_COUNT =0
INFO_MESSAGE = ""
WARNING_COUNT =0
WARNING_MESSAGE =""

# Open and read log file
with open('logfile') as file:
    for each in file:
        if each contains "ERROR":
            ERROR_COUNT+=1
            ERROR_MESSAGE = each

        if each contains "INFO":
            INFO_COUNT+=1
            INFO_MESSAGE = each

        if each contains "WARNING":
            WARNING_COUNT+=1
            WARNING_MESSAGE = each

# print  error count and last error message
print(f'ERROR COUNT {ERROR_COUNT}')
print(f'LATEST ERROR MESSAGE {ERROR_MESSAGE}')

print(f'INFO COUNT {INFO_COUNT}')
print(f'LATEST INFO MESSAGE {INFO_MESSAGE}')

print(f'WARNING COUNT {WARNING_COUNT}')
print(f'LATEST WARNING MESSAGE {WARNING_MESSAGE}')