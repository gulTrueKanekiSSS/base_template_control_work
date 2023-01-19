import pytest

from utils import load_data


def test_load_data():
    assert type(load_data()) == list, 'формат не является json'
    assert type(load_data()[0]) == dict, 'ты харош'

def test_search_train(train_name):
    for i in range(len(load_data)):
        assert type(test_search_train(i)) == list