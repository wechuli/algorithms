using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace Quadtree
{
    public class QuadtreeNode
    {
        // The maximum number of points allowed in a quadtree node.
        public const int MaxPoints = 10;

        // The bounds and middle X and Y values.
        public float Xmin, Ymin, Xmax, Ymax, Xmid, Ymid;
           
        // The points in this quadtree node.
        public List<PointF> Points = new List<PointF>();

        // The child quadtree nodes in order NW, NE, SW, SE.
        List<QuadtreeNode> Children = new List<QuadtreeNode>();
        
        // Initializing constructor.
        public QuadtreeNode(float xmin, float ymin, float xmax, float ymax)
        {
            Xmin = xmin;
            Ymin = ymin;
            Xmax = xmax;
            Ymax = ymax;
            Xmid = (Xmin + Xmax) / 2;
            Ymid = (Ymin + Ymax) / 2;
        }

        // Add a point to this node.
        public void AddPoint(PointF newPoint)
        {
            // See if this quadtree node us full.
            if ((Points != null) && (Points.Count >= MaxPoints))
            {
                // Divide this quadtree node.
                Children.Add(new QuadtreeNode(Xmin, Ymin, Xmid, Ymid)); // NW
                Children.Add(new QuadtreeNode(Xmid, Ymin, Xmax, Ymid)); // NE
                Children.Add(new QuadtreeNode(Xmin, Ymid, Xmid, Ymax)); // SW
                Children.Add(new QuadtreeNode(Xmid, Ymid, Xmax, Ymax)); // SE

                // Move the points into the appropriate subtrees.
                foreach (PointF point in Points)
                    AddPointToChild(point);

                // Remove this node's points list.
                Points = null;
            }

            // Add the new point here or in the appropriate subtree.
            if (Points != null)
                Points.Add(newPoint);
            else
                AddPointToChild(newPoint);
        }

        // Add a point to the appropriate child subtree.
        private void AddPointToChild(PointF point)
        {
            foreach (QuadtreeNode child in Children)
                if ((point.X >= child.Xmin) &&
                    (point.X <= child.Xmax) &&
                    (point.Y >= child.Ymin) &&
                    (point.Y <= child.Ymax))
                {
                    child.AddPoint(point);
                    break;
                }
        }

        // Draw the points in this quadtree node.
        public void DrawPoints(Graphics gr, Brush brush, Pen pen, float radius)
        {
            // See if this node has children.
            if (Points == null)
                // Make the children draw themselves.
                foreach (QuadtreeNode child in Children)
                    child.DrawPoints(gr, brush, pen, radius);
            else
                // Draw the points in this node.
                foreach (PointF point in Points)
                    DrawPoint(gr, point, brush, pen, radius);
        }

        // Draw a point centered at this spot.
        private void DrawPoint(Graphics gr, PointF point, Brush brush, Pen pen, float radius)
        {
            RectangleF rect = new RectangleF(
                point.X - radius, point.Y - radius,
                2 * radius, 2 * radius);
            gr.FillEllipse(brush, rect);
            gr.DrawEllipse(pen, rect);
        }

        // Draw the quadtree areas.
        public void DrawAreas(Graphics gr, Pen pen)
        {
            // Draw this quadtree node's area.
            gr.DrawRectangle(pen, Xmin, Ymin, Xmax - Xmin, Ymax - Ymin);

            // Draw the child nodes.
            foreach (QuadtreeNode child in Children)
                child.DrawAreas(gr, pen);
        }

        // Find the specified point.
        // Return (-infinity, -infinity) if we don't find it.
        public PointF FindPoint(PointF target, float radius)
        {
            // Make sure the point might intersect this node's area.
            if ((target.X + radius < Xmin) ||
                (target.X - radius > Xmax) ||
                (target.Y + radius < Ymin) ||
                (target.Y - radius > Ymax))
                return new PointF(float.NegativeInfinity, float.NegativeInfinity);

                // If we have children, call FindPointInChildren.
            if (Points == null) return FindPointInChildren(target, radius);

            // Search for the point in this quadtree node.
            return FindPointHere(target, radius);
        }

        // Search the children to find the point closest to the target.
        private PointF FindPointInChildren(PointF target, float radius)
        {
            // Keep track of the best point we find.
            PointF bestPoint = new PointF(float.NegativeInfinity, float.NegativeInfinity);
            float bestDistance = float.MaxValue;

            // Search the child subtrees for the target_point.
            foreach (QuadtreeNode child in Children)
            {
                // See if the target is in this child.
                PointF testPoint = child.FindPoint(target, radius);
                if (testPoint.X > float.NegativeInfinity)
                {
                    float testDistance = Distance(target, testPoint);
                    if (testDistance < bestDistance)
                    {
                        bestDistance = testDistance;
                        bestPoint = testPoint;
                    }
                }
            }

            // Return the best point we found.
            return bestPoint;
        }

        // Search this node's points for the target.
        private PointF FindPointHere(PointF target, float radius)
        {
            // Keep track of the best point we find.
            PointF bestPoint = new PointF(float.NegativeInfinity, float.NegativeInfinity);
            float bestDistance = float.MaxValue;

            // Search the points.
            foreach (PointF testPoint in Points)
            {
                float testDistance = Distance(target, testPoint);
                if ((testDistance < radius) &&
                    (testDistance < bestDistance))
                {
                    bestDistance = testDistance;
                    bestPoint = testPoint;
                }
            }

            // Return the best point we found.
            return bestPoint;
        }

        // Return the distance between two points.
        private float Distance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)Math.Sqrt(dx * dx + dy * dy);
        }
    }
}
