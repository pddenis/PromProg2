import logging

LOG_LEVEL = logging.INFO

def setup_logging():
    """Настройка логирования с обработкой ошибок"""
    try:
        logging.basicConfig(level=LOG_LEVEL)
    except Exception as e:
        print(f"Ошибка настройки логирования: {e}")

def hello():
    """Print hello message"""
    logging.info("Hello function called")
    print("Hello from lab!")

def greet(name):
    logging.info(f"Greet function called with {name}")
    print(f"Hello, {name}!")

def farewell(name):
    """Прощальная функция"""
    logging.info(f"Farewell function called with {name}")
    print(f"Goodbye, {name}!")

def main():
    setup_logging()
    greet("World")
    farewell("World")

if __name__ == "__main__":
    main()
