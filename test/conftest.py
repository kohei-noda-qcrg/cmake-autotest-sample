import pytest

slow_opion = "--slow"
slowest_only_option="--veryslowonly"
runall_option = "--all"


def pytest_addoption(parser):
    parser.addoption(slow_opion, action="store_true", default=False, help="run slow tests")
    parser.addoption(slowest_only_option, action="store_true", default=False, help="run slowest tests only")
    parser.addoption(runall_option, action="store_true", default=False, help="run all tests")
    parser.addoption(
        "--parallel",
        type=int,
        default=1,
        help="run tests in parallel processes",
    )


@pytest.fixture
def the_number_of_process(request):
    return request.config.getoption("--parallel")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")
    config.addinivalue_line("markers", "veryslowonly: mark test as veryslowonly to run")
    config.addinivalue_line("markers", "all: run all tests")


def pytest_collection_modifyitems(config, items):
    skip_slow = pytest.mark.skip(reason=f"need {slow_opion} or {runall_option} option to run. REASON: Slow test")
    skip_slowest = pytest.mark.skip(reason=f"need {runall_option} option to run. REASON: Slow test")
    skip_other_than_slowest = pytest.mark.skip(reason=f"Skipped because the {slowest_only_option} option is set.")
    if config.getoption(runall_option):
        return
    for item in items:
        if item.get_closest_marker("veryslowonly"):
            if not config.getoption(runall_option) and not config.getoption(slowest_only_option):
                item.add_marker(skip_slowest)
        else:
            if config.getoption(slowest_only_option):
                item.add_marker(skip_other_than_slowest)
            elif item.get_closest_marker("slow") and not config.getoption(slow_opion) and not config.getoption(runall_option):
                item.add_marker(skip_slow)
