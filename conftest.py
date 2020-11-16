import pytest
import _pytest.config
import _pytest.config.argparsing


pytest_plugins = ["xdist"]
gpus_ = []


def pytest_addoption(parser: _pytest.config.argparsing.Parser):
    parser.addoption("--gpus", type=str, help="available gpus", required=True)


@pytest.mark.tryfirst
def pytest_xdist_setupnodes(config: _pytest.config.Config):
    if config.option.numprocesses != len(gpus_):
        raise Exception('Wrong number of numprocesses, want: {} got: {}'.format(len(gpus_), config.option.numprocesses))


@pytest.fixture()
def gpus(worker_id):
    yield gpus_.copy()


@pytest.fixture()
def gpu(worker_id):
    idx = int(worker_id[2:])
    yield gpus_[idx]


def pytest_cmdline_main(config: _pytest.config.Config):
    global gpus_
    gpus_ = config.option.gpus.split(',')
