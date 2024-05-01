# Pure function for trajectory calculation
def calculate_trajectory(altitude, velocity):
    gravity = 1.625  # Acceleration due to gravity on the Moon (m/s^2)
    descent_rate = velocity - gravity  # Adjusted descent rate
    new_altitude = altitude - descent_rate  # New altitude
    return new_altitude

# Pure function for thrust control
def adjust_thrust(thrust, target_velocity, current_velocity):
    thrust_correction = 0.2 * (target_velocity - current_velocity)  # Proportional thrust adjustment
    new_thrust = thrust + thrust_correction
    return new_thrust

# Pure function for terrain analysis
def analyze_terrain(altitude, terrain_data):
    if altitude < terrain_data["safe_altitude"]:
        return "WARNING: Approaching unsafe altitude!"
    else:
        return "Altitude within safe range."

# Pure function for abort criteria
def check_abort_criteria(sensor_data):
    if sensor_data["engine_temperature"] > 1000 or sensor_data["fuel_level"] < 10:
        return "ABORT: Engine overheating or low fuel level detected!"
    else:
        return "Landing conditions normal."

# Pure function for decision making
def evaluate_situation(altitude, velocity, sensor_data, terrain_data):
    terrain_status = analyze_terrain(altitude, terrain_data)
    abort_status = check_abort_criteria(sensor_data)
    if "WARNING" in terrain_status or "ABORT" in abort_status:
        return "ABORT: Risky landing conditions detected."
    else:
        return "Continue descent: Landing conditions optimal."

# Main program
if __name__ == "__main__":
    # Simulated lunar landing scenario for Chandrayaan-3
    initial_altitude = 2000  # Starting altitude (m)
    initial_velocity = 60    # Starting velocity (m/s)
    initial_thrust = 40      # Starting thrust (N)

    # Simulated sensor and terrain data for Chandrayaan-3
    sensor_data = {"engine_temperature": 600, "fuel_level": 70}  # Sensor readings
    terrain_data = {"safe_altitude": 500}  # Terrain safety thresholds

    # Flag to keep track of unsafe landing detection
    unsafe_detected = False

    # Loop until landing conditions are met
    while initial_altitude > 0:
        # Calculate trajectory and adjust thrust
        initial_altitude = calculate_trajectory(initial_altitude, initial_velocity)
        initial_thrust = adjust_thrust(initial_thrust, 40, initial_velocity)

        # Analyze terrain and evaluate situation
        terrain_status = analyze_terrain(initial_altitude, terrain_data)
        situation_status = evaluate_situation(initial_altitude, initial_velocity, sensor_data, terrain_data)

        # Check for unsafe landing conditions
        if "WARNING" in terrain_status and not unsafe_detected:
            print("Unsafe landing conditions detected. Adjusting to normal state...")
            # Adjust altitude and thrust to normal state
            initial_altitude += 200  # Add 200 meters to altitude
            initial_thrust += 10     # Increase thrust by 10 N
            unsafe_detected = True

        # Print results for each iteration
        print("New Altitude:", initial_altitude)
        print("New Thrust:", initial_thrust)
        print("Terrain Status:", terrain_status)
        print("Situation Status:", situation_status)
        print("-------------------------")

    # Successful landing message
    print("Landing successful. The spacecraft has safely landed on the moon's surface.")