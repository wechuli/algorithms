class Student {
  private firstName: string;
  private lastName: string;
  private year: Date;
  private absenceLimit: number = 0;
  private scores: number[] = [];

  constructor(firstName: string, lastName: string, year: Date) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.year = year;
  }

  get dateOfReg(): Date {
    return this.year;
  }
  fullName(): string {
    return `${this.firstName},${this.lastName}`;
  }
  markLate(): string {
    this.absenceLimit += 1;
    return `${this.fullName()} has been late ${this.absenceLimit} times`;
  }
  addScore(score: number): void {
    this.scores.push(score);
  }
  calculateAverage(): number {
    let sum = this.scores.reduce(function(a, b) {
      return a + b;
    });
    return sum / this.scores.length;
  }

  static sayHello(): void {
    console.log("I am a static method");
  }
}

const student = new Student("Paul", "Wechuli", new Date("12/11/2015"));

console.log(student.dateOfReg);
console.log(student.fullName());
console.log(student.markLate());
student.addScore(58.6);
student.addScore(78);
student.addScore(12);
console.log(student.calculateAverage());
Student.sayHello();
