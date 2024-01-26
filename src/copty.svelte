<script>
  const postData = {
    userId: '',
    title: '',
    body: ''
  }

  function formHandler(event) {
    event.preventDefault()

    fetch('https://jsonplaceholder.typicode.com/posts/',{
      method:  'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_id: userId,
        title:   title,
        body:    body
      })
    })
      .then(response => response.json())
      .then(result => console.log(result))
  }
</script>

<section>
  <form>
    <div>
      <label for="userId">UserID:</label>
      <input type="text" id="userId" bind:value={postData.userId}>
    </div>
    <div>
      <label for="title">Title: </label>
      <input type="text" id="title" bind:value={postData.title}>
    </div>
    <div>
      <label for="body">Body: </label>
      <textarea id="body" rows="6" cols="22" bind:value={postData.body}></textarea>
    </div>
    <button on:click="{formHandler}">Create Post</button>
  </form>
</section>

<style>
  section{height:100vh;display:grid;justify-items:center;padding-top:40px}
  div{margin:24px auto}
  label{font-weight:bolder;display:block;margin-bottom:4px}
</style>