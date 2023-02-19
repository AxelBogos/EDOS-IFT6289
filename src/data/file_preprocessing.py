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


if __name__ == "__main__":
    pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

    data_root = Path(pyrootutils.find_root(), "data", "edos_raw").resolve().as_posix()

    all_data = pd.read_csv(os.path.join(data_root, "edos_labelled_aggregated.csv"))
    dev_task_a = pd.read_csv(os.path.join(data_root, "dev_task_a_entries.csv"))
    dev_task_b = pd.read_csv(os.path.join(data_root, "dev_task_b_entries.csv"))
    dev_task_c = pd.read_csv(os.path.join(data_root, "dev_task_c_entries.csv"))

    dev_task_a_labelled = FilePreprocessor.merge(dev_task_a, all_data, "label_sexist")
    dev_task_b_labelled = FilePreprocessor.merge(dev_task_b, all_data, "label_category")
    dev_task_c_labelled = FilePreprocessor.merge(dev_task_c, all_data, "label_vector")

    dev_task_a_labelled.to_csv(os.path.join(data_root, "dev_task_a_labelled.csv"), index=False)
    dev_task_b_labelled.to_csv(os.path.join(data_root, "dev_task_b_labelled.csv"), index=False)
    dev_task_c_labelled.to_csv(os.path.join(data_root, "dev_task_c_labelled.csv"), index=False)
