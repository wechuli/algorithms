using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace SwarmMinimum
{
    class Bug
    {
        public static Random Rand = new Random();

        public double BestValue;
        public Point2d BestPoint, Location;
        public Vector2d Velocity;
        public double MaxSpeed;
        public int LockAfter;
        public Func<Point2d, double> F;
        public bool IsActive = true;
        public int MovesSinceChanged = 0;

        public Bug(Func<Point2d, double> f, Point2d location,
            Vector2d velocity, double maxSpeed, int lockAfter)
        {
            F = f;
            Location = new Point2d(location);
            Velocity = velocity;
            MaxSpeed = maxSpeed;
            LockAfter = lockAfter;

            BestPoint = new Point2d(location);
            BestValue = F(Location);
        }

        // Move the bug.
        public void Move(double deltaTime, double cogAccel, double socAccel,
            ref Point2d globalBestPoint, ref double globalBestValue)
        {
            if (!IsActive) return;

            // Calculate the forces.
            Vector2d cogForce =
                Rand.NextDouble() * cogAccel * (this.BestPoint - this.Location);
            Vector2d socForce =
                Rand.NextDouble() * socAccel * (globalBestPoint - this.Location);

            // Update the velocity.
            Velocity += deltaTime * (cogForce + socForce);
            if (Velocity.Length > MaxSpeed)
                Velocity.SetLength(MaxSpeed);

            // Update the position.
            Location += Velocity * deltaTime;

            // See if this gives a new best value.
            double value = Value;
            if (value < BestValue)
            {
                BestValue = value;
                BestPoint = new Point2d(Location);

                if (value < globalBestValue)
                {
                    globalBestValue = value;
                    globalBestPoint = new Point2d(Location);
                }
            }
            else
            {
                MovesSinceChanged++;
                IsActive = (MovesSinceChanged < LockAfter);
            }
        }

        // Return the Bug's current value.
        public double Value
        {
            get
            {
                return F(Location);
            }
        }
    }
}
