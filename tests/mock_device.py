from zorg.adaptor import Adaptor
from mock import Mock


def MockAdaptor():
    mock_adaptor = Mock(spec=Adaptor)

    mock_adaptor.analog_write = Mock()
    mock_adaptor.analog_read = Mock(return_value=500)

    mock_adaptor.digital_write = Mock()
    mock_adaptor.digital_read = Mock(return_value=1.0)

    mock_adaptor.servo_write = Mock()
    mock_adaptor.servo_read = Mock(return_value=150)

    return mock_adaptor
