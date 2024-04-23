# # def load_questions(file_path):
# #     with open(file_path) as file:
# #         return [line.strip().split("||") for line in file]

# # def main():
# #     file_name = 'soal.txt'
# #     print(f"nama file1: {file_name}")

# #     for question, correct_answer in load_questions(file_name):
# #         print(question)
# #         user_answer = input("Jawab: ").strip().lower()
# #         print("Jawaban benar!" if user_answer == correct_answer.lower() else "Jawaban salah!")
# #         print()

# # if __name__ == "__main__":
# #     main()

# def load_questions(file_path):
#     questions = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             question, answer = line.strip().split("||")
#             questions.append((question.strip(), answer.strip()))
#     return questions

# def main():
#     file_name = 'soal.txt'
#     questions = load_questions(file_name)
    
#     print(f"nama file1: {file_name}")
    
#     for question, correct_answer in questions:
#         print(question)
#         user_answer = input("Jawab: ").strip().lower()
#         print(f"Jawaban benar!" if user_answer == correct_answer.lower() else "Jawaban salah!")
#         print()

# if __name__ == "__main__":
#     main()

def main():
    file_name = 'soal.txt'
    
    print(f"nama file1: {file_name}")
    
    with open(file_name, 'r') as file:
        for line in file:
            question, correct_answer = map(str.strip, line.split("||"))
            print(question)
            user_answer = input("Jawab: ").strip().lower()
            print("Jawaban benar!" if user_answer == correct_answer.lower() else "Jawaban salah!")
            print()

if __name__ == "__main__":
    main()
