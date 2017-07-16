# Created by Dhavan Shekarappa on 07/15/2017

from random import randint
from pprint import pprint


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
                        "sec-E": ["Heena", "Srinidhi", "Sameer", "Kalavathi", "Raghavendra"],
                    }

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
    all_toppers = {}
    print("\n\nTop three scorers in Each section are as follows:")
    for section in sections:
        toppers = top_three(section_students[section], student_data)
        print("\n\nToppers of section ", section)
        for score in sorted(toppers.values())[-1::-1]:
            for topper in toppers:
                if toppers[topper] == score:
                    print("Name: {}, Percentage: {}".format(topper, student_data[topper]['total']/len(courses)))
                    # Detailed information
                    # pprint(student_data[topper])
                    # print("\n")
                    all_toppers[topper] = student_data[topper]

    # Determine top three students throughout the class
    print("\n\nTop three scorers throughout the class:")
    toppers = top_three(all_toppers.keys(), all_toppers)
    for score in sorted(toppers.values())[-1::-1]:
        for topper in toppers:
            if toppers[topper] == score:
                print("Name: {}, Percentage: {}".format(topper, all_toppers[topper]['total'] / len(courses)))
                # Detailed information
                # pprint(student_data[topper])
                # print("\n")

    # print("ALl toppers: ", all_toppers.keys())
    # pprint(student_data)

    return

main()
