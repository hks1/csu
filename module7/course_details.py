'''
course_rooms: dictionary mapping course codes to room numbers
'''
course_rooms = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}
    

'''
course_instructors: dictionary mapping course codes to instructors
'''
course_instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

'''
course_times: dictionary mapping course codes to times
'''
course_times = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

''''
Method to display the course's room number, instructor, and meeting time for a given course number
'''
def display_course_info(course_code):
    print(f"Room number: {course_rooms[course_code]}")
    print(f"Instructor: {course_instructors[course_code]}")
    print(f"Meeting time: {course_times[course_code]}")

'''
Main function to prompt the user for a course code and display the course's room number, instructor, and meeting time
'''
def main():
    course_code = input("Enter a course code: ")
    display_course_info(course_code)

# calling main function
if __name__ == '__main__':
    main()