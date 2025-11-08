def wpl_to_txt(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    waypoints = []
    for line in lines:
        line = line.strip()
        if line.startswith("[Point"):
            waypoint = {}
            waypoint['Latitude'] = line.split('=')[1]
            waypoint['Longitude'] = lines[lines.index(line) + 1].split('=')[1]
            waypoint['Radius'] = lines[lines.index(line) + 2].split('=')[1]
            waypoint['Altitude'] = lines[lines.index(line) + 3].split('=')[1]
            waypoint['ClimbRate'] = lines[lines.index(line) + 4].split('=')[1]
            waypoint['DelayTime'] = lines[lines.index(line) + 5].split('=')[1]
            waypoint['WP_Event_Channel_Value'] = lines[lines.index(line) + 6].split('=')[1]
            waypoint['Heading'] = lines[lines.index(line) + 7].split('=')[1]
            waypoint['Speed'] = lines[lines.index(line) + 8].split('=')[1]
            waypoint['CAM-Nick'] = lines[lines.index(line) + 9].split('=')[1]
            waypoint['Type'] = lines[lines.index(line) + 10].split('=')[1]
            waypoint['Prefix'] = lines[lines.index(line) + 11].split('=')[1]
            waypoint['AutoTrigger'] = lines[lines.index(line) + 12].split('=')[1]
            waypoints.append(waypoint)

    with open(output_file, 'w') as f:
        for i, waypoint in enumerate(waypoints, start=1):
            f.write(f"Waypoint {i}:\n")
            f.write(f"Latitude: {waypoint['Latitude']}\n")
            f.write(f"Longitude: {waypoint['Longitude']}\n")
            f.write(f"Radius: {waypoint['Radius']}\n")
            f.write(f"Altitude: {waypoint['Altitude']}\n")
            f.write(f"ClimbRate: {waypoint['ClimbRate']}\n")
            f.write(f"DelayTime: {waypoint['DelayTime']}\n")
            f.write(f"WP_Event_Channel_Value: {waypoint['WP_Event_Channel_Value']}\n")
            f.write(f"Heading: {waypoint['Heading']}\n")
            f.write(f"Speed: {waypoint['Speed']}\n")
            f.write(f"CAM-Nick: {waypoint['CAM-Nick']}\n")
            f.write(f"Type: {waypoint['Type']}\n")
            f.write(f"Prefix: {waypoint['Prefix']}\n")
            f.write(f"AutoTrigger: {waypoint['AutoTrigger']}\n")
            f.write("\n")

    print(f"Conversion complete. Result saved to {output_file}")

# Usage example
input_file = 'bark_beetle.wpl'
output_file = 'bark_beetle.txt'
wpl_to_txt(input_file, output_file)