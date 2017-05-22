students = []

def get_studentes_titlecase():
	students_titlecase = []
	for student in students:
		students_titlecase.append(student["name"].title())
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_studentes_titlecase()
	print(students_titlecase)


def add_student(name, student_id = 3934):
	student = { "name": name, "student_id": student_id } 
	students.append(student)	


def save_file(student):
	try:
		file = open("students.txt","a")
		file.writa(stundet + "\n")
		file.close()
	except Exception:
			print('Could not save file')


def read_file()
	try:
		file = open("students.txt","r")
		for student in read_students(file):
			add_student(student)
		file.close()	
	except Exception:
			print('Could not read file')

def read_students(file):
	for line in file:
		yield line

exit = False

read_file()
print_students_titlecase()

while not exit:
	decision = input("Enter student(y/n)? ")

	if decision == 'y':
		student_name = input("Enter student name: ")
		student_id = input("Enter student id: ")

		add_student(student_name, student_id)
		save_file(student_name)
		print_students_titlecase()

	else if decision == 'n':
		exit = True

	else print("Plesase enter 'y' or 'n'.")

print("Exited")
