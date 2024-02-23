from datetime import datetime


def send_email(name: str, email: str, message: str):
    log(f"EMAIL sent to {name} - {email}: {message}")


def log(msg: str):
    print(f"{datetime.now()} - {msg}")
