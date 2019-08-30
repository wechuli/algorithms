﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;
using System.Diagnostics;

namespace LcaParentsAndDepths
{
    public class TreeNode
    {
        public int Value = -1;
        public int Depth = 0;
        public TreeNode Parent = null;
        public List<TreeNode> Children = new List<TreeNode>();

        // Space to skip horizontally between siblings
        // and vertically between tree levels.
        private const float Hoffset = 10;
        private const float Voffset = 20;

        // The circle's radius.
        private const float Radius = 12;

        // The node's center and bounding rectangle after arranging.
        private PointF Center;
        private RectangleF Bounds;
        private SizeF Size = new SizeF(0, 0);

        // The node's background brush.
        public Brush BgBrush = Brushes.White;

        // Initializing constructor.
        public TreeNode(TreeNode parent, int value)
        {
            if (parent != null)
            {
                Depth = parent.Depth + 1;
                parent.Children.Add(this);
            }
            Parent = parent;
            Value = value;
        }

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
            foreach (TreeNode child in Children)
            {
                gr.DrawLine(pen, Center, child.Center);
                child.DrawSubtreeLinks(gr, pen);
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
            foreach (TreeNode child in Children)
            {
                child.DrawSubtreeNodes(gr, textBrush, pen, font, sf);
            }
        }

        // Arrange the tree.
        // Call this method only for the root node.
        public void ArrangeTree(float xmin, float ymin)
        {
            SetSize();
            PositionSubtree(ymin, xmin, xmin + Size.Width);
        }

        // Set the size needed by this subtree.
        private void SetSize()
        {
            // Start with the size needed for this node.
            Size = new SizeF(2 * Radius, 2 * Radius);

            // Get child subtree sizes.
            if (Children.Count > 0)
            {
                float width = Hoffset * (Children.Count - 1);
                float height = 0;
                foreach (TreeNode child in Children)
                {
                    child.SetSize();
                    width += child.Size.Width;

                    if (height < child.Size.Height) height = child.Size.Height;
                }

                if (Size.Width < width) Size.Width = width;
                Size.Height += height + Voffset;
            }
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
            float x = xmin;
            y += Radius + Voffset;
            foreach (TreeNode child in Children)
            {
                child.PositionSubtree(y, x, x + child.Size.Width);
                x += child.Size.Width + Hoffset;
            }
        }

        // Return the node at this position.
        public TreeNode NodeAtPosition(Point location)
        {
            // If this node is here, return it.
            if (Bounds.Contains(location)) return this;

            // See if a node in the child subtrrees is at this position.
            foreach (TreeNode child in Children)
            {
                TreeNode hitNode = child.NodeAtPosition(location);
                if (hitNode != null) return hitNode;
            }

            return null;
        }

        // Find the LCA for the two nodes.
        // Call this method only for the root node.
        public TreeNode FindLca(TreeNode node1, TreeNode node2)
        {
            // Climb up until the nodes have the same depth.
            while (node1.Depth > node2.Depth) node1 = node1.Parent;
            while (node2.Depth > node1.Depth) node2 = node2.Parent;

            // Climb up until the nodes match.
            while (node1 != node2)
            {
                node1 = node1.Parent;
                node2 = node2.Parent;
            }
            return node1;
        }
    }
}
