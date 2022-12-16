
def extract_coordinates(input: list[str]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    coordinates = list()
    for line in input:
        sensor, beacon = line.split(": ")
        sensor = sensor[10:]
        beacon = beacon[21:]
        sensor = sensor.split(", ")
        beacon = beacon.split(", ")
        coordinates.append(((int(sensor[0][2:]), int(sensor[1][2:])), (int(beacon[0][2:]), int(beacon[1][2:]))))
    return coordinates

def solve15_p1(input: list[str]) -> None:
    coordinates = extract_coordinates(input)
    SCANLINE = 2000000
    scanned_positions = set()
    beacons_and_sensors = set()
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in coordinates:
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        distance_to_scanline = abs(SCANLINE - sensor_y)
        if distance_to_scanline > distance:
            continue
        scan_width = distance - distance_to_scanline
        scan_start = sensor_x - scan_width
        for x in range(scan_width * 2 + 1): # scan_width in each direction from the midpoint plus the mid point
            scanned_positions.add(scan_start + x)
        # Also track sensors and beacons on the scanline
        if sensor_y == SCANLINE:
            beacons_and_sensors.add(sensor_x)
        if beacon_y == SCANLINE:
            beacons_and_sensors.add(beacon_x)
    print(len(scanned_positions) - len(beacons_and_sensors))

def solve15_p2(input: list[str]) -> None:
    # Is this brute-force efficient? No.
    # Does it work for a one-off solution? It takes under a minute on my machine, so I think it's fine
    coordinates = extract_coordinates(input)
    coverage = list()
    SEARCH_LENGTH = 4000000
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in coordinates:
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        coverage.append((distance, sensor_x, sensor_y))
    x, y = 0, 0
    while y <= SEARCH_LENGTH:
        while x <= SEARCH_LENGTH:
            found = True
            for distance, sensor_x, sensor_y in coverage:
                distance_to_sensor = abs(sensor_x - x) + abs(sensor_y - y)
                if distance_to_sensor <= distance:
                    found = False
                    # Skip to end of range in this line
                    distance_to_scanline = abs(y - sensor_y)
                    scan_width = distance - distance_to_scanline
                    scan_end = sensor_x + scan_width
                    x = scan_end
                    break
            if found:
                print("(x={}, y={})".format(x, y))
                print(x * 4000000 + y)
                return
            x += 1
        x = 0
        y += 1

if __name__ == "__main__":
    with open("../inputs/input15.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve15_p1(input)
    print("\nPart 2 solution:")
    solve15_p2(input)
