"""Constants used through the simulation."""

BOUNDS_WIDTH: int = 400
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: int = 400
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

CELL_RADIUS: int = 15
CELL_COUNT: int = 50
INFECTED_CELL_COUNT: int = 5
IMMUNE_CELL_COUNT: int = 10
CELL_SPEED: float = 5.0 # Default is 5.0
RECOVERY_PERIOD: int = 90 # A change made that might be causing problems

IMMUNE: int = -1 # A change made that might be causing problems
VULNERABLE: int = 0
INFECTED: int = 1