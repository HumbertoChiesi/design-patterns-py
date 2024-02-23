from Observer.procedural.subjects.subject import subscribe
from Observer.lib.util import send_email

# Dictionary mapping events to their corresponding email messages
event_messages = {
    "package_created": "was created",
    "package_canceled": "was canceled",
    "package_shipped": "in on the way!!",
    "package_arrived": "just arrived!!"
}


def send_package_email(package, message):
    send_email(package.receiver.name, package.receiver.email, f"package {package.tracking_number} {message}")
    send_email(package.shipper.name, package.shipper.email, f"package {package.tracking_number} {message}")


def setup_email_event_handlers():
    for event, message in event_messages.items():
        subscribe(event, lambda package, msg=message: send_package_email(package, msg))
