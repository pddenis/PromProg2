import logging

def setup_logging():
    """Настройка логирования"""
    logging.basicConfig(level=logging.INFO)

def hello():
    """Print hello message"""
    logging.info("Hello function called")
    print("Hello from lab!")

def greet(name):
    logging.info(f"Greet function called with {name}")
    print(f"Hello, {name}!")

def main():
    setup_logging()
    greet("World")
    farewell("World")

if __name__ == "__main__":
    main()

def farewell(name):
    """Прощальная функция"""
    logging.info(f"Farewell function called with {name}")
    print(f"Goodbye, {name}!")
