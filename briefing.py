from src.config import load_config

def main():
    config = load_config()
    print(config["location_name"])

if __name__ == "__main__":
    main()
    