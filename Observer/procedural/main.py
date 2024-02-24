from Observer.lib.DB import User
from Observer.procedural.observers.email_listener import setup_email_event_handlers
from Observer.procedural.services.package import register_new_package, ship_package, package_arrived, cancel_package

user_1 = User(1239126, "Roberto", "user1@email.com")
user_2 = User(4125157, "Luis", "user2@email.com")


def main():
    setup_email_event_handlers()

    register_new_package("Rua teste 330", user_1, user_2)
    ship_package(0)
    package_arrived(0)

    print("=" * 40)
    print("=" * 40)

    
    print("="*40)
    print("=" * 40)

    register_new_package("Rua do nunca 330", user_2, user_1)
    ship_package(1)
    cancel_package(1)


if __name__ == "__main__":
    main()