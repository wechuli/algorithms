class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(value) {
    let newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  traverse() {
    let current = this.head;
    while (current) {
      console.log(current);
      current = current.next;
    }
  }
}

const myLinkedList = new LinkedList();

myLinkedList.push(new Node(52));
myLinkedList.push(new Node("hi there"));
myLinkedList.push(new Node([1, 2]));
myLinkedList.push(new Node(895.58));

console.log(myLinkedList);

myLinkedList.traverse();
