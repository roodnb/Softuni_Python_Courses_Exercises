from project.soccer_player import SoccerPlayer

from unittest import TestCase, main


class TestSoccerPlayer(TestCase):

    def setUp(self):
        self.s = SoccerPlayer("Jordan", 40, 10, "Barcelona")

    def test_init(self):
        self.assertEqual(self.s.name, "Jordan")
        self.assertEqual(self.s.age, 40)
        self.assertEqual(self.s.goals, 10)
        self.assertEqual(self.s.team, "Barcelona")
        self.assertEqual(self.s.achievements, {})

    def test_instance_attribute_type(self):
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.age, int)
        self.assertIsInstance(self.s.goals, int)
        self.assertIsInstance(self.s.team, str)
        self.assertIsInstance(self.s.achievements, dict)

    def test_name_len_below_or_five_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = "Bass"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.s.name = "Basss"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_age_below_16_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.age = 15
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_goals_below_zero(self):
        self.s.goals = -1
        self.assertEqual(self.s.goals, 0)

    def test_team_not_valid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.team = "dnb"
        self.assertEqual(str(ex.exception), f"Team must be one of the following:"
                                            f" {', '.join(SoccerPlayer._VALID_TEAMS)}!")

    def test_change_team_new_team_not_valid(self):
        self.assertEqual(self.s.team, "Barcelona")
        result = self.s.change_team("dnb")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.s.team, "Barcelona")

    def test_change_team_new_team_is_valid(self):
        self.assertEqual(self.s.team, "Barcelona")
        result = self.s.change_team("Real Madrid")
        self.assertEqual(self.s.team, "Real Madrid")
        self.assertEqual(result, "Team successfully changed!")

    def test_add_new_achievements(self):
        self.assertEqual(self.s.achievements, {})
        result = self.s.add_new_achievement("champion's league")
        self.assertEqual(self.s.achievements, {"champion's league": 1})
        self.assertEqual(result, f"champion's league has been successfully "
                                 f"added to the achievements collection!")

        result2 = self.s.add_new_achievement("champion's league")
        self.assertEqual(self.s.achievements, {"champion's league": 2})
        self.assertEqual(result2, f"champion's league has been successfully "
                                 f"added to the achievements collection!")

        result3 = self.s.add_new_achievement("World Cup")
        self.assertEqual(self.s.achievements, {"World Cup": 1, "champion's league": 2})
        self.assertEqual(result3, f"World Cup has been successfully "
                                 f"added to the achievements collection!")

    def test_lt_(self):
        other = SoccerPlayer("another", 40, 20, "Barcelona")
        result = self.s.__lt__(other)
        self.assertEqual(result, f"{other.name} is a top goal scorer! S/he scored more than {self.s.name}.")

        other.goals = 10
        result2 = self.s.__lt__(other)
        self.assertEqual(result2, f"{self.s.name} is a better goal scorer than {other.name}.")


if __name__ == "__main__":
    main()