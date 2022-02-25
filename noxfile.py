import os
import nox


@nox.session(name="test", python=["3.8"])
def test(session):
    """Run all the package tests. we need to run also python 3.6 for support in cloudworks python version."""
    env = {
        # "PYTHONPATH": "/".join(os.getcwd().split("/")[:-1]),
    }
    session.install("-r", "dev-requirements.txt")
    session.install("-e", ".")
    session.run(
        "coverage",
        "run",
        "--rcfile",
        "setup.cfg",
        "-m",
        "pytest",
        "--cov",
        "theoneapi_sdk",
        "--cov-fail-under",
        "65",
        "--cov-config",
        "setup.cfg",
        env=env,
    )
