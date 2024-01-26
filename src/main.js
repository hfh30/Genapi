
import { get } from 'svelte/store';
import App from './App.svelte';

//let url = 'https://www.training.cam.ac.uk/api/v1/event/3732817?fetch=bookings&format=json';
//let username = 'hfh30';
//let password = 'QZrxgTgR7HK5b8hyf3279F3C4xTfXPft';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});
var table = document.getElementById("myTable");
var row = table.rows[0];
for (var i = 0; i < row.cells.length; i++) {
  console.log("Row = " + row.rowIndex + " Cell = " + row.cells[i].cellIndex + " Value = " + row.cells[i].innerText);
}