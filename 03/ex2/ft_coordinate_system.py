import math

def get_player_pos():
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        
        parts = user_input.split(',')

        
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            # Find which parameter failed
            for p in parts:
                try:
                    float(p.strip())
                except ValueError as err:
                    print(f"Error on parameter '{p.strip()}': {err}")
                    break


print("=== Game Coordinate System ===")


print("Get a first set of coordinates")
pos1 = get_player_pos()

print("Got a first tuple:", pos1)
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")


dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print(f"Distance to center: {dist_center:.4f}")


print("Get a second set of coordinates")
pos2 = get_player_pos()


dist_points = math.sqrt(
    (pos2[0] - pos1[0])**2 +
    (pos2[1] - pos1[1])**2 +
    (pos2[2] - pos1[2])**2
)

print(f"Distance between the 2 sets of coordinates: {dist_points:.4f}")
