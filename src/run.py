from Models.data_structs import ArrayArray as array

from Models.RPS_CFR import Trainer
from Models.KUHNS_CFR import KuhnsPokerCFR

# trainer = Trainer()
#
# ## Set fixed strategy
# #trainer.set_fixed_strategy_to_p2([0.8, 0.1, 0.1], 2)
#
# ## Get solution
# trainer.play(10000)
#
# kuhns = KuhnsPokerCFR()
# ## Kuhns Poker solution
# kuhns.run(10000)

special_array = array(3)
special_array.set_val(0, 2.0)
special_array.set_val(1, 3.0)
special_array.set_val(2, 4.0)

special_array.mul(3.0)
print(special_array.list)

special_array2 = array(3)
special_array2.set_val(0, 2.0)
special_array2.set_val(1, 3.0)
special_array2.set_val(2, 4.0)

special_array.mul(special_array2)
print(special_array.list)