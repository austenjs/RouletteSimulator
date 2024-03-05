import argparse
import random

from RouletteSimulator import (
    EuropeanTable,
    DalembertPlayer,
    Dealer,
    FibonacciPlayer,
    MartingalePlayer,
    PloppyPlayer,
    RomanovskyPlayer,
    Simulator
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--initial_money", type=float,
                        help="Initial amount of money to play", default=100)
    parser.add_argument("--num_simulations", type=int,
                        help="Number of roulette simulations", default=100)
    parser.add_argument("--iteration_per_simulation",
                        type=int, help="Number of games per simulation", default=100)
    parser.add_argument("--verbose", action="store_true",
                        help="Print the money of all players at each iteration (for debug)")
    parser.add_argument("--random_seed", type=int, help="Random seed for RNG", default=42)

    args = parser.parse_args()
    random.seed(args.random_seed)
    initial_money = args.initial_money
    num_simulations = args.num_simulations
    iteration_per_simulation = args.iteration_per_simulation
    verbose = args.verbose

    dealer = Dealer()
    players = [
            DalembertPlayer(initial_money),
            FibonacciPlayer(initial_money),
            MartingalePlayer(initial_money),
            PloppyPlayer(initial_money),
            RomanovskyPlayer(initial_money)
        ]
    table = EuropeanTable()

    number_of_wins = [0 for _ in range(len(players))]
    payout = [0 for _ in range(len(players))]
    simulator = Simulator(players, dealer, table)

    for _ in range(num_simulations):
        # Reset players balance
        for player in players:
            player.set_money(initial_money)

        # Simulation
        for iteration in range(iteration_per_simulation):
            if verbose:
                for i, player in enumerate(players):
                    print(f'Iteration no: {iteration} \
                          | Player {i + 1} has {player.get_money()} left')
            simulator.simulate_one_game()

        # Update statistics
        for i, player in enumerate(players):
            final_money = player.get_money()
            if final_money > initial_money:
                number_of_wins[i] += 1
            payout[i] += final_money - initial_money

    for i, player in enumerate(players):
        print(f'Statistics for {str(player)} player')
        print(f'Percentage profit: {number_of_wins[i] / num_simulations * 100}%')
        print(f'Average payout: {payout[i] / num_simulations}')
        print('=' * 10)

if __name__ == '__main__':
    main()
