from datetime import datetime

from my import main
from unittest.mock import patch, Mock

from my_modules.util import get_data


@patch("my.util", Mock(return_value="dummy"))
@patch("my.get_data", Mock(return_value="some data"))
def test_main(list_mock):
    print(list_mock)
    result = main(list_mock)
    print(result)
    assert result == 'dummy'


@patch("my.util")
@patch("my.get_data")
def test_main_util_called_with_expected_parameter(get_data_mock, util_mock, list_mock):
    get_data_mock.return_value = 'some data'
    util_mock.return_value = 'dummy'
    result = main(list_mock)
    assert result == 'dummy'
    util_mock.assert_any_call('some data')


def test_main_util_called_with_expected_parameter_with(list_mock):
    with patch("my.util") as util_mock:
        util_mock.return_value = 'dummy'
        with patch("my.get_data") as get_data_mock:
            get_data_mock.return_value = 'some data'
            result = main(list_mock)
    assert result == 'dummy'
    util_mock.assert_any_call('some data')


@patch("my.util", Mock(return_value="dummy"))
@patch("my.get_data")
def test_main_get_data_called(get_data_mock, list_mock):
    get_data_mock.return_value = 'some data'
    result = main(list_mock)
    assert result == 'dummy'
    assert get_data_mock.called


@patch('my_modules.util.add_time')
def test_get_data(add_time, list_mock):  # Passing mock and fixture in conftest.py
    ct = datetime.now()
    expected = f"{ct}: There are {len(list_mock)} arguments"
    add_time.return_value = expected

    result = get_data(list_mock)

    assert expected == result
