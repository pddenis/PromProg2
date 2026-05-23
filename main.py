cat > main.py << 'EOF'
import logging

def setup_logging():
    """Настройка логирования"""
    logging.basicConfig(level=logging.INFO)

def hello():
    logging.info("Hello function called")
    print("Hello from lab!")

def greet(name):
    logging.info(f"Greet function called with {name}")
    print(f"Hello, {name}!")

def main():
    setup_logging()
    greet("World")

if __name__ == "__main__":
    main()
EOF
