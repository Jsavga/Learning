# Slicing

players = ['charles', 'martina', 'michael', 'florence', 'ellie']
print(players)
print(players[0:3])  # gets items from pos 0 to pos 3-1
print(players[1:4])  # gets items from pos 1 to pos 4-1
print(players[:4])  # gets items from pos 0 to pos 4-1
print(players[2:])  # gets items from pos 2 to end pos
print(players[-1:])  # gets last item
print(players[-3:-1])  # gets items from  3 pos from end to end pos

print("Here are the first three players:")
for player in players[:3]:
    print(player.title())
