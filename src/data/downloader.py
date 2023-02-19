import os
from pathlib import Path

import gdown
import pyrootutils


class GoogleDriveDownloader:
    """Downloader wrapper class. It implements the following:

    - def __init__(...):
        - Sets up the download links and internal states of the downloader such as the outputh path
    - def download(...):
        - Executes the downloading of all requested files.
    - def _download_file_helper(...)
        - Executes the download of a single file
    - def _verify_output_dir(...)
        - Asserts output dir a valid existing dir
    """

    def __init__(
        self,
        output_dir: str = "edos_raw",
        download_unlabeled: bool = False,
        links_dict: dict = None,
    ) -> None:
        """The __init__ function is called when an instance of the class is created. It initializes
        attributes that are common to all instances of the class.

        :param self: Reference the object instance
        :param output_dir:str=&quot;edos_raw&quot;: Specify the name of the folder where all data will be downloaded
        :param download_unlabeled:bool=False: Download the unlabeled data
        :param links_dict:dict=None: Pass a dictionary of links to the class
        :param : Define the output directory
        :return: None
        """

        pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
        default_files_links = {
            "dev_task_a_entries.csv": "https://drive.google.com/file/d/1gEH44dxE0jH87C-JHLxDnqMRvKbHXwxA/view?usp=share_link",
            "dev_task_b_entries.csv": "https://drive.google.com/file/d/169_3cdbeU3x3PO9TUD1CL6wmqLNRxZz_/view?usp=share_link",
            "dev_task_c_entries.csv": "https://drive.google.com/file/d/1FhHM7x-MFw0e4T31vzzyddwKVhc2Rnk3/view?usp=share_link",
            "test_task_a_entries.csv": "https://drive.google.com/file/d/1uOtCjiqYUGjECUfbr2VTkE7NUZ7bBD4P/view?usp=share_link",
            "test_task_b_entries.csv": "https://drive.google.com/file/d/1WniGdTKzlalchoPrntxyTAI6n9aRGnVB/view?usp=share_link",
            "test_task_c_entries.csv": "https://drive.google.com/file/d/1u0FB_K11WAyHbmOy2M_25nJ5XxEpSyH5/view?usp=share_link",
            "train_all_tasks.csv": "https://drive.google.com/file/d/1XVJMR4j_-_C_6D-tfIh6_KrYYhv7bv8R/view?usp=share_link",
        }
        default_unlabeled_file_links = {
            "gab_1M_unlabelled.csv": "https://drive.google.com/file/d/1Uh4IP7Al779bZWf-UVW963osF-WrKCAI/view?usp=share_link",
            "reddit_1M_unlabelled.csv": "https://drive.google.com/file/d/1LGpUv7bBHepmdu5E5JlICOf47wQJy3IZ/view?usp=share_link",
        }
        self.download_unlabeled = download_unlabeled
        if links_dict is None:
            self.links_dict = default_files_links
            self.unlabeled_links_dict = default_unlabeled_file_links
        else:
            self.links_dict = links_dict

        root_data_dir = Path(pyrootutils.find_root(), "data").resolve().as_posix()
        self.output_dir = Path(root_data_dir, output_dir)

    def download(self) -> None:
        """The download function downloads the data from the links specified in the links_dict. It
        then saves them to a folder self.output_dir. If you wish to download unlabeled data, set
        download_unlabeled=True.

        :param self: Reference the class object
        :return: None
        """
        self._verify_output_dir()

        for file_name, url in self.links_dict.items():
            self._download_file_helper(file_name, url)

        if not self.download_unlabeled:
            print(
                'Please set "download_unlabeled" arg to True if you wish to download unlabeled data ('
                "~180MB).\nDownload Done."
            )
            return

        for file_name, url in self.unlabeled_links_dict.items():
            self._download_file_helper(file_name, url)
        print("Download done.")

    def _download_file_helper(self, file_name: str, url: str) -> None:
        """The _download_file_helper function downloads a file from the given url to the specified
        output directory. If the file already exists in that directory, it will not be downloaded
        again.

        :param self: Access the attributes of the class
        :param file_name:str: Specify the name of the file that will be downloaded
        :param url:str: Specify the url of the file that is to be downloaded
        :return: None
        """
        output_path = Path(self.output_dir, file_name).resolve().as_posix()
        if os.path.isfile(output_path):
            print(f"{file_name} already exists in {self.output_dir}. Continuing.")
            return
        gdown.download(url, output_path, quiet=False, fuzzy=True)

    def _verify_output_dir(self) -> None:
        """The _verify_output_dir function checks if the output directory already exists. If it
        does, the function prints a message and continues. If not, the function creates the
        directory and prints a message.

        :param self: Refer to the object itself
        :return: None
        """
        if os.path.isdir(self.output_dir):
            print(f"Directory {self.output_dir} already exists. Continuing.")
        else:
            os.mkdir(self.output_dir)
            print(f"Directory {self.output_dir} created. Continuing.")


if __name__ == "__main__":
    downloader = GoogleDriveDownloader()
    downloader.download()
