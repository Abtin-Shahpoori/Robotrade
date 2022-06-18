import sys
import random
sys.path.append("../..")
from bot_template import Bot


a = Bot("TEST")
a.algo = random.randint
print(a.test())
