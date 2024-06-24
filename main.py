import mysql.connector
from mysql.connector import Error
import uuid
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connection settings
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

def create_connection():
    """Create a database connection"""
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    """Execute a single query"""
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data():
    connection = create_connection()

    if connection is None:
        return

    # Inserting data into Students table
    students_query = """
    INSERT INTO Students (StudentID, FirstName, LastName, Email, Phone, CourseID, EducationalDegree, Speciality, Active) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    students_data = [
        (str(uuid.uuid4()), 'John', 'Doe', 'john.doe@example.com', '1234567890', None, 'Bachelor', 'Computer Science', True),
        (str(uuid.uuid4()), 'Jane', 'Smith', 'jane.smith@example.com', '0987654321', None, 'Master', 'Mathematics', True)
    ]
    for data in students_data:
        execute_query(connection, students_query, data)

    # Inserting data into Instructors table
    instructors_query = """
    INSERT INTO Instructors (InstructorID, FirstName, LastName, Email, Phone, Active) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    instructors_data = [
        (str(uuid.uuid4()), 'Alice', 'Johnson', 'alice.johnson@example.com', '1122334455', True),
        (str(uuid.uuid4()), 'Bob', 'Williams', 'bob.williams@example.com', '5544332211', True)
    ]
    for data in instructors_data:
        execute_query(connection, instructors_query, data)

    # Inserting data into Courses table
    courses_query = """
    INSERT INTO Courses (CourseID, CourseDisplayShortName, CourseDisplayFullName, CourseDescription, LecturesNum, PracticesNum) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    courses_data = [
        (str(uuid.uuid4()), 'CS101', 'Introduction to Computer Science', 'Basic concepts of computer science', 30, 15),
        (str(uuid.uuid4()), 'MATH201', 'Advanced Mathematics', 'In-depth study of advanced mathematical concepts', 25, 10)
    ]
    for data in courses_data:
        execute_query(connection, courses_query, data)

    # Inserting data into Rooms table
    rooms_query = """
    INSERT INTO Rooms (RoomID, Building, Floor, Number, DisplayName, SeatsNumber) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    rooms_data = [
        (str(uuid.uuid4()), 'Building A', 1, 101, 'Room 101', 30),
        (str(uuid.uuid4()), 'Building B', 2, 202, 'Room 202', 50)
    ]
    for data in rooms_data:
        execute_query(connection, rooms_query, data)

    # Inserting data into LessonsSchedule table
    lessons_schedule_query = """
    INSERT INTO LessonsSchedule (LessonScheduleID, StartTime, EndTime) 
    VALUES (%s, %s, %s)
    """
    lessons_schedule_data = [
        (1, '08:00:00', '09:00:00'),
        (2, '09:00:00', '10:00:00')
    ]
    for data in lessons_schedule_data:
        execute_query(connection, lessons_schedule_query, data)

    # Inserting data into StudentsCourseGroups table
    students_course_groups_query = """
    INSERT INTO StudentsCourseGroups (StudentsCourseGroupID, CourseID) 
    VALUES (%s, %s)
    """
    students_course_groups_data = [
        (str(uuid.uuid4()), courses_data[0][0]),
        (str(uuid.uuid4()), courses_data[1][0])
    ]
    for data in students_course_groups_data:
        execute_query(connection, students_course_groups_query, data)

    # Inserting data into Schedule table
    schedule_query = """
    INSERT INTO Schedule (ScheduleID, CourseID, InstructorID, StudentsCourseGroupID, WeekDay, LessonScheduleID, RoomID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    schedule_data = [
        (str(uuid.uuid4()), courses_data[0][0], instructors_data[0][0], students_course_groups_data[0][0], 'Monday', 1, rooms_data[0][0]),
        (str(uuid.uuid4()), courses_data[1][0], instructors_data[1][0], students_course_groups_data[1][0], 'Tuesday', 2, rooms_data[1][0])
    ]
    for data in schedule_data:
        execute_query(connection, schedule_query, data)

    # Inserting data into InstructorsCourses table
    instructors_courses_query = """
    INSERT INTO InstructorsCourses (InstructorCourseID, InstructorID, CourseID) 
    VALUES (%s, %s, %s)
    """
    instructors_courses_data = [
        (str(uuid.uuid4()), instructors_data[0][0], courses_data[0][0]),
        (str(uuid.uuid4()), instructors_data[1][0], courses_data[1][0])
    ]
    for data in instructors_courses_data:
        execute_query(connection, instructors_courses_query, data)

    # Inserting data into StudentsCourseGroupStudents table
    students_course_group_students_query = """
    INSERT INTO StudentsCourseGroupStudents (StudentsCourseGroupStudentID, StudentID, StudentsCourseGroupID) 
    VALUES (%s, %s, %s)
    """
    students_course_group_students_data = [
        (str(uuid.uuid4()), students_data[0][0], students_course_groups_data[0][0]),
        (str(uuid.uuid4()), students_data[1][0], students_course_groups_data[1][0])
    ]
    for data in students_course_group_students_data:
        execute_query(connection, students_course_group_students_query, data)

    connection.close()

if __name__ == "__main__":
    insert_data()
