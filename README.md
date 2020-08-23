# web-monitor

Little discovery project : a web application to display computer informations (CPU, RAM, OS...).

## Description

The front-end and back-end communicate via HTTP and websocket. Static information (platform, number of CPU cores... etc) is sent via HTTP when the web application opens. Dynamic information (RAM, CPU times... etc) is sent continuously via websocket.  

## Getting started

#### Prerequisites
* Python 3.8
* pip

#### Installation

```
git clone https://github.com/Gyskard/web-monitor
cd ./web-monitor/src/back
pip install -r requirements.txt
uvicorn main:app --reload
```

### technologies

* **front** : VueJs
* **link** : WebSocket
* **back** : FastAPI
