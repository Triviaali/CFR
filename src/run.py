from Models.RPS_CFR import Trainer

trainer = Trainer()

## Set fixed strategy
#trainer.set_fixed_strategy_to_p2([0.8, 0.1, 0.1], 2)

## Get solution
trainer.play(10000)