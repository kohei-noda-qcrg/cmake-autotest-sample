import subprocess
import os
import pytest


def test() -> None:
    absolute_filepath = os.path.dirname(os.path.abspath(__file__))
    cp = subprocess.run("ls " + absolute_filepath + "/test.sh", shell=True)
    assert cp.returncode == 0


def test2() -> None:
    assert 0 == pytest.approx(10 ** -20)
