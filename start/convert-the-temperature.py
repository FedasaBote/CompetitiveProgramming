class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        kelvin = celsius + 273.15
        fahren = celsius*1.8 + 32

        return [kelvin, fahren]
        