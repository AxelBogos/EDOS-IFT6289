import os
from pathlib import Path

import pandas as pd
import pyrootutils


class FilePreprocessor:
    @staticmethod
    def merge(feature_df: pd.DataFrame, labels_df: pd.DataFrame, label_col: str) -> pd.DataFrame:
        """The merge function takes two dataframes as input: a feature dataframe and a labels
        dataframe. It then merges the two on the 'rewire_id' column, which is common to both. The
        function then renames the label column from the labels df to 'target'. Finally, it returns
        this merged df.

        :param feature_df:pd.DataFrame: Specify the dataframe containing the features
        :param labels_df:pd.DataFrame: Specify the labels dataframe
        :param label_col:str: Specify which column in the labels_df contains the target variable
        :return: A dataframe with the features and labels merged on the rewire_id column
        """

        labels_df = labels_df[["rewire_id", label_col]]

        # Merge the dataframes on the common 'rewire_id' column
        merged_df = pd.merge(feature_df, labels_df, on="rewire_id", how="left")

        # rename label cols to standard 'target'
        merged_df = merged_df.rename(columns={label_col: "target"})

        # Return the merged dataframe
        return merged_df

    def run(self) -> None:
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Saves the merged dataset to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: None
        """
        pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

        data_root = Path(pyrootutils.find_root(), "data", "edos_raw").resolve().as_posix()

        all_data = pd.read_csv(os.path.join(data_root, "edos_labelled_aggregated.csv"))

        # Load dev sets
        dev_task_a = pd.read_csv(os.path.join(data_root, "dev_task_a_entries.csv"))
        dev_task_b = pd.read_csv(os.path.join(data_root, "dev_task_b_entries.csv"))
        dev_task_c = pd.read_csv(os.path.join(data_root, "dev_task_c_entries.csv"))

        # Load test sets
        test_task_a = pd.read_csv(os.path.join(data_root, "test_task_a_entries.csv"))
        test_task_b = pd.read_csv(os.path.join(data_root, "test_task_b_entries.csv"))
        test_task_c = pd.read_csv(os.path.join(data_root, "test_task_c_entries.csv"))

        # Merge dev sets
        dev_task_a_labelled = self.merge(dev_task_a, all_data, "label_sexist")
        dev_task_b_labelled = self.merge(dev_task_b, all_data, "label_category")
        dev_task_c_labelled = self.merge(dev_task_c, all_data, "label_vector")

        # Merge test sets
        test_task_a_labelled = self.merge(test_task_a, all_data, "label_sexist")
        test_task_b_labelled = self.merge(test_task_b, all_data, "label_category")
        test_task_c_labelled = self.merge(test_task_c, all_data, "label_vector")

        # Save merged dev tests
        dev_task_a_labelled.to_csv(os.path.join(data_root, "dev_task_a_labelled.csv"), index=False)
        dev_task_b_labelled.to_csv(os.path.join(data_root, "dev_task_b_labelled.csv"), index=False)
        dev_task_c_labelled.to_csv(os.path.join(data_root, "dev_task_c_labelled.csv"), index=False)

        # Save merged test sets
        test_task_a_labelled.to_csv(
            os.path.join(data_root, "test_task_a_labelled.csv"), index=False
        )
        test_task_b_labelled.to_csv(
            os.path.join(data_root, "test_task_b_labelled.csv"), index=False
        )
        test_task_c_labelled.to_csv(
            os.path.join(data_root, "test_task_c_labelled.csv"), index=False
        )


if __name__ == "__main__":
    FilePreprocessor().run()
