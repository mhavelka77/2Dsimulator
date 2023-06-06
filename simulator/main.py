from simulation import Simulation

def main():
    simulation = Simulation(0.1, terminal=False)
    simulation.add_body(mass=1e13, position=(0, 0))
    simulation.add_body(mass=1e11, position=(10, 0), velocity=(0, 7))

    simulation.run()

if __name__ == "__main__":
    main()