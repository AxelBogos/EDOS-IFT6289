from typing import List, Tuple

from torch.utils.data import Dataset


class BinaryClassificationDataset(Dataset):
    def __init__(self, data: List[Tuple[str, int]], tokenizer, max_length):
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, label = self.data[idx]
        encoded_text = self.tokenizer(
            text, padding="max_length", truncation=True, max_length=128, return_tensors="pt"
        )
        input_ids = encoded_text["input_ids"].squeeze()
        attention_mask = encoded_text["attention_mask"].squeeze()
        return input_ids, attention_mask, label
