from fastapi import FastAPI
import psutil, typing, json, time, datetime, platform

app = FastAPI()

def getCpuTimesPercents():
    cpuTimesPercent = psutil.cpu_times_percent()
    return json.dumps(
        {
            'userTimePercent': cpuTimesPercent[0],
            'systemTimePercent': cpuTimesPercent[1],
            'idleTimePercent': cpuTimesPercent[2]
        }
    )

def getCpuNumber():
    return json.dumps({'logical': psutil.cpu_count(), 'physical': psutil.cpu_count(logical=False)})

def getCpuFrequence():
    return round(psutil.cpu_freq()[0])

def getMemory():
    virtualMemory = psutil.virtual_memory()
    swapMemory = psutil.swap_memory()
    return json.dumps(
        {
            'virtualMemory': {
                'total': virtualMemory[0],
                'available': virtualMemory[1],
                'used': virtualMemory[3],
                'free': virtualMemory[4]
            },
            'swapMemory': {
                'total': swapMemory[0],
                'used': swapMemory[1],
                'free': swapMemory[2]
            }
        }
    )

def getDiskUsage():
    diskUsage = {}
    for device in psutil.disk_partitions():
        diskUsage[device[0]] = {
            'total': psutil.disk_usage(device[0])[0],
            'used': psutil.disk_usage(device[0])[1],
            'free': psutil.disk_usage(device[0])[2]
        }
    return json.dumps(diskUsage)

def getNetworkUsage():
    networkUsage = psutil.net_io_counters()
    return json.dumps(
        {
            'bytesSent': networkUsage[0],
            'bytesReceive': networkUsage[1],
            'packetsSent': networkUsage[2],
            'packetsReceive': networkUsage[3] 
        }
    )

def getBootTime():
    return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

def getUsers():
    users = []
    for user in psutil.users():
        users.append(user[0])
    return json.dumps(users)

def getArchitecture():
    return platform.architecture()[0]

def getMachine():
    return platform.machine()

def getComputerNetworkName():
    return platform.node()

def getPlatform():
    return platform.platform()
    
def getProcessorName():
    return platform.processor()

def getSystem():
    return platform.system()

def getVersion():
    return platform.version()

getCpuTimesPercents() #initilization

time.sleep(1)

print(getVersion())

@app.get("/")
async def root():
    return "It works!"