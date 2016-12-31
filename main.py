from Security.Security import Security
from Temperature.Temperature import Temperature


temp = Temperature(False,'28-0316563a9dff')
temp.get_temperature()
security = Security(17, 18, 3)
security.secure_up()
