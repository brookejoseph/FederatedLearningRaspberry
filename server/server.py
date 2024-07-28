import flwr as fl
from config import *

# Define strategy
strategy = fl.server.strategy.FedAvg(
    min_fit_clients=2,
    min_eval_clients=2,
    min_available_clients=2,
)

# Start Flower server
fl.server.start_server(server_address=SERVER_ADDRESS, strategy=strategy)
