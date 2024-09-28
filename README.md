# System Monitoring Application

This project consists of two main components: an agent script (`agent.py`) that collects system information and a server (`server.py`) that receives and serves this information.

## Components

### 1. Agent (agent.py)

The agent script is responsible for collecting system information and sending it to the server. It performs the following tasks:

- Retrieves information about all running processes
- Collects system information
- Sends collected data to a specified IP and port

Key functions:
- `get_all_processes()`: Lists all running processes with their PID, name, and username
- `sysinfo()`: Prints system information using the platform module
- `send_data(data, ip, port)`: Sends collected data to the server

The agent runs continuously, collecting and sending data every 10 seconds.

### 2. Server (server.py)

The server is a Flask application that receives data from the agent and provides endpoints to access this information. It includes:

- A route to receive POST requests with computer information
- A route to retrieve stored computer information
- A simple web interface

Routes:
- `/`: Renders the main page (index.html)
- `/computer_info` (POST): Receives and stores computer information
- `/computer_info` (GET): Returns stored computer information

## Setup and Running

1. Install required dependencies:
   ```
   pip install flask psutil
   ```

2. Start the server:
   ```
   python server.py
   ```
   The server will run on `http://0.0.0.0:5000`

3. Run the agent:
   ```
   python agent.py
   ```

## Note

Ensure that the IP and port in `agent.py` match the server's address. Currently, the agent is set to connect to `127.0.0.1:10000`, which may need to be updated to match the server's actual address (`0.0.0.0:5000`).

## Future Improvements

- Implement secure communication between agent and server
- Add more detailed system monitoring features
- Create a more comprehensive web interface for data visualization

