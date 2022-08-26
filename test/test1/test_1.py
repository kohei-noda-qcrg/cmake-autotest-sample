import subprocess
import pytest
import os

# def err() -> None:
#     print("err")


@pytest.mark.slow
def test2() -> None:
    assert 0 == pytest.approx(10**-20)


# @pytest.mark.performance
# def test() -> None:
#     absolute_filepath = os.path.dirname(os.path.abspath(__file__))
#     cp = subprocess.run("ls " + absolute_filepath + "/test.sh", shell=True)
#     assert cp.returncode == 0


@pytest.mark.runall
def test_grep() -> None:
    absolute_filepath = os.path.dirname(os.path.abspath(__file__))
    cp0 = subprocess.call(absolute_filepath + "/../../bin/a.out", shell=True)
    print(cp0)
    out = subprocess.call(
        "cat test.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",
        shell=True,
    )
    assert cp0 == out
