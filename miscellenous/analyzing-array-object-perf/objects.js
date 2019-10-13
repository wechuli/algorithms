//We
const instructor = {
  firstName: "Kelly",
  isInstructor: true,
  favoriteNumbers: [1, 2, 3, 4]
};

instructor.hasOwnProperty("firstName");

for (prop in instructor) {
  console.log(prop);
}

console.log(Object.keys(instructor));
