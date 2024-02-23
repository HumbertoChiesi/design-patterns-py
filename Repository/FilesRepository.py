import pathlib
from dataclasses import dataclass
import os
from typing import List

from Repository.repository import Repository

import pandas as pd


@dataclass
class CSV:
    id: str
    content: pd.DataFrame

    def __eq__(self, other):
        if not isinstance(other, CSV):
            return False
        return self.id == other.id and self.content.equals(other.content)


class CSVFileRepository(Repository[CSV]):
    def __init__(self, directory_path: pathlib.Path):
        self.directory_path = directory_path
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(self.directory_path):
            os.makedirs(self.directory_path)

    def get(self, id: str) -> CSV:
        csv_path = os.path.join(self.directory_path, id + ".csv")

        if not os.path.exists(csv_path):
            raise ValueError("File does not exist.")

        csv = CSV(id=id, content=pd.read_csv(csv_path))
        return csv

    def get_all(self) -> List[CSV]:
        files = os.listdir(self.directory_path)
        csv_files = [file for file in files if file.endswith(".csv")]

        csv_list = []

        for file in csv_files:
            csv_id = file.replace('.csv', '')
            csv = CSV(id=csv_id, content=pd.read_csv(os.path.join(self.directory_path, file)))
            csv_list.append(csv)

        return csv_list

    def add(self, **kwargs: object) -> None:
        if 'id' not in kwargs or 'content' not in kwargs:
            raise ValueError("Both 'id' and 'content' must be provided.")

        if not isinstance(kwargs['content'], pd.DataFrame):
            raise TypeError("'content' must be a pandas DataFrame.")

        csv_path = os.path.join(self.directory_path, f"{kwargs['id']}.csv")

        if os.path.exists(csv_path):
            raise ValueError(f"{csv_path} already exists use update instead")

        kwargs['content'].to_csv(csv_path, index=False)

    def update(self, **kwargs: object) -> None:
        if 'id' not in kwargs or 'content' not in kwargs:
            raise ValueError("Both 'id' and 'content' must be provided.")

        if not isinstance(kwargs['content'], pd.DataFrame):
            raise TypeError("'content' must be a pandas DataFrame.")

        csv_path = os.path.join(self.directory_path, f"{kwargs['id']}.csv")

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_path} does not exist")

        kwargs['content'].to_csv(csv_path, index=False)

    def delete(self, id: str) -> None:
        csv_path = os.path.join(self.directory_path, f"{id}.csv")

        if not os.path.exists(csv_path):
            raise ValueError("File does not exist.")

        os.remove(csv_path)
