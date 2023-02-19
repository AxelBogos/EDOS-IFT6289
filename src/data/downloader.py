import os
from pathlib import Path

import gdown
import pyrootutils


class GoogleDriveDownloader:
    def __init__(
        self,
        output_dir: str = "edos_raw",
        download_unlabeled: bool = False,
        links_dict: dict = None,
    ) -> None:

        pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
        default_files_links = {
            "dev_task_a_entries.csv": "https://drive.google.com/file/d/1gEH44dxE0jH87C-JHLxDnqMRvKbHXwxA/view?usp=share_link",
            "dev_task_b_entries.csv": "https://drive.google.com/file/d/169_3cdbeU3x3PO9TUD1CL6wmqLNRxZz_/view?usp=share_link",
            "dev_task_c_entries.csv": "https://drive.google.com/file/d/1FhHM7x-MFw0e4T31vzzyddwKVhc2Rnk3/view?usp=share_link",
            "test_task_a_entries.csv": "https://drive.google.com/file/d/1uOtCjiqYUGjECUfbr2VTkE7NUZ7bBD4P/view?usp=share_link",
            "test_task_b_entries.csv": "https://drive.google.com/file/d/1WniGdTKzlalchoPrntxyTAI6n9aRGnVB/view?usp=share_link",
            "test_task_c_entries.csv": "https://drive.google.com/file/d/1u0FB_K11WAyHbmOy2M_25nJ5XxEpSyH5/view?usp=share_link",
            "train_all_tasks.csv": "https://drive.google.com/file/d/1XVJMR4j_-_C_6D-tfIh6_KrYYhv7bv8R/view?usp=share_link",
            "edos_labelled_aggregated.csv": "https://drive.google.com/file/d/1wzu_ERah3iTTt3gWZY342c7GFZSUlPLJ/view?usp=share_link",
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
        self.verify_output_dir()

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

    def verify_output_dir(self) -> None:
        if os.path.isdir(self.output_dir):
            print(f"Directory {self.output_dir} already exists. Continuing.")
        else:
            os.mkdir(self.output_dir)
            print(f"Directory {self.output_dir} created. Continuing.")

    def _download_file_helper(self, file_name: str, url: str) -> None:
        output_path = Path(self.output_dir, file_name).resolve().as_posix()
        if os.path.isfile(output_path):
            print(f"{file_name} already exists in {self.output_dir}. Continuing.")
            return
        gdown.download(url, output_path, quiet=False, fuzzy=True)


if __name__ == "__main__":
    downloader = GoogleDriveDownloader()
    downloader.download()
