#!/usr/bin/env python2

# calcRisk.py
# calculating the winning ratio for different scenarios
# for the game "Risk"
# bd03 -- 2018-05-03

import random
import time

def rollDice(numDice):
  dice=[]
  for i in range(numDice):
    dice.append(random.randint(1,6))
  dice=sorted(dice)
  return dice[::-1]

def fight(attackers, defenders):
  aDice = 3 if attackers > 3 else attackers - 1
  dDice = 3 if defenders > 2 else defenders
  attack = rollDice(aDice)
  defence = rollDice(dDice)
  while attack and defence:
    if attack[0] > defence[0]:
      defenders = defenders - 1
    else:
      attackers = attackers - 1
    del attack[0]
    del defence[0]
  if attackers == 1:
    return False
  elif defenders == 0:
    return True
  elif attackers <= 0 or defenders < 0:
    assert("Something went wrong!")
  else:
    return fight(attackers, defenders)

def main():
  # parameters
  numTrials = 1000000
  attackForce = (2, 3, 4, 5, 6, 7, 8, 9, 10)
  defenceForce = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  filename = "output.csv"
  f=open(filename, "w")
  f.write("numTrials: "+str(numTrials)+"\n")
  f.write("AttackForces: "+str(attackForce)+"\n")
  f.write("DefenceForces: "+str(defenceForce)+"\n")
  for aa in attackForce:
    print "AttackForce: "+str(aa)
    line=""
    for dd in defenceForce:
      print "--DefenceForce: "+str(dd)
      aWon = 0
      for tt in range(0,numTrials):
        attackWon = fight(aa,dd)
        if attackWon:
          aWon = aWon + 1
      winRate = aWon * 1.0 / numTrials
      line=line+str(winRate)+","
    f.write(line+"\n")
  f.close()

if __name__ == "__main__":
  main()