class SpaceAge(object):
    # Class Constants
    EARTH_PERIOD_SECONDS = 31557600
    # The following are in Earth-Years
    PLANET_RATES = {
        'earth': 1.0,
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def _conversion_for(self, planet):
        # return PLANET_RATES[planet]
        return round(self.seconds /
                     self.EARTH_PERIOD_SECONDS /
                     self.PLANET_RATES[planet],
                     2)

    def on_earth(self):
        # return round(self.seconds / self.EARTH_PERIOD_SECONDS, 2)
        return self._conversion_for('earth')

    def on_mercury(self):
        return self._conversion_for('mercury')

    def on_jupiter(self):
        return self._conversion_for('jupiter')

    def on_venus(self):
        return self._conversion_for('venus')

    def on_mars(self):
        return self._conversion_for('mars')

    def on_neptune(self):
        return self._conversion_for('neptune')

    def on_saturn(self):
        return self._conversion_for('saturn')

    def on_uranus(self):
        return self._conversion_for('uranus')
