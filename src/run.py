

from Models.RPS_CFR import Trainer
from Models.KUHNS_CFR import KuhnsPokerCFR

trainer = Trainer()

## Get solution
trainer.play(10000)


kuhns = KuhnsPokerCFR()
## Kuhns Poker solution
kuhns.run(10000)
