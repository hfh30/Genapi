
<script>
    let data;
  import { onMount } from 'svelte'
  import responses from '/Users/Harry/Documents/Current test/workingversion/output.json'
    import { element } from 'svelte/internal';

  // A variable to store the current colour of the button
  let colour = "white";

  function sayconfirm() {
    alert("User logged in");
  }
  
</script>

<h1>{responses.result.event.title}</h1>
<h2>Event aims:</h2>
<p>{responses.result.event.aims}</p>
<h3>Event Objectives:</h3>
<p>{responses.result.event.objectives}</p>

 

 <table name =myTable>
  <thead>
    <tr>
      <th>CRSdasdasdyID</th>
      <th>Booking Status</th>
      <th>Register</th>
    </tr>
  </thead>
  <tbody>
    {#each responses.result.event.bookings as response (response.bookingId)}
    <tr>
      <td>{response.participant.crsid}</td>
      <td>{response.status}</td>
  
      <td>
        <button style="background-color: {colour}" on:click={() => {console.log(response.participant.crsid);sayconfirm();}}>Log</button>
    
      </td>
    
      
    </tr>
    {/each}
  </tbody>
</table>

<head>
  <style>
  table, th, td {
    border: 2px solid black;
    border-collapse: collapse;
    margin: auto
  }
   /* Styling for the table margin auto makes it center */
  </style>


  </head>