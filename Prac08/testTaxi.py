
from Prac07.taxi import Taxi

def main():
    prius = Taxi ("Prius 1", 100, 1.20)
    prius.drive(40)
    print(prius.get_fare())
    prius.start_fare()
    prius.drive(100)
    print(prius.get_fare())

main()