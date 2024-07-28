import logging
import os
import json
import tensorflow as tf

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_logging(log_file="server.log"):
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def save_model(model, model_dir="models", model_name="model.h5"):
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, model_name)
    model.save(model_path)
    logger.info(f"Model saved to {model_path}")

def load_model(model_dir="models", model_name="model.h5"):
    model_path = os.path.join(model_dir, model_name)
    if os.path.exists(model_path):
        model = tf.keras.models.load_model(model_path)
        logger.info(f"Model loaded from {model_path}")
        return model
    else:
        logger.error(f"Model path {model_path} does not exist")
        return None

def save_config(config, config_path="config.json"):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    logger.info(f"Configuration saved to {config_path}")

def load_config(config_path="config.json"):
    """Load the configuration from a JSON file."""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    else:
        logger.error(f"Configuration path {config_path} does not exist")
        return None

if __name__ == "__main__":
    setup_logging()
    log_info("Server started")

    config = {
        "server_address": "127.0.0.1:8080",
        "min_fit_clients": 2,
        "min_eval_clients": 2,
        "min_available_clients": 2
    }

    save_config(config)
    loaded_config = load_config()
    print(loaded_config)
    
    model = tf.keras.Sequential([tf.keras.layers.Dense(10, input_shape=(784,))])
    save_model(model)
    loaded_model = load_model()
