# Simple Messaging Service Using RabbitMQ

## Installation

### Prerequisites
- Docker and docker-compose
- Python3.7 or greater
- Virtualenv (Python venv)
- Git (optional)

### Setup Instructions
1. **Clone the repository** (optional if you download the project as a zip file):
   ```
   git clone https://github.com/modhpranav/upwork_testTask.git
   cd upwork_testTask
   ```
2. **Create virtualenv** (optional if you want to use the existing virtualenv):
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies**:
    ```
    pip3 install -r requirements.txt
    ```
4. **Build the Docker container for starting RabbitMQ**:
   ```
   docker-compose up --build
   or for latest docker compose version 
   docker compose up --build
   ```
5. **Start Consumer service**:
   ```
   python3 consumer.py
   ```
6. **Start Producer service**:
    ```
    python3 producer.py
    ```
7. **Configuring the delay**:
    To configure delay you can modify the delay time in config.json file directly or:
    
    ```
    python3 update_delay.py <delay>
    ```
