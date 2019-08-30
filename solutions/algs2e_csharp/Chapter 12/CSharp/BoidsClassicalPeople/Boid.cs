using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace BoidsClassicalPeople
{
    class Boid
    {
        public Point2d Position = new Point2d(0, 0);
        public Vector2d Velocity = new Vector2d(0, 0);
        public double MaxSpeed = 0;         // Pixels per second.
        public double NeighborhoodDist = 0; // Detection distance.

        public Boid(Point2d position, Vector2d velocity,
            double maxSpeed, double neighborhoodDist)
        {
            Position = position;
            Velocity = velocity;
            MaxSpeed = maxSpeed;
            NeighborhoodDist = neighborhoodDist;
        }

        public void Move(List<Boid> boids, List<Point2d> people,
            Point2d target, double deltaTime,
            double separationWgt, double alignmentWgt,
            double cohesionWgt, double targetWgt, double personWgt)
        {
            int numNeighbors = 0;
            Point2d nbrCenter = new Point2d(0, 0);
            Vector2d nbrSeparation = new Vector2d(0, 0);
            Vector2d nbrAlignment = new Vector2d(0, 0);

            foreach (Boid neighbor in boids)
            {
                // Skip if it's this boid or not a neighbor.
                if (neighbor == this) continue;
                if (Distance(neighbor) > NeighborhoodDist) continue;

                numNeighbors++;

                // Add vectors from the neighbors to this Boid
                // to push away from the neighbors (for separation).
                Vector2d separationVector = (Position - neighbor.Position);
                nbrSeparation += separationVector;

                // Add the velocities (for alignment).
                nbrAlignment += neighbor.Velocity;

                // Add the locations (for cohesion).
                nbrCenter += neighbor.Position;
            }

            // Average the separation components.
            Vector2d nbrCohesion = new Vector2d(0, 0);
            if (numNeighbors > 0)
            {
                nbrSeparation /= numNeighbors;

                // Average the alignment components.
                nbrAlignment /= numNeighbors;

                // Use the average location to calculate the cohesion component.
                nbrCenter /= numNeighbors;
                nbrCohesion = nbrCenter - Position;
            }

            // Get the vector toward the target.
            Vector2d targetVector = target - Position;
            targetVector.Normalize();

            // Adjust for people.
            int numPeople = 0;
            Vector2d personVector = new Vector2d();
            foreach (Point2d person in people)
            {
                if (Distance(person) < NeighborhoodDist)
                {
                    numPeople++;
                    personVector += (Position - person);
                }
            }
            if (numPeople > 0) personVector /= numPeople;

            // Adjust this Boid.
            Vector2d newVelocity =
                nbrSeparation* separationWgt +
                nbrAlignment * alignmentWgt +
                nbrCohesion * cohesionWgt +
                targetVector * targetWgt +
                personVector * personWgt;
            Velocity += newVelocity * deltaTime;
            if (Velocity.Length > MaxSpeed)
                Velocity.SetLength(MaxSpeed);

            // Update the location.
            Position += Velocity * deltaTime;
        }

        // Return the distance to another Boid.
        private double Distance(Boid other)
        {
            return Distance(other.Position);
        }

        // Return the distance to a point.
        private double Distance(Point2d point)
        {
            Vector2d v = Position - point;
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
