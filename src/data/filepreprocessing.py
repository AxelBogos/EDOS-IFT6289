import os

from pathlib import Path
import pandas as pd


class FilePreprocessor:
    @staticmethod
    def merge(file1, file2):
        # Load the CSV files into pandas dataframes
        df1 = file1
        df2 = file2

        # Merge the dataframes on the common 'rewire_id' column
        merged_df = pd.merge(df1, df2, on='rewire_id', suffixes=('_df1', '_df2'))

        # Drop the duplicate column
        merged_df.drop('text_df2', axis=1, inplace=True)

        # Return the merged dataframe
        return merged_df.rename(columns={'text_df1': 'text'})


if __name__ == "__main__":

    if "data" in os.getcwd():
        os.chdir("../..")

    data_root = Path("data", "edos_raw").resolve().as_posix()

    all_data = pd.read_csv(os.path.join(data_root, "data_label.csv"))
    dev_task_a = pd.read_csv(os.path.join(data_root, "dev_task_a_entries.csv"))
    dev_task_b = pd.read_csv(os.path.join(data_root, "dev_task_b_entries.csv"))
    dev_task_c = pd.read_csv(os.path.join(data_root, "dev_task_c_entries.csv"))

    dev_task_a_labelled = FilePreprocessor.merge(all_data, dev_task_a)
    dev_task_b_labelled = FilePreprocessor.merge(all_data, dev_task_b)
    dev_task_c_labelled = FilePreprocessor.merge(all_data, dev_task_c)

    dev_task_a_labelled.to_csv(os.path.join(data_root, "dev_task_a_labelled.csv"), index=False)
    dev_task_b_labelled.to_csv(os.path.join(data_root, "dev_task_b_labelled.csv"), index=False)
    dev_task_c_labelled.to_csv(os.path.join(data_root, "dev_task_c_labelled.csv"), index=False)
