<script>
    import { push } from "svelte-spa-router";

    let title = '';
    let description = '';
    let condition = '';
    let showHint = false;
    

    function addPost(){
        const post = fetch('./postsquared', {
            method: 'POST',
            body: JSON.stringify({'title': title, 'description': description, 'condition': condition}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let id = res['id'];
            if (id){
                title='';
                description='';
                condition = '';
                push('/feed');
            } else{
                showHint=true;
            }
        }));
    }
</script>


<main>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    <div class="post">
        <h1>Create new post</h1>
        <input type="text" bind:value={title}>
        <input type="text" bind:value={description}>
        <select bind:value={condition}>
            <option value="GOOD">Good</option>
            <option value="OK">OK</option>
        </select>
        <input type="submit" on:click={() => {addPost()}}>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your post has all of the necessary elements!</small>
        {/if}
    </div>
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

    .login{
        margin: auto;
    }

    h1{
        color: #27214D;
        font-size: 40px;
        font-family: 'Barlow', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
    }

    .errmess{
        color:#f57272;
        font-weight: bold;
    }
</style>