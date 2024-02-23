import os
import pathlib
import shutil
from Repository.FilesRepository import CSVFileRepository, CSV

import pandas as pd
import pytest

data = [
    ['Humberto', 23, 'New York'],
    ['Vinicius', 16, 'Los Angeles'],
    ['Leandro', 30, 'Chicago'],
    ['Guilherme', 46, 'Houston']
]
columns = ['Name', 'Age', 'City']
df = pd.DataFrame(data, columns=columns)

data_2 = [
    ['Humberto', 23, 'New York'],
    ['Vinicius', 16, 'Los Angeles']
]
df_2 = pd.DataFrame(data_2, columns=columns)


def setup_module():
    if os.path.exists("./csv_repo_test/"):
        shutil.rmtree("./csv_repo_test/")


def test_get_all():
    repo = CSVFileRepository(pathlib.Path("./csv_repo_test/get"))

    repo.add(id="moradores", content=df)
    repo.add(id="parentes", content=df)

    assert repo.get_all() == [CSV(id="moradores", content=df), CSV(id="parentes", content=df)]


def test_add():
    repo = CSVFileRepository(pathlib.Path("./csv_repo_test/add"))

    repo.add(id="moradores", content=df)

    assert CSV(id="moradores", content=df) == repo.get("moradores")


def test_update_non_existent():
    repo = CSVFileRepository(pathlib.Path("./csv_repo_test/update"))

    with pytest.raises(FileNotFoundError):
        repo.update(id="teste_update", content=df)


def test_update_existing():
    repo = CSVFileRepository(pathlib.Path("./csv_repo_test/update"))

    repo.add(id="moradores", content=df)
    repo.update(id="moradores", content=df_2)

    assert CSV(id="moradores", content=df_2) == repo.get("moradores")


def test_delete():
    repo = CSVFileRepository(pathlib.Path("./csv_repo_test/delete"))

    repo.add(id="moradores", content=df)
    repo.delete("moradores")

    with pytest.raises(ValueError):
        repo.get("moradores")


if __name__ == '__main__':
    pytest.main()
