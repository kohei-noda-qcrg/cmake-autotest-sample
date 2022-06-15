import subprocess
import os


def test_grep():
    absolute_filepath = os.path.dirname(os.path.abspath(__file__))
    # cp0 = subprocess.call(absolute_filepath + "/../bin/a.out", shell=True)
    # print(cp0)
    os.chdir(absolute_filepath)
    # subprocess.run("sh " + absolute_filepath + "/run.sh", shell=True)  # Run calculation
    binpath = os.path.normpath(os.path.join(absolute_filepath, "../bin/a.out"))
    p = subprocess.run(binpath, shell=True)
    cp1 = subprocess.run(
        "cat test.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",
        shell=True,
    )
    out = subprocess.run(
        "cat ref.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",
        shell=True,
    )
    assert cp1.stdout == out.stdout


if __name__ == "__main__":
    test_grep()
