<script>
    //[{'id': 8, 'title': 'The Great Gatsby', 'description': 'Stolen from an ALH classroom', 'condition': 'TRAUMATIZED'}]

    export let es = '';
    export let pes = '';
    export let indicator=false;
    let hidden = false;
    let showHint = false;
    function userLogin(){
        const user = fetch('./login', {
            method: 'POST',
            body: JSON.stringify({'username': es, 'password': pes}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let userFound = res['success'];
            if (userFound === true){
                hidden=true;
                indicator=true;
            } else{
                showHint=true;
            }
            //console.log("RES SUCCESS IS " + res['success']);
            //console.log("TYPE IS " + typeof(res['success']));
        }));
    }
</script>


<main> <!--hi-->
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    {#if hidden==false}
    <div class="login">
        <h1>Log in</h1>
        <input type="text" bind:value={es}>
        <input type="password" bind:value={pes}>
        <input type="submit" on:click={() => {userLogin()}}>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your credentials were entered correctly!</small>
        {/if}
    </div>
    {/if}
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
            text-align: left;
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

    .errmess{
        color:#f57272;
        font-weight: bold;
    }
</style>