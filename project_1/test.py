import subprocess
import os
import platform
def run_test(test_number):
    input_file = os.path.join("in", f"test{test_number:02d}.in")
    output_file = os.path.join("out", f"test{test_number:02d}.out")
    print(input_file, output_file)

    try:
        if platform.system() == 'Windows': 
            result = result = subprocess.run(["a.exe"], stdin=open(input_file, "r"), stdout=subprocess.PIPE, text=True, check=True)
        else:
            result = subprocess.run(["./a.out"], stdin=open(input_file, "r"), stdout=subprocess.PIPE, text=True, check=True)
        expected_output = open(output_file, "r").read()
        if result.stdout == expected_output:
            print(f"passed test{test_number:02d}")
        else:
            print(f"failed test{test_number:02d}: Output mismatch")
    except subprocess.CalledProcessError as e:
        print(f"failed test{test_number:02d}: Execution error - {e}")
    except FileNotFoundError:
        print(f"failed test{test_number:02d}: Required files not found")
    except Exception as e:
        print(f"failed test{test_number:02d}: An error occurred - {e}")
num_test_cases = int(input("Please enter the number of tests you will be running: "))

for test_number in range(1, num_test_cases + 1):
    run_test(test_number)