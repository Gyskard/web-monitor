from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
from fastapi.middleware.cors import CORSMiddleware

import psutil, typing, json, time, datetime, platform, socket, asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def getCpuTimesPercents():
    cpuTimesPercent = psutil.cpu_times_percent()
    return {'user': cpuTimesPercent[0], 'system': cpuTimesPercent[1], 'idle': cpuTimesPercent[2]}

def getCpuNumber():
    return {'logical': psutil.cpu_count(), 'physical': psutil.cpu_count(logical=False)}

def getCpuFrequence():
    return round(psutil.cpu_freq()[0])

def getMemory():
    virtualMemory = psutil.virtual_memory()
    swapMemory = psutil.swap_memory()
    return(
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
    return diskUsage

def getNetworkUsage():
    networkUsage = psutil.net_io_counters()
    return (
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
    return users

def getArchitecture():
    return platform.architecture()[0]

def getInstructionSet():
    return platform.machine()

def getNetworkName():
    return platform.node()

def getPlatform():
    return platform.platform()
    
def getProcessorName():
    return platform.processor()

def getSystem():
    return platform.system()

def getVersion():
    return platform.version()

def getHostname():
    return socket.gethostname()

def getIp():
    return socket.gethostbyname(socket.gethostname())

getCpuTimesPercents() #initilization

time.sleep(1)

# consistent value

cpuNumber = getCpuNumber()
architecture = getArchitecture()
instructionSet = getInstructionSet()
networkName = getNetworkName()
theplatform = getPlatform()
processorName = getProcessorName()
system = getSystem()
version = getVersion()
bootTime = getBootTime()
hostname = getHostname()
ip = getIp()

@app.get("/")
async def root():
    return "It works!"

@app.get("/staticvalue")
async def initilization():
    return {
        "processor": {
            "name": processorName,
            "cpuNumber": cpuNumber,
            "instructionSet": instructionSet,
        },
        "os": {
            "platform": theplatform,
            "networkName": networkName,
            "system": system,
            "version": version,
            "architecture": architecture,
            "bootTime": bootTime
        },
        "network": {
            "hostname": hostname,
            "ip": ip
        }
    }

@app.websocket("/dynamicvalue")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(1)
        await websocket.send_json({
                "processor": {
                    "cpuTimesPercents": getCpuTimesPercents(),
                    "cpuFrequence": getCpuFrequence()
                },
                "memory": getMemory(),
                "diskUsage": getDiskUsage(),
                "networkUsage": getNetworkUsage(),
                "users": getUsers()
        })