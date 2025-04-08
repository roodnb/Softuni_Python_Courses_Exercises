from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.s = Student("Jordan")

    def test_init_courses_is_none(self):
        self.assertEqual(self.s.name, "Jordan")
        self.assertEqual(self.s.courses, {})

    def test_init_courses_is_not_none(self):
        self.s.courses = {"BEL": ['Notes', 'More Notes']}
        self.assertEqual(self.s.name, "Jordan")
        self.assertEqual(self.s.courses, {"BEL": ['Notes', 'More Notes']})

    def test_instance_attribute_type(self):
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.courses, dict)

    def test_enroll_course_name_in_courses_keys_returns(self):
        self.s.courses = {"BEL": ['Notes', 'More Notes']}
        self.assertEqual(self.s.courses, {"BEL": ['Notes', 'More Notes']})

        result = self.s.enroll("BEL", ["less notes", "pesho"])
        self.assertEqual(self.s.courses["BEL"], ['Notes', 'More Notes',"less notes", "pesho"])
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_add_course_notes_is_y_or_empty_returns(self):
        self.assertEqual(self.s.courses, {})
        result = self.s.enroll("BEL", ["less notes", "pesho"])
        self.assertEqual(self.s.courses, {"BEL": ["less notes", "pesho"]})
        self.assertEqual(result, "Course and course notes have been added.")

        self.s.courses = {}
        self.assertEqual(self.s.courses, {})
        result2 = self.s.enroll("BEL", ["less notes", "pesho"], 'Y')
        self.assertEqual(self.s.courses, {"BEL": ["less notes", "pesho"]})
        self.assertEqual(result2, "Course and course notes have been added.")

    def test_enroll(self):
        self.assertEqual(self.s.courses, {})
        result = self.s.enroll("BEL", ["less notes", "pesho"], 'N')
        self.assertEqual(self.s.courses["BEL"], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_course_name_in_courses_returns(self):
        self.assertEqual(self.s.courses, {})
        self.s.enroll("BEL", ["less notes", "pesho"], 'N')
        self.assertEqual(self.s.courses, {"BEL": []})
        result = self.s.add_notes("BEL", ("less notes", "pesho"))
        self.assertEqual(self.s.courses["BEL"], [("less notes", "pesho")])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_raises(self):
        self.assertEqual(self.s.courses, {})
        self.s.enroll("BEL", ["less notes", "pesho"], 'N')
        self.assertEqual(self.s.courses, {"BEL": []})
        with self.assertRaises(Exception) as ex:
            self.s.add_notes("Mathematics", ("less notes", "pesho"))
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.s.courses, {"BEL": []})

    def test_leave_course_course_name_in_courses_returns(self):
        self.s.courses = {"BEL": [], "Mathematics": [], "History": []}
        self.assertEqual(self.s.courses, {"BEL": [], "Mathematics": [], "History": []})
        result = self.s.leave_course("BEL")
        self.assertEqual(self.s.courses,{"Mathematics": [], "History": []})
        self.assertEqual(result, "Course has been removed")

    def test_leve_course_raises(self):
        self.s.courses = {"BEL": [], "Mathematics": [], "History": []}
        self.assertEqual(self.s.courses, {"BEL": [], "Mathematics": [], "History": []})
        with self.assertRaises(Exception) as ex:
            self.s.leave_course("Alabala")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")
        self.assertEqual(self.s.courses,{"BEL": [], "Mathematics": [], "History": []})



