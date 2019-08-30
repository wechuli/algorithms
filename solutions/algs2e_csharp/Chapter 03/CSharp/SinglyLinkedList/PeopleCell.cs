﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SinglyLinkedList
{
    class PersonCell
    {
        public string Name;
        public PersonCell Next;

        // Insert a cell after this one.
        public void InsertAfter(string newName)
        {
            PersonCell newCell = new PersonCell();
            newCell.Name = newName;
            newCell.Next = this.Next;
            this.Next = newCell;
        }

        // Insert a cell after the indicated one.
        public void InsertAfter(string afterName, string newName)
        {
            // Find the target cell.
            PersonCell afterCell = FindCell(afterName);
            if (afterCell == null)
                throw new KeyNotFoundException("Item " +
                    afterName + " not found in list.");

            // Insert the new name after the one we found.
            afterCell.InsertAfter(newName);
        }

        // Delete the cell after this one.
        public void DeleteAfter()
        {
            PersonCell cell = this.Next;
            if (cell == null) return;
            this.Next = cell.Next;
            // free(cell);
        }

        // Delete the indicate cell.
        public void Delete(string name)
        {
            // Find the cell before the one to delete.
            PersonCell cell = this.FindCellBefore(name);
            if (cell == null)
                throw new KeyNotFoundException("Item " +
                    name + " not found in list.");

            // Delete the target cell.
            cell.DeleteAfter();
        }

        // Return the indicated cell.
        public PersonCell FindCell(string name)
        {
            for (PersonCell cell = this; ; cell = cell.Next)
            {
                if (cell == null) return null;
                if (cell.Name == name) return cell;
            }
        }

        // Return the cell before the indicated one.
        public PersonCell FindCellBefore(string name)
        {
            for (PersonCell cell = this; ; cell = cell.Next)
            {
                if (cell.Next == null) return null;
                if (cell.Next.Name == name) return cell;
            }
        }
    }
}
