import re
import string

import pandas as pd
import spacy


class TextPreprocessor:
    """Preprocessing wrapper class. It implements the following:

    - def __init__(...):
        -Sets up the boolean internal states for which preprocessing to do
    - def fit(...):
        - Does nothing, included to respect a scikit-learn style access
    - def transform(...):
        - Applies the preprocessing to a string or a pandas.Series of strings
    """

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
    ) -> None:
        """The __init__ function is called when an instance of the class is created. It initializes
        all the variables that are passed into it, and sets them as attributes of the object. In
        this case, we're passing in an optional set of stop words , which will be used to filter
        out common English words (spacy stopwords are used by default). We also pass in flags for
        each of the preprocessing steps that we can toggle on or off.

        :param self: Reference the class instance
        :param stop_words=None: Pass in a set of stop words. Spacy stopwords by default.
        :param lower=True: Convert all the text to lowercase
        :param remove_multispace=True: Convert multiple spaces in the text to single space
        :param remove_punc=True: Remove punctuation from the text
        :param remove_spec_chars=True: Remove special characters
        :param remove_stop_words=True: Remove stop words from the text
        :param tokenize=True: Specify whether the text should be tokenized or not
        :param lemmatize=True: Lemmatize the words
        :param remove_handles=True: Remove the Twitter handles from the tweets
        :return: None
        """
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

    def fit(self, x: pd.Series | str) -> None:
        """Placeholder function to match scikit-learn pattern.

        :param self: Refer to the object that is calling the method
        :param x:pd.Series|str: Specify the string to fit
        :return: None
        """
        return None

    def transform(self, x) -> pd.Series | str:
        """The transform function takes in a pandas Series|str and returns a pre-processed pandas
        Series|str. The transform function does the following:

            - If self.lower is True, it converts all characters to lowercase.
            - If self.remove_punc is True, it removes punctuation from the text. Punctuation characters are defined by self.punctuation
            - If self.remove_spec_chars is True, it removes special characters from the text using regex via re
            - If self.tokenize is True, it tokenizes the text using spacy
            - If self.lemmatize is True, it lemmatizes the text using spacy
            - If self.remove_handles is True, it removes handles starting with "@" via re
            - If self.remove_multispace is True, it replaces multisplaces with a single space

        :param self: Access the attributes and methods of the class in python
        :param x: The data to be transformed.
        :return: Transformed pd.Series | str
        """
        if self.lower:
            x = x.str.lower()
        if self.remove_punc:
            x = x.apply(lambda x: re.sub(f"[{self.punctuation}]+", " ", x))
        if self.remove_spec_chars:
            x = x.apply(
                lambda x: re.sub(r"(@[A-Za-z0-9]+)|(https?://[A-Za-z0-9./]+)|(\w+:\/\/\S+)", "", x)
            )
        if self.tokenize:
            x = x.apply(
                lambda x: " ".join(
                    [
                        word.text
                        for word in self.nlp(x)
                        if word.text.lower() not in self.stop_words and not word.is_punct
                    ]
                )
            )
        if self.lemmatize:
            x = x.apply(lambda x: " ".join([word.lemma_ for word in self.nlp(x)]))
        if self.remove_handles:
            x = x.apply(lambda x: re.sub(r"[^\x00-\x7F]+", "", x))
        if self.remove_multispace:
            x = x.str.replace(r"\s+", " ")
        return x
