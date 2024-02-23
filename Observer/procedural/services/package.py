from Observer.lib.DB import create_package, PackageStatus, update_package_status
from Observer.procedural.subjects.subject import post_subject


def register_new_package(destination_address, receiver, shipper):
    package = create_package(destination_address, receiver, shipper)

    post_subject("package_created", package)


def ship_package(package_id):
    package = update_package_status(package_id, PackageStatus.SHIPPED)

    post_subject("package_shipped", package)


def package_arrived(package_id):
    package = update_package_status(package_id, PackageStatus.DELIVERED)

    post_subject("package_arrived", package)


def cancel_package(package_id):
    package = update_package_status(package_id, PackageStatus.CANCELED)

    post_subject("package_canceled", package)
