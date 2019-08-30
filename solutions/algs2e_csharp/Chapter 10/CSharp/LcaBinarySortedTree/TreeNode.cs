using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace LcaBinarySortedTree
{
    public class TreeNode
    {
        public int Value = -1;
        public TreeNode LeftChild = null;
        public TreeNode RightChild = null;

        // Space to skip horizontally between siblings
        // and vertically between tree levels.
        private const float Hoffset = 10;
        private const float Voffset = 20;

        // The circle's radius.
        private const float Radius = 12;

        // The node's center and bounding rectangle after arranging.
        private PointF Center;
        private RectangleF Bounds;

        // The node's background brush.
        public Brush BgBrush = Brushes.White;

        // Draw the tree.
        public void DrawTree(Graphics gr,
            Brush textBrush, Pen pen, Font font, StringFormat sf)
        {
            DrawSubtreeLinks(gr, pen);
            DrawSubtreeNodes(gr, textBrush, pen, font, sf);
        }

        // Draw the subtree's links.
        public void DrawSubtreeLinks(Graphics gr, Pen pen)
        {
            if (LeftChild != null)
            {
                gr.DrawLine(pen, Center, LeftChild.Center);
                LeftChild.DrawSubtreeLinks(gr, pen);
            }
            if (RightChild != null)
            { 
                gr.DrawLine(pen, Center, RightChild.Center);
                RightChild.DrawSubtreeLinks(gr, pen);
            }
        }

        // Draw the subtree's nodes.
        public void DrawSubtreeNodes(Graphics gr,
            Brush textBrush, Pen pen, Font font, StringFormat sf)
        {
            // Draw the circle.
            gr.FillEllipse(BgBrush, Bounds);
            gr.DrawEllipse(pen, Bounds);

            // Draw the label.
            gr.DrawString(Value.ToString(), font, textBrush, Center, sf);

            // Draw the child subtrees.
            if (LeftChild != null)
                LeftChild.DrawSubtreeNodes(gr, textBrush, pen, font, sf);
            if (RightChild != null)
                RightChild.DrawSubtreeNodes(gr, textBrush, pen, font, sf);
        }

        // Build a full binary tree with the indicated
        // upper left corner.
        public static TreeNode BuildFullTree(int height, Point upperLeftCorner)
        {
            // Build the nodes.
            TreeNode root = new TreeNode();
            root.BuildSubtree(height);

            // Assign node values.
            int value = 1;
            root.AssignValues(ref value);

            // Position the nodes.
            // Calculate the tree's width.
            int numLeafNodes = (int)Math.Pow(2, height);
            float width = numLeafNodes * (2 * Radius) +
                (numLeafNodes - 1) * Hoffset;
            float ymin = upperLeftCorner.Y + Radius;
            float xmin = upperLeftCorner.X;
            float xmax = xmin + width;
            root.PositionSubtree(ymin, xmin, xmax);

            return root;
        }

        // Build a subtree below this node of the given height.
        public void BuildSubtree(int height)
        {
            if (height == 0) return;

            // Build child subtrees.
            LeftChild = new TreeNode();
            LeftChild.BuildSubtree(height - 1);

            RightChild = new TreeNode();
            RightChild.BuildSubtree(height - 1);
        }

        // Perform an inorder traversal and assign values to the nodes.
        private void AssignValues(ref int value)
        {
            if (LeftChild != null) LeftChild.AssignValues(ref value);
            Value = value;
            value++;
            if (RightChild != null) RightChild.AssignValues(ref value);
        }

        // Position the node at this y position 
        // centered between xmin and xmax horizontally.
        private void PositionSubtree(float y, float xmin, float xmax)
        {
            // Position this node.
            float xmid = (xmin + xmax) / 2;
            y += Radius;
            Center = new PointF(xmid, y);
            Bounds = new RectangleF(
                Center.X - Radius, Center.Y - Radius,
                2 * Radius, 2 * Radius);

            // Position our child nodes.
            y += Radius + Voffset;
            if (LeftChild != null)
                LeftChild.PositionSubtree(y, xmin, xmid);
            if (RightChild != null)
                RightChild.PositionSubtree(y, xmid, xmax);
        }

        // Return the node at this position.
        public TreeNode NodeAtPosition(Point location)
        {
            // If this node is here, return it.
            if (Bounds.Contains(location)) return this;

            // See if a node in the child subtrrees is at this position.
            if (LeftChild != null)
            {
                TreeNode hitNode = LeftChild.NodeAtPosition(location);
                if (hitNode != null) return hitNode;
            }
            if (RightChild != null)
            {
                TreeNode hitNode = RightChild.NodeAtPosition(location);
                if (hitNode != null) return hitNode;
            }

            return null;
        }

        // Find the LCA for the two nodes.
        public TreeNode FindLca(int value1, int value2)
        {
            // See if both nodes belong down the same child branch.
            if ((value1 < Value) && (value2 < Value))
                return LeftChild.FindLca(value1, value2);
            if ((value1 > Value) && (value2 > Value))
                return RightChild.FindLca(value1, value2);

            // This is the LCA.
            return this;
        }
    }
}
