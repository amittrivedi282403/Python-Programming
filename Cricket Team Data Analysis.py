import matplotlib.pyplot as plt

file_path = 'Project_odi.csv'

class MatchStatistics:
    def __init__(self):
        self.total_matches = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_runs = 0
        self.total_wickets = 0

    def calculate_stats(self):
        pass  # This will be overridden by derived classes

    def display_total_matches(self):
        print(f"\nTotal Matches: {self.total_matches}\n")

    def display_wins(self):
        print(f"\nWins: {self.wins} Win Percentage: {round(self.win_percentage(), 2)} %\n")

    def display_losses(self):
        print(f"\nLosses: {self.losses} Loss Percentage: {round(self.loss_percentage(), 2)} %\n")

    def display_ties(self):
        print(f"\nTied: {self.ties} Tie Percentage: {round(self.tie_percentage(), 2)} %\n")

    def display_total_runs(self):
        print(f"\nTotal Runs Scored in complete matches: {self.total_runs}\n")

    def display_total_wickets(self):
        print(f"\nTotal Wickets Taken in complete matches: {self.total_wickets}\n")

    def win_percentage(self):
        return (self.wins / self.total_matches) * 100 if self.total_matches > 0 else 0

    def loss_percentage(self):
        return (self.losses / self.total_matches) * 100 if self.total_matches > 0 else 0

    def tie_percentage(self):
        return (self.ties / self.total_matches) * 100 if self.total_matches > 0 else 0

class ODIStatistics(MatchStatistics):
    def __init__(self):
        super().__init__()
        self.player_of_match_count = {}

    def calculate_stats(self):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            for line in lines[1:]:
                parts = line.strip().split(',')
                result = parts[3]
                runs_scored = int(parts[4])
                wickets_taken = int(parts[5])
                player_of_match = parts[6]

                self.total_matches += 1
                if result == "Win":
                    self.wins += 1
                elif result == "Loss":
                    self.losses += 1
                elif result == "Tied":
                    self.ties += 1

                self.total_runs += runs_scored
                self.total_wickets += wickets_taken

                if player_of_match in self.player_of_match_count:
                    self.player_of_match_count[player_of_match] += 1
                else:
                    self.player_of_match_count[player_of_match] = 1

    def display_most_player_of_match(self):
        most_player_of_match = ''
        total_awards = 0
        for player, count in self.player_of_match_count.items():
            if count > total_awards:
                most_player_of_match = player
                total_awards = count

        print(f"\nMost 'Player of the Match' Awards: {most_player_of_match} with {total_awards} awards\n")

    def display_all(self):
        print("\nODI match summary from 2016 to 2024:\n")
        self.display_total_matches()
        self.display_wins()
        self.display_losses()
        self.display_ties()
        self.display_total_runs()
        self.display_total_wickets()
        self.display_most_player_of_match()

    # Visualization 1: Pie Chart for Wins, Losses, and Ties
    def plot_wins_losses_ties(self):
        labels = ['Wins', 'Losses', 'Tied']
        sizes = [self.wins, self.losses, self.ties]
        colors = ['green', 'red', 'blue']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Win, Loss, and Tie Distribution')
        plt.show()

    # Visualization 2: Pie Chart for Total Runs and Wickets
    def plot_runs_wickets(self):
        labels = ['Total Runs', 'Total Wickets']
        sizes = [self.total_runs, self.total_wickets]
        colors = ['orange', 'purple']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Total Runs vs Wickets Distribution')
        plt.show()

    # Visualization 3: Bar Graph for Player of the Match Awards
    def plot_player_of_match(self):
        players = list(self.player_of_match_count.keys())
        awards = list(self.player_of_match_count.values())
        
        # Ensure awards are integers
        awards = [int(award) for award in awards]

        plt.figure(figsize=(12, 8))
        plt.barh(players, awards, color='teal')
        plt.title('Player of the Match Awards')
        plt.xlabel('Number of Awards')
        
        # Display integer values on the x-axis
        plt.xticks(range(0, max(awards) + 1, 1))
        
        plt.show()

def data_analysis_menu(stats):
    while True:
        print("\nData Analysis Menu:")
        print("1. Total Matches")
        print("2. Wins")
        print("3. Losses")
        print("4. Tied")
        print("5. Total Runs")
        print("6. Total Wickets")
        print("7. Most 'Player of the Match' Awards")
        print("8. All Data Analysis")
        print("9. Visualization - Wins/Losses/Ties (Pie Chart)")
        print("10. Visualization - Runs/Wickets (Pie Chart)")
        print("11. Visualization - Player of the Match (Bar Graph)")
        print("12. Return to Main Menu")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            stats.display_total_matches()
        elif choice == '2':
            stats.display_wins()
        elif choice == '3':
            stats.display_losses()
        elif choice == '4':
            stats.display_ties()
        elif choice == '5':
            stats.display_total_runs()
        elif choice == '6':
            stats.display_total_wickets()
        elif choice == '7':
            stats.display_most_player_of_match()
        elif choice == '8':
            stats.display_all()
        elif choice == '9':
            stats.plot_wins_losses_ties()
        elif choice == '10':
            stats.plot_runs_wickets()
        elif choice == '11':
            stats.plot_player_of_match()
        elif choice == '12':
            break
        else:
            print("\nInvalid choice. Please select a valid option. ")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display ODI match summary")
        print("2. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            stats = ODIStatistics()
            stats.calculate_stats()
            data_analysis_menu(stats)
        elif choice == '2':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
