import pytest
from spaCy_analysis import spaCy_analysis

class TestSpaCyAnalisys:

    def test_spaCy_analysis(self):
        form_input = 'Hello World'
        spaCy_response = spaCy_analysis(form_input)
        expected = [('Hello', 'INTJ'), ('World', 'PROPN')]
        assert spaCy_response == expected
        assert isinstance(spaCy_response, list)