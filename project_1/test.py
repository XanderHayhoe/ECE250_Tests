import subprocess
import os

def run_test(test_number):
    input_file = os.path.join("in", f"test{test_number:02d}.in")
    output_file = os.path.join("out", f"test{test_number:02d}.out")
    print(input_file, output_file)

    try:
        # Run your program with Valgrind for memory analysis
        #valgrind_cmd = ["valgrind", "./a.out"]
        #print(f"./" + {input_file})
        print(f"valgrind ./a.out < ./{input_file}")
        result = subprocess.run([f"valgrind ./a.out < ./{input_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        expected_output = open(output_file, "r").read()

        if "ERROR SUMMARY: 0 errors" in result.stderr:
            if result.stdout == expected_output:
                print(f"passed test{test_number:02d}")
            else:
                print(f"failed test{test_number:02d}: Output mismatch")
        else:
            print(f"failed test{test_number:02d}: Memory leak detected")
    except subprocess.CalledProcessError as e:
        print(f"failed test{test_number:02d}: Execution error - {e}")
    except FileNotFoundError:
        print(f"failed test{test_number:02d}: Required files not found")
    except Exception as e:
        print(f"failed test{test_number:02d}: An error occurred - {e}")

num_test_cases = int(input("Please enter the number of tests you will be running: "))

for test_number in range(1, num_test_cases + 1):
    run_test(test_number)
