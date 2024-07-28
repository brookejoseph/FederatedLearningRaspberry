import flwr as fl
import tensorflow as tf
from config import *
from utils import load_data, build_model

# Load and preprocess data
x_train, y_train, x_test, y_test = load_data()

# Build and compile model
model = build_model()
model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])

# Define Flower client
class FlowerClient(fl.client.NumPyClient):
    def get_parameters(self):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        model.fit(x_train, y_train, epochs=1, batch_size=32)
        return model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}

# Start Flower client
fl.client.start_numpy_client(server_address=SERVER_ADDRESS, client=FlowerClient())
