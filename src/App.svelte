<script>
  let data;
  import { onMount } from 'svelte';
  import { element } from 'svelte/internal';

  import responses from '/Users/Harry/Documents/Current test/workingversion/output.json';

  let colour = "white";

  let searchQuery = "";

  let bookings = responses.result.event.bookings;

  $: filteredBookings = bookings.filter(
    (booking) =>
      booking.participant.crsid.toLowerCase().includes(searchQuery.toLowerCase())
  );

  function sayconfirm(crsid) {
    alert(` ${crsid} logged in`);
  }

  function handleSearchInput(event) {
    searchQuery = event.target.value;
  }

  async function removeRow(bookingId, crsid, status) {
    bookings = bookings.filter((booking) => booking.bookingId !== bookingId);

    sayconfirm(crsid);
  }
</script>

<h1>{responses.result.event.title}</h1>
<h2>Event aims:</h2>
<p>{responses.result.event.aims}</p>
<h3>Event Objectives:</h3>
<p>{responses.result.event.objectives}</p>

<input type="text" placeholder="Search by CRSID" bind:value={searchQuery} on:input={handleSearchInput} />

<table name="myTable">
  <thead>
    <tr>
      <th>CRS ID</th>
      <th>Booking Status</th>
      <th>Register</th>
    </tr>
  </thead>
  <tbody>
    {#each filteredBookings as response (response.bookingId)}
      <tr>
        <td>{response.participant.crsid}</td>
        <td>{response.status}</td>
        <td>
          <button
            style="background-color: {colour}"
            on:click={() => {
              console.log(response.participant.crsid);
              removeRow(response.bookingId, response.participant.crsid, response.status);
            }}
          >
            Log
          </button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table, th, td {
    border: 2px solid black;
    border-collapse: collapse;
    margin: auto;
  }
</style>
