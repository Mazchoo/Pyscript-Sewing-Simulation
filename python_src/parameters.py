""" Common place to put all parameters of simulation """

NR_SEWING_POINTS = 10  # Number of points to used to pull to sewn lines together
AVATAR_SCALING = 0.5627  # Amount to change avatar by
VERTEX_RESOLUTION = 1  # Resolution to take number of points
GRAVITY = 9.81  # Acceleration downwards due to gravity
MAX_VELOCITY = 0.5  # Terminal velocity of a piece (may need something more sophisticated with dampening)
TIME_DELTA = 0.01  # Time increment to make update to each piece
STRESS_WEIGHTING = 100  # Weight to apply to the stress force
STRESS_THRESHOLD = 0.001  # Percentage of resting distance where stress starts applying
SHEAR_WEIGHTING = 100  # Weight to apply to the shear force
SHEAR_THRESHOLD = 0.001  # Percentage of resting distance where shear starts applying
BEND_WEIGHTING = 100  # Weight to apply to bend force
BEND_THRESHOLD = 0.001  # Sin of angle where bending is applied
CM_PER_M = 100  # Scale of coordinates in clothing to world coordinates
FRICTION_CONSTANT = 0.05  # Constant of velocity resisting acceleration
VELOCITY_DAMPING = 0.9  # Amount to reduce velocity by in every step
