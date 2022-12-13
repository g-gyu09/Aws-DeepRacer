import math


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    reward = 0.0
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    heading = params['heading']
    speed = params['speed']
    steps = params['steps']

    if all_wheels_on_track:
        reward_wheels = 10.0
    else:
        reward_wheels = 0

    # Max Speed 2.5
    max_speed = 2.5
    reward_speed = speed / max_speed

    # 1 point for each percentage of tracks covered
    reward_progress = 1.0
    reward_progress += progress

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    # When a track is completed, points are awarded based on the percentage completed.
    if progress == 100:
        reward += 10000
    elif progress == 80:
        reward += 6000
    elif progress == 50:
        reward += 1000

    total_num_steps = 300
    if (steps % 100) == 0 and progress > (steps / total_num_steps) * 100:
        reward += 10.0
    reward += ((reward_wheels * 1.0) + (reward_speed * 0.8) + (reward_progress * 1.2))
    return float(reward)