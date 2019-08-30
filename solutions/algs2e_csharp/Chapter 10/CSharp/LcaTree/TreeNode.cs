using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;
using System.Diagnostics;

namespace LcaTree
{
    public class TreeNode
    {
        public int Value = -1;
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
            if (parent != null) parent.Children.Add(this);
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
        public TreeNode FindLca(int value1, int value2)
        {
            bool contains1, contains2;
            return ContainsNodes(value1, value2,
                out contains1, out contains2);
        }

        // Find the LCA for the two nodes.
        public TreeNode ContainsNodes(int value1, int value2,
            out bool contains1, out bool contains2)
        {
            // See if this node contains either value.
            contains1 = (Value == value1);
            contains2 = (Value == value2);
            if (contains1 && contains2) return this;

            // See which children contain the values.
            foreach (TreeNode child in Children)
            {
                // Check this child.
                bool has1, has2;
                TreeNode lca = child.ContainsNodes(value1, value2,
                    out has1, out has2);

                // If we have found the LCA, return it.
                if (lca != null) return lca;

                // Update contains1 and contains2.
                if (has1) contains1 = true;
                if (has2) contains2 = true;

                // If has1 and has2 are both true, then this child
                // should contain the LCA so we shouldn't get here.
                Debug.Assert(!(has1 && has2),
                    $"Child subtree {child.Value} contains {value1} and {value2} but does not contain the LCA.");

                // If we found both values in different
                // children, then this is the LCA.
                if (contains1 && contains2) return this;
            }
            return null;
        }
    }
}
