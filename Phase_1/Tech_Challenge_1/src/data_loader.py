from pathlib import Path
import pandas as pd


def locate_dataset():
    project_root = Path(__file__).resolve().parents[1]
    return project_root / "Dataset"


def find_csv_files(dataset_dir):

    csv_files = list(dataset_dir.glob("*.csv"))

    return csv_files


def load_datasets(*csv_files):
    datasets = {}

    for file in csv_files:
        dataset_name = file.stem
        datasets[dataset_name] = pd.read_csv(file)

    return datasets