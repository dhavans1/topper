# Created by Dhavan Shekarappa on 07/15/2017


class Student:

    def __init__(self, name, sec, course_marks):
        self.name = name
        self.section = sec
        self.course_marks = course_marks

    def displayDetails(self):
        print("Name: {}\tSection: {}".format(self.name, self.section))
        print("\nCourse: Marks")
        for course in self.course_marks.keys():
            print("{}: {}".format(course, self.course_marks[course]))


if __name__ == '__main__':

    #Student data Entry
    student1 = Student('Arjun', 'A', {'Algebra':80, 'Geometry':67, 'Calculus':70, 'Physics':86, 'Chemistry':64})
    student2 = Student('Ganesh', 'A', {'Algebra':78, 'Geometry':85, 'Calculus':71, 'Physics':68, 'Chemistry':73})
    student3 = Student('Dhavan', 'A', {'Algebra':68, 'Geometry':75, 'Calculus':90, 'Physics':84, 'Chemistry':78})
    student4 = Student('Naveen', 'A', {'Algebra':71, 'Geometry':67, 'Calculus':89, 'Physics':95, 'Chemistry':66})
    student5 = Student('Rakshith', 'A', {'Algebra':77, 'Geometry':62, 'Calculus':75, 'Physics':67, 'Chemistry':76})

    student2.displayDetails()
    # student = Student('', '', {'Algebra':, 'Geometry':, 'Calculus':, 'Physics':, 'Chemistry':})
    student6 = Student('Arju', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
    student7 = Student('Ganes', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
    student8 = Student('Dhava', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
    student9 = Student('Navee', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
    student10 = Student('Rakshit', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})

    student11 = Student('Arj', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
    student12 = Student('Gane', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
    student13 = Student('Dhav', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
    student14 = Student('Nave', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
    student15 = Student('Rakshi', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})

    student16 = Student('rjun', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
    student17 = Student('anesh', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
    student18 = Student('havan', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
    student19 = Student('aveen', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
    student20 = Student('akshith', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})

    student21 = Student('jun', 'A', {'Algebra': 80, 'Geometry': 67, 'Calculus': 70, 'Physics': 86, 'Chemistry': 64})
    student22 = Student('nesh', 'A', {'Algebra': 78, 'Geometry': 85, 'Calculus': 71, 'Physics': 68, 'Chemistry': 73})
    student23 = Student('avan', 'A', {'Algebra': 68, 'Geometry': 75, 'Calculus': 90, 'Physics': 84, 'Chemistry': 78})
    student24 = Student('veen', 'A', {'Algebra': 71, 'Geometry': 67, 'Calculus': 89, 'Physics': 95, 'Chemistry': 66})
    student25 = Student('kshith', 'A', {'Algebra': 77, 'Geometry': 62, 'Calculus': 75, 'Physics': 67, 'Chemistry': 76})

    