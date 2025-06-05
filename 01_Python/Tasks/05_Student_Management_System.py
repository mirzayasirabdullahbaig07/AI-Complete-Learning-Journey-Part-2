# Define a class to represent a student
class Student:
    def __init__(self, name, student_id):
        # Initialize student name, ID, and an empty dictionary to store courses and grades
        self.name = name
        self.student_id = student_id
        self.courses = {}  # Example: {"Math": 85, "Science": 90}

    # Method to add or update a course and its grade
    def add_course(self, course_name, grade):
        if course_name in self.courses:
            print(f"{self.name} is already enrolled in {course_name}. Updating grade.")
        # Add or update the course grade
        self.courses[course_name] = grade

    # Method to calculate the average grade across all courses
    def calculate_average(self):
        if not self.courses:
            return 0  # Return 0 if no courses are added
        return sum(self.courses.values()) / len(self.courses)

    # Method to display all student details
    def get_details(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            print(f" - {course}: {grade}")
        print(f"Average Grade: {self.calculate_average():.2f}")

# ----------------------------
# Testing the Student class
# ----------------------------

# Create a student object
student1 = Student("Ali", "Yasir")

# Add some courses and their grades
student1.add_course("Math", 75)
student1.add_course("Science", 60)
student1.add_course("English", 97)

# Display the student's full details
student1.get_details()
