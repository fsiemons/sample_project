import pandas as pd
import subprocess
import unittest


data_file = 'test_data.txt'


class TestAppOutput(unittest.TestCase):

    def run_app(self, first, second):
        result = subprocess.run(
            ['python3', 'app.py', str(first), str(second)],
            capture_output=True,
            text=True
        )

        return result

    def test_add_numbers_from_table_file(self):
        data = pd.read_csv(data_file, header=None, sep=';')
        first_nums = data.iloc[:, 0]
        second_nums = data.iloc[:, 1]
        expected_sums = data.iloc[:, 2]

        for index in range(len(first_nums)):
            with self.subTest(index=index):
                first = first_nums.iloc[index]
                second = second_nums.iloc[index]
                expected_sum = expected_sums.iloc[index]
                print(f"f {first}, s {second}")
                result = self.run_app(first, second)
                print(f" the result is: {result}")

                self.assertEqual(expected_sum, float(result.stdout.strip()))


if __name__ == '__main__':
    unittest.main()
