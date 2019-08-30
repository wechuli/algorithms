using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;

namespace BinomialHeap
{
    public class BinomialNode
    {
        // The sub-tree's order.
        public int Order = 0;

        // This node's value.
        public int Value = int.MinValue;

        // References to other nodes.
        public BinomialNode Parent = null;
        public BinomialNode NextSibling = null;
        public BinomialNode FirstChild = null;

        // Intializing constructor.
        public BinomialNode(int value)
        {
            Value = value;
        }

        // Insert a new child node at the top of the child list.
        public void InsertChild(BinomialNode child)
        {
            child.NextSibling = FirstChild;
            FirstChild = child;
        }

        // Merge two binomial trees of the same size.
        public static BinomialNode MergeTrees(BinomialNode root1, BinomialNode root2)
        {
            // Ensure that root1 <= root2.
            if (root2.Value < root1.Value)
            {
                // Swap them.
                BinomialNode temp = root1;
                root1 = root2;
                root2 = temp;
            }

            // Make root2 a sub-tree of root1.
            root2.Parent = root1;
            root2.NextSibling = root1.FirstChild;
            root1.FirstChild = root2;
            root1.NextSibling = null;

            // The new tree has one greater order.
            root1.Order++;

            // Return the new root.
            return root1;
        }

        // Display the tree in a TreeView control.
        public void AddToTreeView(TreeNodeCollection nodes)
        {
            // Add our value to the TreeView.
            TreeNode ourNode = nodes.Add(ToString());

            // Recursively add our children to the TreeView.
            for (BinomialNode child = FirstChild;
                child != null;
                child = child.NextSibling)
            {
                child.AddToTreeView(ourNode.Nodes);
            }
        }

        // Display a linked list's values.
        public string ToListString()
        {
            string txt = ToString();
            for (BinomialNode node = this.NextSibling;
                node != null;
                node = node.NextSibling)
                    txt += $" -> {node.ToString()}";

            return txt;
        }

        // Set the sub-tree's order.
        public void SetOrder()
        {
            Order = 0;
            if (FirstChild == null) return;

            // Higher orders.
            for (BinomialNode child = FirstChild;
                child != null;
                child = child.NextSibling)
            {
                child.SetOrder();
                if (Order < child.Order) Order = child.Order;
            }
            Order++;
        }

        public override string ToString()
        {
            return $"(V={Value}, O={Order})";
        }
    }
}
