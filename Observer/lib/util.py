from datetime import datetime


def send_email(name: str, email: str, message: str):
    log(f"EMAIL sent to {name} - {email}: {message}")


def log(msg: str):
    print(f"{datetime.now()} - {msg}")


def get_stocks():
    stocks = {
        "PETR4.SA": 28.50,
        "VALE3.SA": 112.75,
        "ITUB4.SA": 31.80,
        "BBDC4.SA": 25.65,
        "B3SA3.SA": 20.15
    }

    return stocks