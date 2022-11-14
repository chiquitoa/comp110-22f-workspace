"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730295419"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between two points."""
        a: float = self.x - other.x
        b: float = self.y - other.y
        distance: float = sqrt((a * a) + (b * b))
        return (distance)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Sends a cell in a direction."""
        self.location = self.location.add(self.direction)
        
    # def color(self) -> str:
    #     """Return the color representation of a cell."""
    #     return "black"

    def contract_disease(self) -> None:
        """Makes a cell contract the disease."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> None:  # A change made that might be causing problems
        """Determines whether a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return (True)

        else:
            return (False)

    def is_vulnerable(self) -> bool:
        """Determines whether a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return (True)

        else:
            return (False)

    def is_infected(self) -> bool:
        """Determines whether a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return (True)

        else:
            return (False)

    def color(self) -> str:
        """Colors the cells appropriately."""
        if self.is_vulnerable() is True:
            return ("gray")

        elif self.is_infected() is True:
            return ("green")

        elif self.is_immune() is True:
            return ("blue")

        else:
            return ("purple")

    def contact_with(self, poor_sap: Cell) -> None:
        """Action taken when two cells come into contact."""
        if self.is_infected() is True and poor_sap.is_vulnerable() is True:
            poor_sap.contract_disease()
        if poor_sap.is_infected() is True and self.is_vulnerable() is True:
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    ticks: int = 0
    # infected_cells: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells >= cells:
            raise ValueError("You have too many infected cells. Lower this value to continue.")
        if infected_cells <= 0:
            raise ValueError("You have too few infected cells. Raise this value to continue.")
        if immune_cells >= cells:
            raise ValueError("You have too many immune cells. Lower this value to continue.")
        if immune_cells < 0:
            raise ValueError("You cannot have a negative number of immune cells. Raise this value to 0 or higher to continue.")
        if infected_cells + immune_cells >= cells:
            raise ValueError("You won't have any vulnerable cells. Reduce your infected or immune cells to continue.")
        self.population = []
        x: int = 0
        z: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if x < infected_cells:
                cell.contract_disease()
                x += 1
            elif z < immune_cells:
                cell.immunize()
                z += 1
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.ticks += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
            if cell.is_infected() is True:
                cell.sickness += 1
            if cell.sickness >= constants.RECOVERY_PERIOD:
                cell.immunize()
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected() is True:
                return (False)

        return (True)

        # if self.infected_cells == 0:
        #     return (True)
        # else:
        #     return (False)

    def check_contacts(self) -> None:
        """Checks if two cells come into contact with one another."""
        x = 0
        for cell in self.population:
            x += 1
            y = x
            while y < len(self.population):
                if cell.location.distance(self.population[y].location) <= 15:
                    cell.contact_with(self.population[y])
                    y += 1
                else:
                    y += 1