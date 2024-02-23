import uuid
from dataclasses import dataclass
from enum import Enum

packages = list()


class PackageStatus(Enum):
    CREATED = "created"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"


@dataclass
class User:
    SSN: int
    name: str
    email: str


@dataclass
class Package:
    id: int
    tracking_number: str
    destination_address: str
    status: PackageStatus
    receiver: User
    shipper: User


def create_package(destination_address: str, receiver: User, shipper: User) -> Package:
    new_package = Package(id=len(packages), status=PackageStatus.CREATED, destination_address=destination_address
                          , receiver=receiver, shipper=shipper, tracking_number=str(uuid.uuid4()))

    packages.append(new_package)
    return new_package


def get_package(package_id: int) -> Package:
    for package in packages:
        if package.id == package_id:
            return package

    raise Exception(f"Package with id: {package_id} not found")


def update_package_status(package_id: int, status: PackageStatus):
    for package in packages:
        if package.id == package_id:
            package.status = status
            return package

    raise Exception(f"Package with id: {package_id} not found")

