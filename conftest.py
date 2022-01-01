def pytest_addoption(parser):
    parser.addoption('--finished', action='store_true', dest="finished",
                     default=False, help="enable finished decorated tests")


def pytest_configure(config):
    if not config.option.finished:
        setattr(config.option, 'markexpr', 'not finished')
