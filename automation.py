from devices import fan_on
from devices import fan_off


def automatic_fan(temp):

    if temp > 30:

        fan_on()

    else:

        fan_off()