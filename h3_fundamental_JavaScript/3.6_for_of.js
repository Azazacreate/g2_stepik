const developer = {
    name: 'Michail',
    surname: 'Petrov',
    age: 30,
    skiils: ['Javascript', 'Typescript', 'CSS', 'HTML'],
    is__married: false,

    // way-1
    add__age: function() {},

    // way-2:более-современный
    add__age2() {
        this.age++;       // context
        console.log(this)
    },
    get__married() {this.is__married = true;},
    get__divorced() {this.is__married = false;},
};
developer.add__age2()


// proto