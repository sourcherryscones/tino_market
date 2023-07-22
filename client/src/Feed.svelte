<script>
    export let postdict = [];
    //[{'id': 8, 'title': 'The Great Gatsby', 'description': 'Stolen from an ALH classroom', 'condition': 'TRAUMATIZED'}]
    //import OldCard from './OldCard.svelte';
    function claimItem(bk){
        console.log('the id of this item is ' + bk['id']);
        const resp = fetch('./claim/' + bk['id'], {
            method: 'PUT',
            body: JSON.stringify(bk),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => {
            console.log(resp.json().then(data => {
                bk['is_claimed'] = data['is_claimed']
                bk['recip'] = data['recip']
                postdict=postdict
            }));
    });
    }
</script>


<main> <!--hi-->
    <div class="container">
    {#each postdict as book}
    <!--<OldCard bookitem={book} title={book['title']} description={book['description']} donor={book['donor']} claimed={book['is_claimed']} />-->
    <div class = "card">
        <h1>{book['title']}</h1>
        <h3>{book['description']}</h3>
        <h4>Posted by {book['donor']}</h4>
        <button disabled = {book['is_claimed']} on:click={claimItem(book)}>i want this!</button>
        {#if book['is_claimed'] == true}
            <h4>claimed by {book['recip']}</h4>
        {/if}
    </div>
    {/each}
    </div>
</main>

<style>
    .container{
        display:grid;
        grid-template-columns: 2;
    }

    .card{
        color:#27214D;
        border-radius:20px;
        padding: 10px;
        margin: 20px 0px;
    }

    .card h1{
        font-family: 'JetBrains Mono', monospace;
    }
</style>