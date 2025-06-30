''''''
import json

def update_config(file_path, updates):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)

        for key_path, new_value in updates.items():
            keys = key_path.split(".")
            d = config
            for k in keys[:-1]:
                d = d[k]
            d[keys[-1]] = new_value

        
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=2)

        print("Config updated successfully.")
        return config

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except KeyError as e:
        print(f"Key not found while updating: {e}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from: {file_path}")
    except Exception as e:
        print(f"Unexpected error: {e}")

updates = {
        "version": "1.1.0",
        "features.reporting": True,
        "max_users": 150
    }

updated = update_config("config.json", updates)
print(json.dumps(updated, indent=2))
