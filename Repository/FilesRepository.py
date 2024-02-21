from abc import ABC
from dataclasses import dataclass
import os
from typing import List

from Repository.repository import Repository, ID

import pandas as pd


@dataclass
class CSV:
    id: str
    content: pd.DataFrame


class CSVFileRepository(Repository[CSV]):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(self.directory_path):
            os.makedirs(self.directory_path)

    def get(self, id: str) -> CSV:
        csv_path = os.path.join(self.directory_path, id + ".csv")
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

        file_path = os.path.join(self.directory_path, f"{kwargs['id']}.csv")
        kwargs['content'].to_csv(file_path, index=False)

    def delete(self, id: str) -> None:
        file_path = os.path.join(self.directory_path, f"{id}.csv")
        if os.path.exists(file_path):
            os.remove(file_path)