using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace BoidsGravity
{
    class Boid
    {
        public double Mass = 0;
        public Point2d Position = new Point2d(0, 0);
        public Vector2d Velocity = new Vector2d(0, 0);
        public double MaxSpeed = 0;         // Pixels per second.
        public double NeighborhoodDist = 0; // Detection distance.

        public Boid(double mass, Point2d position, Vector2d velocity,
            double maxSpeed, double neighborhoodDist)
        {
            Mass = mass;
            Position = position;
            Velocity = velocity;
            MaxSpeed = maxSpeed;
            NeighborhoodDist = neighborhoodDist;
        }

        public void Move(List<Boid> boids, Point2d target,
            double targetMass, double deltaTime, double attractionWgt,
            double repulsionWgt, double targetWgt)
        {
            int numNeighbors = 0;
            Vector2d attraction = new Vector2d(0, 0);
            Vector2d repulsion = new Vector2d(0, 0);

            foreach (Boid neighbor in boids)
            {
                // Skip if it's this boid or not a neighbor.
                if (neighbor == this) continue;
                double dist = Distance(neighbor);
                if (dist > NeighborhoodDist) continue;
                if (dist < 0.1) dist = 0.1;

                numNeighbors++;

                // Calculate attractive force.
                Vector2d newAttraction =
                    new Vector2d(this.Position, neighbor.Position);
                attraction += newAttraction *
                    this.Mass * neighbor.Mass / (dist * dist);

                // Calculate repulsive force.
                Vector2d newRepulsion =
                    new Vector2d(neighbor.Position, this.Position);
                repulsion += newRepulsion *
                    this.Mass * neighbor.Mass / (dist * dist * dist);
            }

            // Get the vector toward the target.
            Vector2d targetAttraction = target - Position;
            double targetDist = targetAttraction.Length;
            targetAttraction *= this.Mass * targetMass / (targetDist * targetDist);

            // Update the velocity.
            Vector2d force =
                attraction * attractionWgt +
                repulsion * repulsionWgt +
                targetAttraction * targetWgt;
            Vector2d acceleration = force / Mass;
            Velocity += acceleration * deltaTime;
            if (Velocity.Length > MaxSpeed)
                Velocity.SetLength(MaxSpeed);

            // Update the location.
            Position += Velocity * deltaTime;
        }

        // Return the distance to another Boid.
        private double Distance(Boid other)
        {
            Vector2d v = Position - other.Position;
            return v.Length;
        }

        // Draw.
        public void Draw(Graphics gr)
        {
            const float radius = 2;
            RectangleF rect = new RectangleF(
                (float)(Position.X - radius),
                (float)(Position.Y - radius),
                2 * radius, 2 * radius);
            gr.FillEllipse(Brushes.Black, rect);
        }
    }
}
