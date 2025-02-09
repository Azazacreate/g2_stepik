const developer = {
    name: 'Michail',
    surname: 'Petrov',
    age: 30,
    skiils: ['Javascript', 'Typescript', 'CSS', 'HTML'],
    is__married: false
};
for (let prop in developer) {
    console.log(prop, developer[prop])
}