<script>
	import responses from './assets/responses.json'

  </script>
<!-- svelte-ignore a11y-missing-attribute -->
  {#each responses.result.event.bookings as response (response.bookingId)}
	<p>{response.participant.crsid.toString()}</p>


  {/each}