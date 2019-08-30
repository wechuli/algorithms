using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RoundRobin
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void goButton_Click(object sender, EventArgs e)
        {
            // Get the number of teams and make the list.
            int numTeams = int.Parse(numTeamsTextBox.Text);
            List<string> teams = new List<string>();
            for (int i = 0; i < numTeams; i++)
                teams.Add($"Team {i + 1}");

            // Build the schedule.
            List<List<MatchUp>> schedule =
                ScheduleRoundRobin(teams);

            // Display the schedule.
            scheduleTreeView.Nodes.Clear();
            for (int i = 0; i < schedule.Count; i++)
            {
                TreeNode roundNode =
                    scheduleTreeView.Nodes.Add($"Round {i + 1}");
                foreach (MatchUp match in schedule[i])
                {
                    roundNode.Nodes.Add(
                        $"{match.Team1} versus {match.Team2}");
                }
            }
            scheduleTreeView.ExpandAll();
        }

        // Find a round robin schedule for the teams.
        private List<List<MatchUp>>
            ScheduleRoundRobin(List<string> teamList)
        {
            // Copy the team list.
            List<string> teams = new List<string>(teamList);

            // See if the number of teams is odd or even.
            string byeTeam = "BYE";
            if (teams.Count % 2 == 0)
            {
                // Even. Use the first item as the bye team.
                byeTeam = teams[0];
                teams.RemoveAt(0);
            }

            // Make the schedule.
            return ScheduleRoundRobinOdd(teams, byeTeam);
        }

        // Find a round robin schedule for the teams.
        private List<List<MatchUp>>
            ScheduleRoundRobinOdd(List<string> teams, string byeTeam)
        {
            int numTeams = teams.Count;
            int mid = numTeams / 2;

            // Loop.
            List<List<MatchUp>> schedule =
                new List<List<MatchUp>>();
            for (int i = 0; i < numTeams; i++)
            {
                // Save this arrangement.
                List<MatchUp> round = new List<MatchUp>();
                for (int j = 1; j <= mid; j++)
                    round.Add(new MatchUp(teams[j], teams[numTeams - j]));
                round.Add(new MatchUp(teams[0], byeTeam));
                schedule.Add(round);

                // Rotate.
                teams.Insert(0, teams[numTeams - 1]);
                teams.RemoveAt(numTeams);
            }

            return schedule;
        }
    }
}
