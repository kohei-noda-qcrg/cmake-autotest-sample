import subprocess
import os
# import pytest


# def err() -> None:
#     print("err")


# @pytest.mark.default
# def test2() -> None:
#     if 1 == 1:
#         err()
#         exit(1)
#     assert 0 == pytest.approx(10 ** -20)


# @pytest.mark.performance
# def test() -> None:
#     absolute_filepath = os.path.dirname(os.path.abspath(__file__))
#     cp = subprocess.run("ls " + absolute_filepath + "/test.sh", shell=True)
#     assert cp.returncode == 0

def greptest() -> None:
    absolute_filepath = os.path.dirname(os.path.abspath(__file__))
    cp0 = subprocess.call(absolute_filepath + "/../src/a.out && ./test.sh",shell=True)
    print(cp0)
    out = subprocess.call("cat test.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",shell=True)
    # print(out.stdout)

if __name__ == "__main__":
    greptest()
