using System;

namespace  bst
{
    public class BinarySearchTree
    {
        private Node root;
        private int[] data; 
        
        public BinarySearchTree() { }
        
        public BinarySearchTree(int[] data)
        {
            this.data = data;
            // init root as the first element of the data array 
            this.root = returnNode(this.data[0]);
        }

        public Node returnNode(int value)
        {
            Node  node  = new Node();
            node.Key = value;
            node.Left = null;
            node.Right = null;
            node.Parent = null;
            return node; 
        }

        public void InsertNode(int value)
        {
            Node node = returnNode(value);
            Node x = this.root;
            Node y = null;

            while(x != null)
            {
                y = x;
                if(node.Key < x.Key){
                    x = x.Left;
                } else {
                    x = x.Right;
                }
            }

            node.Parent = y;
            if (y == null){
                this.root = node;
            } else if (node.Key < y.Key){
                y.Left = node;
            } else if (node.Key > y.Key){
                y.Right = node;
            }

        }

        public void BuildBst()
        {
            for(int i =0;i < this.data.Length; i++){
                InsertNode(this.data[i]);
            }
        }

        public void PrintInOrder()
        {
            InOrder(this.root);
        }

        public Node Find(int value)
        {
            Node node = this.root;
            while ((node != null) && value != node.Key ){
                if (value < node.Key){
                    node = node.Left;
                } else {
                    node = node.Right;
                }
            }   

            return node;
        }


        public bool IsLeft(int value)
        {
            Node node = Find(value);
            if (node != null && node.Parent.Key > value){
                return true;
            } else {
                return false;
            }
        }
        
        public bool IsRight(int value)
        {
            Node node = Find(value);
            if (node != null && node.Parent.Key < value){
                return true;
            } else {
                return false;
            }
        }

        private void InOrder(Node node)
        {
            if(node != null){
                InOrder(node.Left);
                Console.WriteLine(node.Key);
                InOrder(node.Right);
            }
        }

    }
}