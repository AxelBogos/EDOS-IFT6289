import re
import string

import spacy


class TextPreprocessor:
    def __init__(
        self,
        stop_words=None,
        lower=True,
        remove_multispace=True,
        remove_punc=True,
        remove_spec_chars=True,
        remove_stop_words=True,
        tokenize=True,
        lemmatize=True,
        remove_handles=True,
    ):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = (
            set(spacy.lang.en.stop_words.STOP_WORDS) if stop_words is None else stop_words
        )
        self.punctuation = string.punctuation

        # Preprocessing flags. Additional test comment.
        self.lower = lower
        self.remove_multispace = remove_multispace
        self.remove_punc = remove_punc
        self.remove_spec_chars = remove_spec_chars
        self.remove_stop_words = remove_stop_words
        self.tokenize = tokenize
        self.lemmatize = lemmatize
        self.remove_handles = remove_handles

    def fit(self, X):
        return self

    def transform(self, X):
        if self.lower:
            X = X.str.lower()
        if self.remove_punc:
            X = X.apply(lambda x: re.sub(f"[{self.punctuation}]+", " ", x))
        if self.remove_spec_chars:
            X = X.apply(
                lambda x: re.sub(r"(@[A-Za-z0-9]+)|(https?://[A-Za-z0-9./]+)|(\w+:\/\/\S+)", "", x)
            )
        if self.tokenize:
            X = X.apply(
                lambda x: " ".join(
                    [
                        word.text
                        for word in self.nlp(x)
                        if word.text.lower() not in self.stop_words and not word.is_punct
                    ]
                )
            )
        if self.lemmatize:
            X = X.apply(lambda x: " ".join([word.lemma_ for word in self.nlp(x)]))
        if self.remove_handles:
            X = X.apply(lambda x: re.sub(r"[^\x00-\x7F]+", "", x))
        if self.remove_multispace:
            X = X.str.replace(r"\s+", " ")
        return X
