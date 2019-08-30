import tkinter as tk
from tkinter import ttk

class MatchUp:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

def schedule_round_robin(team_list):
    """ Find a round robin schedule for the teams."""
    # Copy the team list.
    teams = team_list.copy()

    # See if the number of teams is odd or even.
    bye_team = "BYE"
    if len(teams) % 2 == 0:
        # Even. Use the first item as the bye team.
        bye_team = teams[0]
        del teams[0]

    # Make the schedule.
    return schedule_round_robin_odd(teams, bye_team)

def schedule_round_robin_odd(teams, bye_team):
    """ Find a round robin schedule for the teams."""
    num_teams = len(teams)
    mid = num_teams // 2

    # Loop.
    schedule = []
    for i in range(num_teams):
        # Save this arrangement.
        round = []
        for j in range(mid):
            round.append(MatchUp(teams[j], teams[num_teams - 2 - j]))
        round.append(MatchUp(teams[num_teams - 1], bye_team))
        schedule.append(round)

        # Rotate.
        teams.insert(0, teams[num_teams - 1])
        del teams[num_teams]

    return schedule

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("round_robin")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x250")

        params_frame = tk.Frame(self.window)
        params_frame.pack(fill=tk.BOTH)

        num_teams_label = tk.Label(params_frame, text="# Teams:")
        num_teams_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.num_teams_entry = tk.Entry(params_frame, width=4, justify=tk.RIGHT)
        self.num_teams_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.num_teams_entry.insert(tk.END, "6")
        go_button = tk.Button(params_frame, text="Go", width=8, command=self.go)
        go_button.grid(row=0, column=2, padx=5, pady=5)

        schedule_label = tk.Label(params_frame, text="Schedule:", anchor=tk.W)
        schedule_label.grid(row=1, column=0, padx=5, pady=(2,0), sticky=tk.W)

        # List.
        list_frame = tk.Frame(self.window)
        list_frame.pack(padx=5, pady=(0,5), side=tk.TOP, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(list_frame)
        self.treeview.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(pady=5, side=tk.RIGHT, fill=tk.Y)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_teams_entry.focus_force()
        self.window.mainloop()

    def go(self):
        """ Find a round robin schedule."""
        # Get the number of teams and make the list.
        num_teams = int(self.num_teams_entry.get())

        teams = []
        for i in range(num_teams):
            teams.append(f"Team {i + 1}")
        print(f"Teams: {teams}")#@

        # Build the schedule.
        schedule = schedule_round_robin(teams)

        # Display the schedule.
        self.treeview.delete(*self.treeview.get_children())
        for i in range(len(schedule)):
            round_node = self.treeview.insert("", tk.END, text=f"Round {i + 1}", open=True)
            for match in schedule[i]:
                self.treeview.insert(round_node, tk.END, text=f"{match.team1} versus {match.team2}", open=True)

if __name__ == '__main__':
    app = App()

# app.root.destroy()
