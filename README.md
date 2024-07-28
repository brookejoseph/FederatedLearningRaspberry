# Federated Learning with Raspberry Pi

This repository contains the code to set up a federated learning system using a Raspberry Pi as the client. Federated learning allows multiple devices to collaboratively learn a shared model while keeping the training data on the device.

## Repository Structure

- `client/`: Contains the code for the Raspberry Pi client.
- `server/`: Contains the code for the central server that coordinates federated learning.
- `README.md`: This file, providing an overview and setup instructions for the project.

## Requirements

### General Requirements
- Python 3.7+
- TensorFlow or PyTorch
- `flwr` (Flower framework for federated learning)

### Client Requirements (Raspberry Pi)
- Raspberry Pi (preferably the latest model)
- `client/requirements.txt`: Required Python packages for the client

### Server Requirements
- Sufficient computational resources to run the federated learning server
- `server/requirements.txt`: Required Python packages for the server

## Setup Instructions

### Server Setup
1. Navigate to the `server/` directory.
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    python server.py
    ```

### Client Setup (Raspberry Pi)
1. Navigate to the `client/` directory.
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the client:
    ```bash
    python client.py
    ```

## Configuration

### Client Configuration (`client/config.py`)
- `SERVER_ADDRESS`: The address of the federated learning server.
- `DATASET_PATH`: The path to the dataset used by the client.

### Server Configuration (`server/config.py`)
- `SERVER_ADDRESS`: The address for the federated learning server to listen on.

## Utility Functions

### Server Utilities (`server/utils.py`)
- `setup_logging(log_file="server.log")`: Sets up logging to a file and console.
- `log_info(message)`: Logs an informational message.
- `log_error(message)`: Logs an error message.
- `save_model(model, model_dir="models", model_name="model.h5")`: Saves the model to the specified directory.
- `load_model(model_dir="models", model_name="model.h5")`: Loads the model from the specified directory.
- `save_config(config, config_path="config.json")`: Saves the configuration to a JSON file.
- `load_config(config_path="config.json")`: Loads the configuration from a JSON file.

## Running the Federated Learning System

1. **Start the Server**: Ensure the server is running on a machine with sufficient resources.
2. **Start the Client**: Run the client script on the Raspberry Pi.
3. The server and client will communicate to perform federated learning.

## References

- [Flower Framework](https://flower.dev/)
- [Federated Learning Concepts](https://www.tensorflow.org/federated)

## Example Usage

### Starting the Server
```bash
cd server/
pip install -r requirements.txt
python server.py
