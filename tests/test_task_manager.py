import unittest
import task_manager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        task_manager.tasks.clear()

    def test_add_task(self):
        result = task_manager.add_task("Complete assignment")

        self.assertTrue(result)
        self.assertEqual(len(task_manager.tasks), 1)
        self.assertEqual(
            task_manager.tasks[0]["title"],
            "Complete assignment"
        )

    def test_add_empty_task(self):
        result = task_manager.add_task("   ")

        self.assertFalse(result)
        self.assertEqual(len(task_manager.tasks), 0)

    def test_complete_task(self):
        task_manager.add_task("Study Git")

        result = task_manager.complete_task(1)

        self.assertTrue(result)
        self.assertTrue(task_manager.tasks[0]["completed"])

    def test_delete_task(self):
        task_manager.add_task("Submit project")

        result = task_manager.delete_task(1)

        self.assertTrue(result)
        self.assertEqual(len(task_manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()