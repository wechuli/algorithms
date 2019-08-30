using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace IntervalTrees2
{
    class IntervalNode
    {
        public float Xmin, Xmid, Xmax;
        public List<Interval> LeftOverlap = new List<Interval>();
        public List<Interval> RightOverlap = new List<Interval>();
        public IntervalNode LeftChild = null;
        public IntervalNode RightChild = null;

        public IntervalNode(float xmin, float xmax)
        {
            Xmin = xmin;
            Xmax = xmax;
            Xmid = (xmin + xmax) / 2;
        }

        // Add an interval to the node.
        public void AddInterval(Interval interval)
        {
            // Find the interval's position.
            if (interval.RightPoint.X < Xmid)
            {
                // Left branch.
                if (LeftChild == null)
                    LeftChild = new IntervalNode(Xmin, Xmid);
                LeftChild.AddInterval(interval);
            }
            else if (interval.LeftPoint.X > Xmid)
            {
                // Right branch.
                if (RightChild == null)
                    RightChild = new IntervalNode(Xmid, Xmax);
                RightChild.AddInterval(interval);
            }
            else
            {
                // Overlapping.
                // Add to the left overlap list in sorted order.
                int position = 0;
                foreach (Interval seg in LeftOverlap)
                    if (seg.LeftPoint.X < interval.LeftPoint.X)
                        position++;
                LeftOverlap.Insert(position, interval);

                // Add to the right overlap list in sorted order.
                position = 0;
                foreach (Interval seg in RightOverlap)
                    if (seg.RightPoint.X > interval.RightPoint.X)
                        position++;
                RightOverlap.Insert(position, interval);
            }
        }

        // Make an interval tree for the given horizontal intervals.
        public static IntervalNode MakeIntervalTree(List<Interval> intervals)
        {
            // Find the intervals' X coordinate bounds.
            float xmin = intervals[0].LeftPoint.X;
            float xmax = xmin;
            foreach (Interval interval in intervals)
            {
                if (interval.LeftPoint.X < xmin) xmin = interval.LeftPoint.X;
                if (interval.LeftPoint.X > xmax) xmax = interval.LeftPoint.X;
                if (interval.RightPoint.X < xmin) xmin = interval.RightPoint.X;
                if (interval.RightPoint.X > xmax) xmax = interval.RightPoint.X;
            }

            // Add the intervals to a tree.
            IntervalNode root = new IntervalNode(xmin, xmax);
            foreach (Interval interval in intervals)
                root.AddInterval(interval);

            // Return the tree.
            return root;
        }

        // Find intervals that overlap the target X value.
        public void FindOverlappingIntervals(List<Interval> results, int testX)
        {
            // Check our overlap intervals.
            if (testX <= Xmid)
            {
                // Use the left overlap list.
                foreach (Interval seg in LeftOverlap)
                {
                    if (seg.LeftPoint.X > testX) break;
                    results.Add(seg);
                }
            }
            else
            {
                // Use the right overlap list.
                foreach (Interval seg in RightOverlap)
                {
                    if (seg.RightPoint.X < testX) break;
                    results.Add(seg);
                }
            }

            // Check left branch.
            if ((testX < Xmid) && (LeftChild != null))
            {
                LeftChild.FindOverlappingIntervals(results, testX);
            }
            else if ((testX > Xmid) && (RightChild != null))
            {
                RightChild.FindOverlappingIntervals(results, testX);
            }
        }

        // Find intervals that overlap the target interval xmin --> xmax.
        public void FindOverlappingIntervals(
            List<Interval> results, int xmin, int xmax)
        {
            // Check our overlap intervals.
            if (xmax <= Xmid)
            {
                // Use the left overlap list.
                foreach (Interval seg in LeftOverlap)
                {
                    if (seg.LeftPoint.X > xmax) break;
                    results.Add(seg);
                }
            }
            else if (xmin >= Xmid)
            {
                // Use the right overlap list.
                foreach (Interval seg in RightOverlap)
                {
                    if (seg.RightPoint.X < xmin) break;
                    results.Add(seg);
                }
            }
            else
            {
                // Add all intervals.
                foreach (Interval seg in LeftOverlap)
                    results.Add(seg);
            }

            // Check the children.
            if ((xmin < Xmid) && (LeftChild != null))
            {
                LeftChild.FindOverlappingIntervals(results, xmin, xmax);
            }
            if ((xmax > Xmid) && (RightChild != null))
            {
                RightChild.FindOverlappingIntervals(results, xmin, xmax);
            }
        }
    }
}
