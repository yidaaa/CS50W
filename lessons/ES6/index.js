// VAR, CONST, LET
    // when you declare var inside a loop, it still can be accessed out of the loop
    function sayHello() {
        for ( var i=0; i<5; i++) {
            print(i)
        }
        console.log(i)
    }

    // let and const are within blocks only
    // const are read-only, cannot be reassigned
    function sayHello() {
        for ( let i=0; i<5; i++) {
            print(i)
        }
        console.log(i)
    }

// FUNCTIONS are js objects
    // simpler ways to create methods inside an object
    const person = {
        name: "Mosh",
        walk: function() {
            console.log(this);
        },
        talk() {
            console.log(this);
        }
    };

    // accessing values in 2 ways
    const targetMember= 'name';
    person[targetMember.value]='John';

    person.name = "John";

    // 'this' returns the reference to the current object if you call a function to an object
    person.talk();

    // if you call 'this' as a stand alone object, it calls the window object instead
    // if you call it in strict mode, it will return undefined
    const walk = person.walk;
    walk();

    // to fix this, bind the object, create a new talk function that binds the person object
    const talk = person.talk.bind(person);
    talk();

// ARROW FUNCTIONS
    // arrow functions dont rebind 'this' keyword
    const square = (number) => {
        return number*number
    }

    const jobs = [
        { id: 1, isActive: true },
        { id: 2, isActive: true },
        { id: 3, isActive: false },
    ];
    const activeJobs = jobs.filter((job) => job.isActive);

// MAP function, returns array
    const colors = ['red', 'green', 'blue'];
    const items = colors.map( color => `<li>${color}</li>` )

// DESTRUCTURING 
    const address = {
        street: '',
        city: '',
        country: ''
    };

    const street = address.street;
    const city = address.city;
    const country = address.country;
    // this is an easier way to write the equivalent
    const { street, city, country } = address; 
    // if we want to use alias, define new constant st with value street
    const { street: st } = address; 

// SPREAD operator ...
    const first = [1, 2, 3];
    const second = [5, 6, 7];

    const one = { name: 'Mosh' };
    const two = { job: 'Instructor'};
    
    // cloning 
    const cloneArr = [...first];
    const cloneObj = {...one};
    // inserting/combining 
    const combinedArr = [...first, 4, ...second, 8];
    const combinedObj = {...first, ...second, age: 23 };

// CLASSES and MODULES

    // --- (person.js)---
    export class Person {
        // just like init
        constructor(name) {
            this.name = name;
        }

        walk() {
            console.log("walk");
        }
    }

    // ---(teacher.js)---
    // inheritance
    import { Person } from './person'; 

    // named exports can be imported in another file
    export function promote() {}
    export default class Teacher extends Person {
        constructor(name, degree) {
            super(name);
            this.degree = degree;
        }
        teach() {
            console.log("teach");
        }
    }

    // ---(index.js)---
    import Teacher, { promote } from './teacher' 
    // default exports --> import ... from ...
    // named exports --> import {...} from ...
    const teacher = new Teacher('Mosh', 'FoSHons');
    teacher.teach();


    
