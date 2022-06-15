import subprocess
import os


def test_grep():
    absolute_filepath = os.path.dirname(os.path.abspath(__file__))
    # cp0 = subprocess.call(absolute_filepath + "/../bin/a.out", shell=True)
    # print(cp0)
    os.chdir(absolute_filepath)
    print(absolute_filepath)
    # subprocess.run("sh " + absolute_filepath + "/run.sh", shell=True)  # Run calculation
    binpath = os.path.normpath(os.path.join(absolute_filepath, "../bin/a.out"))
    p = subprocess.run(binpath, shell=True)
    output_file_path = os.path.normpath(os.path.join(absolute_filepath, "test.out"))
    print(output_file_path)
    with open(output_file_path, encoding="utf-8", mode="r") as f:
        print("output file")
        print(f.read())
    with open(output_file_path, encoding="utf-8", mode="r") as f:
        test_grep_str = [s.strip() for s in f.readlines() if "Total" in s]
    ref_file_path = os.path.normpath(os.path.join(absolute_filepath, "ref.out"))
    print(ref_file_path)
    with open(ref_file_path, encoding="utf-8", mode="r") as f:
        print("ref file")
        print(f.read())
    with open(ref_file_path, encoding="utf-8", mode="r") as f:
        ref_grep_str = [s.strip() for s in f.readlines() if "Total" in s]
    # cp1 = subprocess.run(
    #     "cat test.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",
    #     shell=True,
    # )
    # out = subprocess.run(
    #     "cat ref.out | awk '/ENERGY/{getline;print $2}$1 ~ /Total/{print $(NF - 1)}' | tr -s '\n'",
    #     shell=True,
    # )
    assert test_grep_str == ref_grep_str


if __name__ == "__main__":
    test_grep()
