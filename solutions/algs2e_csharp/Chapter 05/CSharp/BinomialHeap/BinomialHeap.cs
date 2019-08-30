using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;

namespace BinomialHeap
{
    public class BinomialHeap
    {
        // A linked list of child trees.
        public BinomialNode RootSentinel =
            new BinomialNode(int.MinValue);

        // Find the root before the one with the smallest value.
        public BinomialNode FindRootBeforeSmallestValue()
        {
            BinomialNode bestPrev = RootSentinel;
            int bestValue = int.MaxValue;

            for (BinomialNode prev = RootSentinel;
                prev.NextSibling != null;
                prev = prev.NextSibling)
            {
                if (prev.NextSibling.Value < bestValue)
                {
                    bestPrev = prev;
                    bestValue = prev.NextSibling.Value;
                }
            }

            return bestPrev;
        }

        // Find the node before where this value should go.
        public BinomialNode FindNewRootPosition(BinomialNode newRoot)
        {
            BinomialNode prev = RootSentinel;
            while ((prev.NextSibling != null) &&
                (prev.NextSibling.Order < newRoot.Order))
            {
                prev = prev.NextSibling;
            }

            return prev;
        }

        // Add a new root in the proper position in the root list.
        public void AddRoot(BinomialNode newRoot)
        {
            // Find the root before the position
            // where the new one belongs.
            BinomialNode prev = FindNewRootPosition(newRoot);

            // Insert the new root after prev.
            newRoot.NextSibling = prev.NextSibling;
            prev.NextSibling = newRoot;
        }

        // Merge with another heap.
        public void MergeWithHeap(BinomialHeap heap2)
        {
            // Merge the heaps' root lists.
            BinomialNode mergedListSentinel =
                MergeRootLists(this, heap2);

            // Merge roots that have the same order.
            MergeRootsWithSameOrder(mergedListSentinel);

            // Save the new roots.
            RootSentinel = mergedListSentinel;
        }

        // Merge the two heaps' roots into one list in ascending order.
        // Return the sentinel for the merged list.
        public static BinomialNode MergeRootLists(BinomialHeap heap1, BinomialHeap heap2)
        {
            // Make a list to hold the merged roots.
            BinomialNode mergedListSentinel = new BinomialNode(int.MinValue);
            BinomialNode mergedListBottom = mergedListSentinel;

            // Remove the root list sentinels.
            heap1.RootSentinel = heap1.RootSentinel.NextSibling;
            heap2.RootSentinel = heap2.RootSentinel.NextSibling;

            // Merge the two heaps' roots into one list in ascending order.
            while ((heap1.RootSentinel != null) &&
                   (heap2.RootSentinel != null))
            {
                // See which root has the smaller order.
                BinomialHeap moveHeap = null;
                if (heap1.RootSentinel.Order <= heap2.RootSentinel.Order)
                    moveHeap = heap1;
                else
                    moveHeap = heap2;

                // Move the selected root.
                BinomialNode moveRoot = moveHeap.RootSentinel;
                moveHeap.RootSentinel = moveRoot.NextSibling;
                mergedListBottom.NextSibling = moveRoot;
                mergedListBottom = moveRoot;
                mergedListBottom.NextSibling = null;
            }

            // Add any remaining roots.
            if (heap1.RootSentinel != null)
            {
                mergedListBottom.NextSibling = heap1.RootSentinel;
                heap1.RootSentinel = null;
            }
            else if (heap2.RootSentinel != null)
            {
                mergedListBottom.NextSibling = heap2.RootSentinel;
                heap2.RootSentinel = null;
            }

            // Return the merged list sentinel.
            return mergedListSentinel;
        }

        // Sift through the list and merge roots with the same order.
        private static void MergeRootsWithSameOrder(BinomialNode listSentinel)
        {
            BinomialNode prev = listSentinel;
            BinomialNode node = prev.NextSibling;
            BinomialNode next = null;
            if (node != null) next = node.NextSibling;

            while (next != null)
            {
                // See if we need to merge node and next.
                if (node.Order != next.Order)
                {
                    // Move to consider the next pair.
                    prev = node;
                    node = next;
                    next = next.NextSibling;
                }
                else
                {
                    // Remove them from the list.
                    prev.NextSibling = next.NextSibling;

                    // Merge node and next.
                    node = BinomialNode.MergeTrees(node, next);

                    // Insert the new root where the old ones were.
                    next = prev.NextSibling;
                    node.NextSibling = next;
                    prev.NextSibling = node;

                    // If we have three matches in a row,
                    // skip the first one so we can merge
                    // the other two in the next round.
                    // Otherwise consider node and next
                    // again in the next round.
                    if ((next != null) &&
                        (node.Order == next.Order) &&
                        (next.NextSibling != null) &&
                        (node.Order == next.NextSibling.Order))
                    {
                        prev = node;
                        node = next;
                        next = next.NextSibling;
                    }
                }
            }
        }

        // Add a value to the heap.
        public void Enqueue(int value)
        {
            // If this heap is empty, just add the value.
            if (RootSentinel.NextSibling == null)
            {
                RootSentinel.NextSibling = new BinomialNode(value);
            }
            else
            {
                // Make a new heap containing the new value.
                BinomialHeap newHeap = new BinomialHeap();
                newHeap.Enqueue(value);

                // Merge with the new heap.
                MergeWithHeap(newHeap);
            }
        }

        // Remove the smallest value from the heap.
        public int Dequeue()
        {
            if (RootSentinel.NextSibling == null)
                throw new InvalidOperationException("The heap is empty.");

            // Find the root with the smallest value.
            BinomialNode prev = FindRootBeforeSmallestValue();

            // Remove the tree containing the value from our list.
            BinomialNode root = prev.NextSibling;
            prev.NextSibling = root.NextSibling;

            // Make a new heap containing the
            // removed tree's subtrees.
            BinomialHeap newHeap = new BinomialHeap();
            BinomialNode subtree = root.FirstChild;
            while (subtree != null)
            {
                // Add this subtree to the top of the new heap's root list.
                BinomialNode next = subtree.NextSibling;
                subtree.NextSibling = newHeap.RootSentinel.NextSibling;
                newHeap.RootSentinel.NextSibling = subtree;
                subtree = next;
            }

            // Merge with the new heap.
            MergeWithHeap(newHeap);

            // Return the removed root's value.
            return root.Value;
        }

        // Display the heap's trees in a TreeView control.
        public void AddToTreeView(TreeNodeCollection nodes)
        {
            TreeNode heapNode = nodes.Add("Heap");

            // Add our children to the TreeView.
            for (BinomialNode root = RootSentinel.NextSibling;
                root != null;
                root = root.NextSibling)
            {
                root.AddToTreeView(heapNode.Nodes);
            }
        }
    }
}
