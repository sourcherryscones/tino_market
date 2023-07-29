<script>
    export let es = '';
    export let pes = '';
    export let indicator=false;
    let hidden = false;
    let showHint = false;
    let showLogout = false;
    function logout(){
        const lo = fetch('./logout', {
            method:'POST',
            body: JSON.stringify({'logout': true}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let loggedOut = res['logoutsuccessful'];
            if (loggedOut == true){
                hidden=false;
                indicator=false
                showLogout = false;
            }
        }))
    }

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
                showLogout = true;
                es=''
                pes='';
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
    {#if showLogout == true}
        <button on:click={logout}>LOG OUT</button>
    {/if}
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