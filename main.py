from Security import Security
from Temperature import Temperature


temp = Temperature('28-0316563a9dff', False)
temp.get_temperature()
security = Security(17, 18, 3)
security.secure_up()
