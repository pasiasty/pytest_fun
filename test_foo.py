import pytest
import time


@pytest.mark.parametrize("test_input", [x for x in range(4)])
def test_a(test_input, gpu):
    print('Hello', gpu)
    time.sleep(1)
