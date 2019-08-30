using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;

namespace DrawTree3
{
    public class NAryNode
    {
        public string Name;
        public List<NAryNode> Children = new List<NAryNode>();

        public NAryNode(string name)
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
            if (Children.Count == 0)
            {
                // There are no children. Put the node here.
                xmax += 2 * NodeRadius;
                SubtreeRect = new Rectangle(xmin, ymin, xmax - xmin, ymax - ymin);
            }
            else
            {
                ymax += YSpacing;

                // Position the child subtrees.
                int subtreeBottom = ymax;
                for (int i = 0; i < Children.Count; i++)
                {
                    // Position this child subtree.
                    NAryNode child = Children[i];
                    child.PositionSubtree(xmax, ymax);

                    // Update xmax to allow room for the subtree.
                    xmax = child.SubtreeRect.Right;

                    // Update the subtree bottom.
                    if (child.SubtreeRect.Bottom > subtreeBottom)
                        subtreeBottom = child.SubtreeRect.Bottom;

                    // If this is not the last child, add horizontal
                    // space before the next child subtree.
                    if (i < Children.Count - 1) xmax += XSpacing;
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
            foreach (NAryNode child in Children)
            {
                child.DrawSubtreeLinks(gr, pen);
                gr.DrawLine(pen, Center, child.Center);
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
            foreach (NAryNode child in Children)
                child.DrawSubtreeNodes(gr, font, fgBrush, bgBrush, pen);
        }

        #endregion Drawing Methods

    }
}
