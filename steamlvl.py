# Written using Python 3.6.3

from sys import exit
from math import ceil
from time import sleep

# Basic information printed every time
print(">>>Enter the following information to calculate cost of desired Steam level",
	"\n>>>Calculations are based on XP\n>>>To force exit press CTRL + C\n")

# Formatting
hyp_count = 29		# Number of hyphens printed
right_align = 21	# Right aligning input() message
secs = 5			# Sleep for this many seconds

try: # User input inside of try for exception handling
	print("-" * hyp_count)
	print("{:>{}}".format("INPUT", right_align + 5))
	current_xp = int(input("{:>{}}".format("Current XP: ", right_align)))
	# The following flow control statements are well explained by their corresponding ERROR messages
	if current_xp < 0:
		print("-" * hyp_count)
		print("\n>>>ERROR: minimum value is 0")
		sleep(secs), exit()

	desired_level_xp = int(input("{:>{}}".format("Desired XP: ", right_align)))
	if desired_level_xp == current_xp:
		print("-" * hyp_count)
		print("\n>>>ERROR: identical Current XP and Desired XP")
		sleep(secs), exit()
	elif desired_level_xp < current_xp:
		print("-" * hyp_count)
		print("\n>>>ERROR: higher Current XP than Desired XP")
		sleep(secs), exit()
	elif desired_level_xp < 100:
		print("-" * hyp_count)
		print("\n>>>ERROR: minimum value is 100")
		sleep(secs), exit()

	card_cost = round(float(input("{:>{}}".format("Cost of one card: ", right_align))), 2)
	if card_cost <= 0:
		print("-" * hyp_count)
		print("\n>>>ERROR: positive value required")
		sleep(secs), exit()

	num_of_cards = int(input("{:>{}}".format("Cards in badge: ", right_align)))
	if num_of_cards < 5:
		print("-" * hyp_count)
		print("\n>>>ERROR: minimum value is 5")
		sleep(secs), exit()
	elif 15 < num_of_cards:
		print("-" * hyp_count)
		print("\n>>>ERROR: maximum value is 15")
		sleep(secs), exit()

except ValueError:
	print("-" * hyp_count)
	print("\n>>>ERROR: enter a whole number")
	sleep(secs), exit()
except KeyboardInterrupt:
	print()	# Needed for newline character, without this the hyphens are printed in the input() line
	print("-" * hyp_count)
	print("\n>>>Force exited")
	exit() # No sleep() here on purpose -- CTRL + C should have an instant effect

def roundup(xp):						# Round up by 100 because one badge equals 100 XP
	return int(ceil(xp / 100.0)) * 100 	# Example: you have 25 XP and want to reach level 1 (100 XP),
										#          you therefore need one badge. Since getting a fraction of
										#          a badge is not possible, you need the whole badge.
										# Not taking this into account would result in an incorrect
										# amount of badges needed (i.e. n-1).

def main(): # All of the calculations take place inside of main() so that it's easier to see what's going on
	xp_needed = (desired_level_xp - current_xp)
	num_of_badges_needed = (roundup(xp_needed) / 100)
	badge_cost = float(card_cost * num_of_cards)
	desired_level_cost = float(badge_cost * num_of_badges_needed)

	print("\n{:>{}}".format("OUTPUT", right_align + 6))
	if str(desired_level_cost).endswith("0"): # If a whole number, print it in int format (i.e. print 5 not 5.0)
		print("{:>{}}{:,}".format("Cost: ", right_align, int(desired_level_cost)))
	else:
		print("{:>{}}{:,.2f}".format("Cost: ", right_align, desired_level_cost))
	print("{:>{}}{:,}".format("Badges needed: ", right_align, int(num_of_badges_needed)))
	print("-" * hyp_count)
	sleep(secs)

if __name__ == "__main__":
	main()
