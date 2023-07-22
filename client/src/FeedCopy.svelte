<script>
    export let postdict = [];
    //[{'id': 8, 'title': 'The Great Gatsby', 'description': 'Stolen from an ALH classroom', 'condition': 'TRAUMATIZED'}]
    import Card from './Card.svelte';

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
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    {#each postdict as book}
    <Card bookitem={book} title={book['title']} description={book['description']} donor={book['donor']} claimed={book['is_claimed']} />
    <!--<div class = "card">
        <h1>{book['title']}</h1>
        <p>{book['description']}</p>
        <h4>Posted by {book['donor']}</h4>
        <button disabled = {book['is_claimed']} on:click={claimItem(book)}>{book['is_claimed'] ? 'X' : '+'}</button>
        {#if book['is_claimed'] == true}
            <p class="claimedby">(claimed by {book['recip']})</p>
        {/if}
    </div>-->
    {/each}
</main>

<style>
    main {
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: auto;
		gap: 20px;
		max-width: 960px;
		margin: auto;
	}
	@media (min-width: 600px) {
		main {
			grid-template-columns: 1fr 1fr 1fr;
		}
		div {
			min-height: auto;
		}
	}

    .card{
        color:#27214D;
        border-radius:20px;
        padding: 10px;
        margin: 0px;
        border: 2px solid;
        font-family: 'Barlow', sans-serif;
    }

    .card h1{
        font-family: 'JetBrains Mono', monospace;
        /*background-color: rgb(77, 148, 162);*/
    }

    .card p{
        min-height: 20px;
    }

    button{
        background-color: #FFF2E7;
        color:#f08626;
        border-radius: 100px;
        font-size: 30px;
        font-weight: 700;
        height:40px;
        padding:0px 40px;
        transition:0.4s;
    }

    button:hover{
        background-color: rgb(255, 209, 172);
    }

    button:disabled{
        background-color: rgb(198, 176, 149);
        color:#9a5718;
    }

    .claimedby{
        margin:0px;
    }
</style>