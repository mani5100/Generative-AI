from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
text = """
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def displayinfo(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"

    def is_passing(self):
        return self.grade >= 50

class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def displayinfo(self):
        return f"Teacher(name={self.name}, subject={self.subject})"

    def teaches(self, student):
        return f"{self.name} teaches {student.name}"
"""
text_splitter = RecursiveCharacterTextSplitter.from_language(Language.PYTHON)
chunks = text_splitter.split_text(text)
print(chunks)