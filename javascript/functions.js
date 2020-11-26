/* creating a js function*/
function hello() {
	const heading = document.querySelector("h1");
	if (heading.innerHTML === "Hello!") {
		heading.innerHTML = "Goodbye!";
  	} else {
		heading.innerHTML = "Hello!";
  	}
}

if (!localStorage.getItem('counter')){
	localStorage.setItem('counter', 0);
}

function count() {
	const text = document.querySelector("h2");
	let counter = localStorage.getItem('counter');
  	counter++;
	text.innerHTML = counter;
	localStorage.setItem('counter', counter);
  	// if (counter % 10 === 0) {
	// 	alert(`Count is now ${counter}`);
	// }
}

/* loads all contents before events */
document.addEventListener("DOMContentLoaded", () => {
	document.querySelector("h2").innerHTML = localStorage.getItem('counter');
	document.getElementById("counter").onclick = count;
	//setInterval(count, 1000);

	document.getElementById("greeter").onclick = hello;
	document.querySelector('form').onsubmit = function(){
		const name = document.querySelector("#name").value; 
		alert(`Hello ${name}`);
	};

	document.querySelector("select").onchange = function() {
		// 'this' always refers to the item that receieves the event
			document.querySelector("h1").style.color = this.value;
		};
});
