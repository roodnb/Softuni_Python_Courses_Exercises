from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.muse_elf import MuseElf
from project.dark_wizard import DarkWizard
from project.dark_knight import DarkKnight
from project.soul_master import SoulMaster









hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
