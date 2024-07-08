import json
import logging
import sys

# Delay Update Method
def update_time(new_delay):
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    config['DELAY'] = new_delay
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) != 2:
        logging.error("Usage: python update_delay.py <new_delay>")
        sys.exit(1)
    
    new_delay = int(sys.argv[1])
    update_time(new_delay)
    logging.info(f"Delay updated to: {new_delay} seconds")