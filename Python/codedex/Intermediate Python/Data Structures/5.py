players = [
    {
    'name': "Patrick Mahomes",
    'position': "Quarterback",
    'jersey_number': 44,
    'yards_gained': 150, 
    'touchdowns': 2
    }, 
    {
    'name': 'Tyreek Hill', 
    'position': 'Wide Receiver', 
    'jersey_number': 10,
    'yards_gained': 120, 
    'touchdowns': 1
    }, 
    {
    'name': 'Travis Kelce', 
    'position': 'Tight End', 
    'jersey_number': 22,
    'yards_gained': 160, 
    'touchdowns': 4
    }]

names = []
positions = []
total_yards_gained = 0
total_touchdowns = 0

players[2]['yards_gained'] += 20
players[2]['touchdowns'] += 1

for i in players:
    names.append(i['name'])
    positions.append(i['position'])
    
    total_yards_gained += i['yards_gained']
    total_touchdowns += i['touchdowns']

print(names)
print(positions)


avg_yards_gained = total_yards_gained/len(players)
avg_touchdowns = total_touchdowns/len(players)

print(avg_yards_gained)
print(avg_touchdowns)