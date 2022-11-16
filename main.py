import requests
import json
import time
import os

root_directory = os.path.normpath(os.getcwd())
filepath = os.path.join(root_directory, "data", "questions.json")

def save_json(data, json_filename):
	json_data = json.dumps(data)
	with open(json_filename, 'w') as file:
		file.write(json_data)

def load_json(json_filename):
	with open(json_filename) as file:
		data = json.load(file)
	return data

def question_generator():
	try:
		questions = load_json(filepath)
	except Exception as e:
		questions = []

	while True:
		question = {}
		question['id'] = len(questions)
		prompt = input("Enter question prompt (q to quit):")
		if prompt == "q":
			break
		else:
			question['prompt'] = prompt
		question['answer'] = input("Enter question answer:")

		choices = ['A', 'B', 'C', 'D', 'E', 'F']
		answers = []
		for choice in choices:
			answer = input(f"Enter Answer: {choice} (q to quit)")
			if answer == "q":
				break
			else:
				answers.append(answer)
		question['answers'] = answers
		print(question)
		questions.append(question)
		save_json(questions, filepath)


if __name__ == '__main__':
	question_generator()

