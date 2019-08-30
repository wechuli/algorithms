using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace DrawTree
{
    public class BinaryNode
    {
        public string Name;
        public BinaryNode LeftChild, RightChild;

        public BinaryNode(string name)
        {
            Name = name;
        }

        #region Drawing Methods

        // Drawing parameters.
        private const int NodeRadius = 10;
        private const int XSpacing = 20;
        private const int YSpacing = 20;
        private Point Center;
        private Rectangle SubtreeRect;

        // Position the node.
        public void PositionSubtree(int xmin, int ymin)
        {
            // Set ymax to the bottom of this node.
            int ymax = ymin + 2 * NodeRadius;
            int xmax = xmin;

            // See if the node has any children.
            if ((LeftChild == null) && (RightChild == null))
            {
                // There are no children. Put the node here.
                xmax += 2 * NodeRadius;
                SubtreeRect = new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
            }
            else
            {
                ymax += YSpacing;

                // Position the left subtree.
                int subtreeBottom = ymax;

                if (LeftChild != null)
                {
                    LeftChild.PositionSubtree(xmax, ymax);

                    // Update xmax to allow room for the left subtree.
                    xmax = LeftChild.SubtreeRect.Right;

                    // If there is also a right child, allow room between them.
                    if (RightChild != null)
                        xmax += XSpacing;

                    // Update the subtree bottom.
                    subtreeBottom = LeftChild.SubtreeRect.Bottom;
                }

                // Position the right subtree.
                if (RightChild != null)
                {
                    RightChild.PositionSubtree(xmax, ymax);

                    // Update xmax.
                    xmax = RightChild.SubtreeRect.Right;

                    // Update the subtree bottom.
                    if (RightChild.SubtreeRect.Bottom > subtreeBottom)
                        subtreeBottom = RightChild.SubtreeRect.Bottom;
                }

                // Position this node centered over the subtrees.
                ymax = subtreeBottom;
                SubtreeRect = new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
            }

            // Position the node.
            int cx = (SubtreeRect.Left + SubtreeRect.Right) / 2;
            int cy = ymin + NodeRadius;
            Center = new Point(cx, cy);
        }

        // Draw the subtree's links.
        public void DrawSubtreeLinks(Graphics gr, Pen pen)
        {
            if (LeftChild != null)
            {
                LeftChild.DrawSubtreeLinks(gr, pen);
                gr.DrawLine(pen, Center, LeftChild.Center);
            }
            if (RightChild != null)
            {
                RightChild.DrawSubtreeLinks(gr, pen);
                gr.DrawLine(pen, Center, RightChild.Center);
            }

            // Outline the subtree for debugging.
            //gr.DrawRectangle(Pens.Red, SubtreeRect);
        }

        // Draw the subtree's nodes.
        public void DrawSubtreeNodes(Graphics gr, Font font, Brush fgBrush, Brush bgBrush, Pen pen)
        {
            // Draw the node.
            Rectangle rect = new Rectangle(
                Center.X - NodeRadius, Center.Y - NodeRadius,
                2 * NodeRadius, 2 * NodeRadius);
            gr.FillEllipse(bgBrush, rect);
            gr.DrawEllipse(pen, rect);
            using (StringFormat format = new StringFormat())
            {
                format.Alignment = StringAlignment.Center;
                format.LineAlignment = StringAlignment.Center;
                gr.DrawString(Name, font, fgBrush, rect, format);
            }

            // Draw the descendants' nodes.
            if (LeftChild != null) LeftChild.DrawSubtreeNodes(gr, font, fgBrush, bgBrush, pen);
            if (RightChild != null) RightChild.DrawSubtreeNodes(gr, font, fgBrush, bgBrush, pen);
        }

        #endregion Drawing Methods

    }
}
