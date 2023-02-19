from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
import pyrootutils


class FilePreprocessor:
    def run(self) -> None:
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing, but it does write out the data to disk
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: None
        :doc-author: Trelent
        """
        """
        The run function is the entry point for this module. It does three things:
            1. Loads the data from a CSV file into a pandas DataFrame object
            2. Merges that DataFrame with another CSV file containing labels and other metadata
            3. Encode targets to integers (train,val test sets)
            3. Saves the merged datasets to disk as a new CSV file

        :param self: Access variables that belong to the class
        :return: None
        """
        pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

        data_root = Path(pyrootutils.find_root(), "data", "edos_raw").resolve().as_posix()

        full_data = pd.read_csv(Path(data_root, "edos_labelled_aggregated.csv"))

        train_all_tasks, dev_sets, test_sets = self.load_data(data_root)

        # Merge dev sets
        dev_sets_labelled = self.merge_labels_wrapper(dev_sets, full_data)

        # Merge test sets
        test_sets_labelled = self.merge_labels_wrapper(test_sets, full_data)

        # Encode train set targets
        train_all_tasks_encoded = self.encode_target(
            train_all_tasks, self._get_task_a_target_encoding, "label_sexist"
        )
        train_all_tasks_encoded = self.encode_target(
            train_all_tasks_encoded, self._get_task_b_target_encoding, "label_category"
        )
        train_all_tasks_encoded = self.encode_target(
            train_all_tasks_encoded, self._get_task_c_target_encoding, "label_vector"
        )

        # Encode dev sets targets
        dev_sets_labelled = self.encode_target_wrapper(dev_sets_labelled)

        # Encode test sets targets
        test_sets_labelled = self.encode_target_wrapper(test_sets_labelled)

        # Save encoded train set
        train_all_tasks_encoded.to_csv(
            Path(data_root, "train_all_tasks_target_encoded.csv"), index=False
        )

        # Save merged dev tests
        self.save_csv_wrapper(dev_sets_labelled, "dev", data_root)

        # Save merged test sets
        self.save_csv_wrapper(test_sets_labelled, "test", data_root)

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

    def merge_labels_wrapper(
        self,
        all_tasks_data: Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame],
        full_data: pd.DataFrame,
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        task_a_set, task_b_set, task_c_set = all_tasks_data
        task_a_labelled = self.merge(task_a_set, full_data, "label_sexist")
        task_b_labelled = self.merge(task_b_set, full_data, "label_category")
        task_c_labelled = self.merge(task_c_set, full_data, "label_vector")
        return task_a_labelled, task_b_labelled, task_c_labelled

    @staticmethod
    def save_csv_wrapper(all_tasks_data, set_prefix: str, data_root: str) -> None:
        task_a_set, task_b_set, task_c_set = all_tasks_data
        task_a_set.to_csv(Path(data_root, f"{set_prefix}_task_a_labelled.csv"), index=False)
        task_b_set.to_csv(Path(data_root, f"{set_prefix}_task_a_labelled.csv"), index=False)
        task_c_set.to_csv(Path(data_root, f"{set_prefix}_task_a_labelled.csv"), index=False)

    @staticmethod
    def encode_target(
        df: pd.DataFrame, encoding_dict: dict, target: str = "target"
    ) -> pd.DataFrame:
        """The encode_target function takes a DataFrame and a dictionary mapping the target values
        to integers. It then replaces the target column with an encoded version of itself, using
        the encoding_dict. The function returns this new DataFrame.

        :param df:pd.DataFrame: Specify the dataframe that we want to encode
        :param encoding_dict:dict: Encode the target column
        :param target:str='target': Specify the name of the target column
        :return: The dataframe with the target column encoded
        :doc-author: Trelent
        """
        df[target].replace(encoding_dict, inplace=True)
        df[target] = df[target].astype(int)
        return df

    def encode_target_wrapper(
        self, all_tasks_data: Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        task_a_set, task_b_set, task_c_set = all_tasks_data
        task_a_set_encoded = self.encode_target(task_a_set, self._get_task_a_target_encoding)
        task_b_set_encoded = self.encode_target(task_b_set, self._get_task_b_target_encoding)
        task_c_set_encoded = self.encode_target(task_c_set, self._get_task_c_target_encoding)
        return (task_a_set_encoded, task_b_set_encoded, task_c_set_encoded)

    @staticmethod
    def load_data(
        data_root: str,
    ) -> Tuple[
        pd.DataFrame,
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame],
        Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame],
    ]:
        # Load train set
        train_set = pd.read_csv(Path(data_root, "train_all_tasks.csv"))

        # Load dev sets
        dev_task_a = pd.read_csv(Path(data_root, "dev_task_a_entries.csv"))
        dev_task_b = pd.read_csv(Path(data_root, "dev_task_b_entries.csv"))
        dev_task_c = pd.read_csv(Path(data_root, "dev_task_c_entries.csv"))

        # Load test sets
        test_task_a = pd.read_csv(Path(data_root, "test_task_a_entries.csv"))
        test_task_b = pd.read_csv(Path(data_root, "test_task_b_entries.csv"))
        test_task_c = pd.read_csv(Path(data_root, "test_task_c_entries.csv"))

        return (
            train_set,
            (dev_task_a, dev_task_b, dev_task_c),
            (test_task_a, test_task_b, test_task_c),
        )

    @property
    def _get_task_a_target_encoding(self) -> dict:
        return {"not sexist": 0, "sexist": 1}

    @property
    def _get_task_b_target_encoding(self) -> dict:
        return {
            "1. threats, plans to harm and incitement": 0,
            "2. derogation": 1,
            "3. animosity": 2,
            "4. prejudiced discussions": 3,
            "none": np.nan,
        }

    @property
    def _get_task_c_target_encoding(self) -> dict:
        return {
            "1.1 threats of harm": 0,
            "1.2 incitement and encouragement of harm": 1,
            "2.1 descriptive attacks": 2,
            "2.2 aggressive and emotive attacks": 3,
            "2.3 dehumanising attacks & overt sexual objectification": 4,
            "3.1 casual use of gendered slurs, profanities, and insults": 5,
            "3.2 immutable gender differences and gender stereotypes": 6,
            "3.3 backhanded gendered compliments": 7,
            "3.4 condescending explanations or unwelcome advice": 8,
            "4.1 supporting mistreatment of individual women": 9,
            "4.2 supporting systemic discrimination against women as a group": 10,
            "none": np.nan,
        }


if __name__ == "__main__":
    FilePreprocessor().run()