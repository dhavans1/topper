# Created by Dhavan Shekarappa on 07/15/2017

from random import randint
from pprint import pprint


# Returns list of top three among students
def top_three(students, student_data, courses = []):
    if courses:
        # marks = []
        course_top_marks = {}
        for course in courses:
            course_top_marks[course] = 0

        for course in courses:
            for student in students:
                if course_top_marks[course] < student_data[student]['course_marks'][course]:
                    course_top_marks[course] = student_data[student]['course_marks'][course]
        # print("course_top_marks", course_top_marks)
        # print("asdas",sorted(list(course_top_marks.values()))[-1:-4:-1])
        return sorted(list(course_top_marks.values()))[-1::-1]


# Display student data by sections
def student_details(students, student_data):
    for student in students:
        pprint(student_data[student])

    return


def main():

    # Initialize data
    # Sections in the Department
    sections = ["sec-A", "sec-B", "sec-C", "sec-D", "sec-E"]

    # Courses offered in the Department
    courses = ["Physics", "Algebra", "Calculus", "Geometry", "Chemistry"]

    # Students belonging to each section
    section_students = {"sec-A": ["Ganesh", "Arjun", "Dhavan", "Naveen", "Rakshith"],
                        "sec-B": ["Kislaya", "Chethan", "Girish", "Sujith", "Dheeraj"],
                        "sec-C": ["Manjunath", "Vikas", "Arun", "Zaid", "Shoaib"],
                        "sec-D": ["Govind", "Rahul", "Devu", "Milan", "Deepak"],
                        "sec-E": ["Heena", "Srinidhi", "Sameer", "Kalavathi", "Raghavendra"]}

    # Structured student data
    student_data = {}
    # Assign marks to each student
    for section in sections:
        for student in section_students[section]:
            marks = {}
            for course in courses:
                # Assigning random marks between 35 and 100
                marks[course] = randint(35, 100)
            student_data[student] = {
                'name': student,
                'section': section,
                'course_marks': marks
               ,'total': sum(marks.values())
            }

    # Output student details
    for section in sections:
        print("\n\nStudents of {}:".format(section))
        student_details(section_students[section], student_data)

    # Determine top three students in each section
    # all_toppers = {}
    all_top_names = {}
    print("\n\nTop three scorers in Each section are as follows:")
    for section in sections:
        top_marks = top_three(section_students[section], student_data, courses)
        print("top_marks: {}".format(top_marks))
        print("\n\nToppers of section ", section)

        top_names = {}
        course_included = []
        count = 0
        for student in section_students[section]:
            for course, course_marks in student_data[student]['course_marks'].items():
                if course_marks in top_marks and course not in course_included and count < 3:
                    # print("Name: {}, Course: {}, Marks: {}".format(student, course, course_marks))
                    top_names[str(student) + ':' + str(course)] = course_marks
                    top_marks.remove(course_marks)
                    course_included.append(course)
                    count += 1
        # print("top_names:\n",top_names)
        # print(top_names)
        all_top_names.update(top_names)
        for marks in sorted(list(top_names.values()))[-1::-1]:
            for top_name, top_marks in top_names.items():
                if top_marks == marks:
                    print("Name: {}, Course: {}, Marks: {}".format(str(top_name).split(':')[0], str(top_name).split(':')[1], top_marks))
        #             del top_names[top_name]
        #             break

    # Determine top three students in each section
    print("Whole section:\n")
    for marks in sorted(list(all_top_names.values()))[-1:-4:-1]:
        for top_name, top_marks in all_top_names.items():
            if top_marks == marks:
                print("Name: {}, Course: {}, Marks: {}".format(str(top_name).split(':')[0], str(top_name).split(':')[1], top_marks))
                del all_top_names[top_name]
                break













        # print("all: ",all_top_marks)
                # if toppers[topper] == score:
                #     print("Name: {}, Percentage: {}".format(topper, student_data[topper]['total']/len(courses)))
                    # Detailed information
                    # pprint(student_data[topper])
                    # print("\n")
                    # all_toppers[topper] = student_data[topper]
                    #     all_top_marks[str(student)+':'+str(course)] = marks
        # print('All top marks\n{}'.format(all_top_marks))

    # # Determine top three students throughout the class
    # print("\n\nTop three scorers throughout the class:")
    # toppers = top_three(all_toppers.keys(), all_toppers)
    # for score in sorted(toppers.values())[-1::-1]:
    #     for topper in toppers:
    #         if toppers[topper] == score:
    #             print("Name: {}, Percentage: {}".format(topper, all_toppers[topper]['total'] / len(courses)))
    #             # Detailed information
    #             # pprint(student_data[topper])
    #             # print("\n")

    return

main()
