import pytest
import System
import Professor
import Staff
import User
import TA
import RestoreData
import Student

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'


#pass
def test_login(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.__init__()
    if users[username]['role'] != 'professor':
        assert False


#pass
def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False

#fail, changes the grade to a zero
def test_change_grade(grading_system):
    grade = 90
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    student = Student.Student(username2, users, courses)
    professor.change_grade(username2,course,assignment,grade)
    
    for key in users:
        if users[username2]['courses'][course][assignment]['grade'] != grade:
            assert False
    

#pass
def test_create_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    professor.create_assignment('assignment4', '04/09/20', 'cloud_computing')

    assignments = []
    for key in courses:
        assignments.append([key, courses[key]])

    if assignments[2][1]['assignments']['assignment4']:
        assert True
    else:
        assert False

#fail:
def test_add_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    professor.add_student('akend3', 'software_engineering')


#pass
def test_drop_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    professor.drop_student('hdjsr7', 'databases')

    if 'databases' in users['hdjsr7']['courses']:
        assert False
    else:
        assert True


#fail: submit assignment only checks for due dates in comp sci,
#so even though assignment3 exits in cloud computing, the function wont work
def test_submit_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username3, users, courses)
    student.submit_assignment(course,'assignment3', 'test', '2/25/20')

    for key in users:
        if users[username3]['courses'][course]['assignment3']['submission_date'] == '2/25/20':
            assert True
        else:
            assert False

#fail: the function returns true every time
def test_check_ontime(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username, users, courses)
    test = None
    test = student.check_ontime('4/18/20','4/10/20')
    if test == True:
        assert False
    

#pass
def test_check_grades(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username3, users, courses)
    grades = student.check_grades(course)

    if grades[0][1] == 3:
        assert True
    else:
        assert False


#fail: only views the assignments in comp_sci
def test_view_assignments(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username2, users, courses)
    assignments = student.view_assignments(course)

    if assignments [0][1] == 'assignment2':
        assert True
    else:
        assert False


#previously required check grades test was for student, this checks the
#professor's check grades function
def test_staff_check_grades(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    grades = professor.check_grades('goggins', 'software_engineering')

#test to add a new student, not in the json database into a class
def test_add_new_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    professor = Professor.Professor(profUser, users, courses)
    professor.add_student('nccdn6', 'software_engineering')


#if a student submits an assignemnt that doesn't exist
#there should be error handling in place to prevent a fatal error
def test_submit_nonexistant_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username3, users, courses)
    student.submit_assignment('comp_sci','gobbeldygook', 'earnest_work', '3/3/20')

#if a student submits to a class that doesn't exist
#the database shouldn't accept it, and handle the error
def test_submit_to_nonexistant_class(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username3, users, courses)
    student.submit_assignment('nonsense','assignment1', 'earnest_work', '2/29/20')
    assignments = student.view_assignments('comp_sci')

    if 'nonsense' not in assignments:
        assert True
    else:
        assert False    


#the database shouldnt accept assignments submitted with garbage dates, such as in the past
#future, or a nonexistant date (such as 2/31/20)
def test_submit_on_a_nonexestant_date(grading_system):    
    users = grading_system.users
    courses = grading_system.courses
    student = Student.Student(username3, users, courses)
    student.submit_assignment('comp_sci','assignment1', 'earnest_work', '2/31/20')
    assignments = student.view_assignments('comp_sci')

    if 'assignment1' not in assignments:
        assert True
    else:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem




