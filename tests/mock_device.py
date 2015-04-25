from zorg.driver import Driver
from mock import Mock


def MockDriver():
    mock_driver = Mock(spec=Driver)

    mock_driver.analog_read = Mock(return_value=500)
    mock_driver.digital_read = Mock(return_value=500)

    mock_driver.analog_write = Mock()
    mock_driver.digital_write = Mock()

    return mock_driver
