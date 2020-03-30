interface IListNode {
  val: any;
  next: IListNode | null;
}
interface ISinglyLinkedList {
  length: number;
  tail: IListNode | null;
  head: IListNode | null;
  //   insert(value: any, index: number): ISinglyLinkedList;
  push(value: any): ISinglyLinkedList;
  pop(): any;
}

class ListNode implements IListNode {
  val: any;
  next: IListNode | null = null;
  constructor(val: any) {
    this.val = val;
  }
}

class SinglyLinkedList implements ISinglyLinkedList {
  length: number = 0;
  tail: IListNode | null = null;
  head: IListNode | null = null;
  constructor() {}
  push(val: any): ISinglyLinkedList {
    const newNode = new ListNode(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else if (this.tail) {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }
  //   insert(val: any, index: number): ISinglyLinkedList {}
  pop(): any {}
  traverse() {
    let currentNode = this.head;
    while (currentNode) {
      console.log(currentNode.val);
      currentNode = currentNode.next;
    }
  }
}

const singleList = new SinglyLinkedList();
singleList.push("1");
singleList.push("2");
singleList.push("3");
singleList.push("4");
console.log(singleList.tail);
singleList.traverse();
