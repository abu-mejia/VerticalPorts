import pandas as pd

def parse_wpl_file(wpl_file_path):
    with open(wpl_file_path, 'r') as file:
        lines = file.readlines()

    data = []
    current_point = None
    for line in lines:
        line = line.strip()
        if line.startswith('[Point'):
            current_point = int(line[6:-1])
            data.append({})
        elif line.startswith(('Latitude=', 'Longitude=', 'Radius=', 'Altitude=', 'ClimbRate=',
                              'DelayTime=', 'WP_Event_Channel_Value=', 'Heading=', 'Speed=',
                              'CAM-Nick=', 'Type=', 'Prefix=', 'AutoTrigger=')):
            key, value = line.split('=')
            data[current_point - 1][key] = value

    return pd.DataFrame(data)

# Example usage
wpl_file_path = 'C:\geodata\ejff_thesis\data\barkBeetle.wpl'
df = parse_wpl_file(wpl_file_path)

output_file_path = 'waypoints.txt'
df.to_csv(output_file_path, index=False, sep='\t')

print(f"Waypoints exported to {output_file_path}")