from project.hero import Hero

from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self):
        self.h = Hero("Jordan", 3, 5.5, 10.5)

    def test_init(self):
        self.assertEqual(self.h.username, "Jordan")
        self.assertEqual(self.h.level, 3)
        self.assertEqual(self.h.health, 5.5)
        self.assertEqual(self.h.damage, 10.5)

    def test_class_attribute_type(self):
        self.assertIsInstance(self.h.username, str)
        self.assertIsInstance(self.h.level, int)
        self.assertIsInstance(self.h.health, float)
        self.assertIsInstance(self.h.damage, float)

    def test_battle_enemy_hero_name_is_hero_name_raises(self):
        enemy_hero = Hero("Jordan", 3, 5.5, 10.5)
        with self.assertRaises(Exception) as ex:
            self.h.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_hero_health_zero_or_negative_raises(self):
        enemy_hero = Hero("Tsvetan", 3, 5.5, 10.5)

        self.h.health = 0
        with self.assertRaises(ValueError) as ex:
            self.h.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

        self.h.health = -5
        with self.assertRaises(ValueError) as ex2:
            self.h.battle(enemy_hero)
        self.assertEqual(str(ex2.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_hero_health_zero_or_negative_raises(self):
        enemy_hero = Hero("Tsvetan", 3, 0, 10.5)

        with self.assertRaises(ValueError) as ex:
            self.h.battle(enemy_hero)
        self.assertEqual(str(ex.exception), f"You cannot fight Tsvetan. He needs to rest")

        enemy_hero.health = -5
        with self.assertRaises(ValueError) as ex2:
            self.h.battle(enemy_hero)
        self.assertEqual(str(ex2.exception), f"You cannot fight Tsvetan. He needs to rest")

    def test_draw(self):
        enemy_hero = Hero("Tsvetan", 3, 5.5, 10.5)
        result = self.h.battle(enemy_hero)
        self.assertEqual(self.h.level, 3)
        self.assertEqual(self.h.health, -26)
        self.assertEqual(self.h.damage, 10.5)
        self.assertEqual(result, "Draw")

    def test_battle_hero_wins(self):
        enemy_hero = Hero("Tsvetan", 1, 1, 1)
        result = self.h.battle(enemy_hero)
        self.assertEqual(self.h.health, 9.5)
        self.assertEqual(self.h.level, 4)
        self.assertEqual(self.h.damage, 15.5)
        self.assertEqual("You win", result)

    def test_battle_hero_loses(self):
        enemy_hero = Hero("Tsvetan", 3, 51.5, 10.5)
        result = self.h.battle(enemy_hero)
        self.assertEqual(enemy_hero.health, 25.0)
        self.assertEqual(enemy_hero.level, 4)
        self.assertEqual(enemy_hero.damage, 15.5)
        self.assertEqual(result, "You lose")

    def test_str(self):
        expected_result = f"Hero Jordan: 3 lvl\n" \
               f"Health: 5.5\n" \
               f"Damage: 10.5\n"
        self.assertEqual(expected_result, str(self.h))


if __name__ == "__main__":
    main()
