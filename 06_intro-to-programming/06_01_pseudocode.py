# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.

# Gather all friends's names that have affinity for cats and like them, also are not allergic to them.
# Name every kitten and make sure they look clean and cute.
# Create an adoption message


# Gather all friends's names that have affinity for cats and like them, also are not allergic to them.
friends = ["Paolo", "Claudio", "Guayo", "Gabriela"]

# Name every kitten and make sure they look clean and cute.
kittens = ["bolt", "blacky", "zeus", "thunder"]

# Create an adoption message
message = "My cat just had beautiful, cute kittens, they are ready to give and receive love!!""\n"

for name in friends:
	print(message, "Their names are: ", kittens, "so", name, "you can pick them up at your availability")