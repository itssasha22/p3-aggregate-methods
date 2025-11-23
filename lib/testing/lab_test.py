from lib.enrollment import Student, Course, Enrollment

def test_aggregate_methods():
    # Create students and courses
    alice = Student("Alice")
    bob = Student("Bob")

    math = Course("Math")
    science = Course("Science")

    # Enroll students in courses
    alice.enroll(math)
    alice.enroll(science)
    bob.enroll(math)

    # Set grades for Alice
    for enrollment in alice.get_enrollments():
        alice.set_grade(enrollment, 90)

    # Set grades for Bob
    for enrollment in bob.get_enrollments():
        bob.set_grade(enrollment, 80)

    # Test course_count
    assert alice.course_count() == 2
    assert bob.course_count() == 1

    # Test aggregate_average_grade
    assert alice.aggregate_average_grade() == 90
    assert bob.aggregate_average_grade() == 80

    # Test aggregate_enrollments_per_day
    enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
    assert isinstance(enrollments_per_day, dict)
    total_enrollments = sum(enrollments_per_day.values())
    assert total_enrollments == 3

    print("All aggregate method tests passed.")

if __name__ == "__main__":
    test_aggregate_methods()
