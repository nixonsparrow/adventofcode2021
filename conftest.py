def pytest_addoption(parser):
    parser.addoption('--ignored', action='store_true', dest="ignored",
                 default=False, help="enable ignored decorated tests")


def pytest_configure(config):
    if not config.option.ignored:
        setattr(config.option, 'markexpr', 'not ignored')
