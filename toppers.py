# Created by Dhavan Shekarappa on 07/15/2017


from random import randint
from pprint import pprint


def main():

    # Initialize data
    sections = ["sec-A", "sec-B", "sec-C", "sec-D", "sec-E"]

    courses = ["Physics", "Algebra", "Calculus", "Geometry", "Chemistry"]

    section_students = {"sec-A": ["Ganesh", "Arjun", "Dhavan", "Naveen", "Rakshith"],
                        "sec-B": ["Kislaya", "Chethan", "Girish", "Sujith", "Dheeraj"],
                        "sec-C": ["Manjunath", "Vikas", "Arun", "Zaid", "Shoaib"],
                        "sec-D": ["Govind", "Rahul", "Devu", "Milan", "Deepak"],
                        "sec-E": ["Heena", "Srinidhi", "Sameer", "Kalavathi", "Raghavendra"],
                    }

    student_data = {}

    # Assigning marks to each student
    for section in sections:
        for student in section_students[section]:
            marks = {}
            for course in courses:
                marks[course] = randint(35, 100)
            student_data[student] = {
                'name': student,
                'section': section,
                'course_marks': marks
               ,'total': sum(marks.values())
            }

    # Print all students details
    for section in sections:
        print("\n\nStudents of {}:".format(section))
        student_details(section_students[section], student_data)

    all_toppers = {}
    # Top three students per section
    print("\n\nTop three scorers in Each section are as follows:")
    for section in sections:
        toppers = top_three(section_students[section], student_data)
        print("\n\nToppers of section ", section)
        for score in sorted(toppers.values())[-1::-1]:
            for topper in toppers:
                if toppers[topper] == score:
                    print("Name: {}, Total: {}".format(topper, student_data[topper]['total']))

                    # Detailed information
                    # pprint(student_data[topper])
                    # print("\n")

                    # Basic Information
                    # print("Name: {}, Total: {}".format(topper, student_data[topper]['total']))

                    all_toppers[topper] = student_data[topper]

    # Top three throughout the class
    print("\n\nTop three scorers throughout the class:")
    toppers = top_three(all_toppers.keys(), all_toppers)
    for score in sorted(toppers.values())[-1::-1]:
        for topper in toppers:
            if toppers[topper] == score:
                # Detailed information
                # pprint(student_data[topper])
                # print("\n")

                # Basic information
                print("Name: {}, Total: {}".format(topper, all_toppers[topper]['total']))

    # print("ALl toppers: ", all_toppers.keys())
    # pprint(student_data)

    return


# Returns list of top three among students
def top_three(students, student_data):
    toppers = {}
    for student in students:
        # total = sum(student_data[student]['course_marks'].values())
        total = student_data[student]['total']
        if len(toppers) < 3:
            toppers[student] = total
        else:
            min_marks = min(toppers.values())
            if total > min_marks:
                for topper in toppers:
                    if toppers[topper] == min_marks:
                        del toppers[topper]
                        break
                toppers[student] = total

    return toppers


# Display student data by sections
def student_details(students, student_data):
    for student in students:
        pprint(student_data[student])

    return

main()



#
# class Section:
#
#
# class Student:
#
#     def __init__(self, name, sec, course_marks):
#         self.name = name
#         self.section = sec
#         self.course_marks = course_marks
#
#     def displayDetails(self):
#         print("Name: {}\tSection: {}".format(self.name, self.section))
#         print("\nCourse: Marks")
#         for course in self.course_marks.keys():
#             print("{}: {}".format(course, self.course_marks[course]))
#
#
# if __name__ == '__main__':
#
#     #Student data Entry
#     student1 = Student('Arjun', 'A', {'Algebra':80, 'Geometry':67, 'Calculus':70, 'Physics':86, 'Chemistry':64})
#     student2 = Student('Ganesh', 'A', {'Algebra':78, 'Geometry':85, 'Calculus':71, 'Physics':68, 'Chemistry':73})
#     student3 = Student('Dhavan', 'A', {'Algebra':68, 'Geometry':75, 'Calculus':90, 'Physics':84, 'Chemistry':78})
#     student4 = Student('Naveen', 'A', {'Algebra':71, 'Geometry':67, 'Calculus':89, 'Physics':95, 'Chemistry':66})
#     student5 = Student('Rakshith', 'A', {'Algebra':77, 'Geometry':62, 'Calculus':75, 'Physics':67, 'Chemistry':76})
#
#     student2.displayDetails()
#     # student = Student('', '', {'Algebra':, 'Geometry':, 'Calculus':, 'Physics':, 'Chemistry':})
#     student6 = Student('Arju', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
#     student7 = Student('Ganes', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
#     student8 = Student('Dhava', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
#     student9 = Student('Navee', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
#     student10 = Student('Rakshit', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})
#
#     student11 = Student('Arj', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
#     student12 = Student('Gane', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
#     student13 = Student('Dhav', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
#     student14 = Student('Nave', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
#     student15 = Student('Rakshi', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})
#
#     student16 = Student('rjun', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
#     student17 = Student('anesh', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
#     student18 = Student('havan', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
#     student19 = Student('aveen', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
#     student20 = Student('akshith', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})
#
#     student21 = Student('jun', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
#     student22 = Student('nesh', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
#     student23 = Student('avan', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
#     student24 = Student('veen', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
#     student25 = Student('kshith', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})
