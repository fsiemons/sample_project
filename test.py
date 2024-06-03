
import pandas as pd
import subprocess
import unittest


data_file = 'test_data.txt'


class TestAppOutput(unittest.TestCase):

    def run_app(self, parameter, input):
        result = subprocess.run(
            ['python3', 'app.py', parameter],
            input=input,
            capture_output=True,
            text=True
        )

        return result

    def test_question_and_answer(self):
        data = pd.read_csv(data_file, header=None, sep=';')
        questions = data.iloc[:, 0]
        answers = data.iloc[:, 1]

        for index in range(len(answers)):
            with self.subTest(index=index):
                question = questions.iloc[index]
                answer = answers.iloc[index]
                result = self.run_app(question, answer)
                self.assertIn(question, result.stdout)
                self.assertIn(answer, result.stdout)


if __name__ == '__main__':
    unittest.main()
