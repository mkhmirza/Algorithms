using System;

namespace bst
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] data = new int[]{ 5, 6, 3, 1, 2, 4};
            BinarySearchTree bst = new BinarySearchTree(data);
            bst.BuildBst();
            bst.PrintInOrder();
        }
    }
}
