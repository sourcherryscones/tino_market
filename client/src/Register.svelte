<script>
    import { push } from "svelte-spa-router";

    export let username = '';
    export let grade = 0;
    export let password = '';
    export let passwordconf = ''
    export let indicator=false;
    let conftext = '';
    let hidden = false;
    let showHint = false;
    function register(){
        const reg = fetch('./createuser', {
            method:'POST',
            body: JSON.stringify({'username': username, 'password': password, 'grade': grade}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let isRegistered = res['registered']
            if (isRegistered){
                username = '';
                grade = 0;
                password = '';
                passwordconf = '';
                push('/');
            } else {
                showHint = true;
            }
        }))
    }
</script>


<main>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    {#if hidden==false}
    <div class="register">
        
        <h1>Register</h1>
        <input type="text" bind:value={username}>
        <input type="number" bind:value={grade}>
        <input type="password" bind:value={password}>
        <input type="password" bind:value={passwordconf}>
        <input type="submit" disabled = {!(password === passwordconf && password != '' && grade > 8 && grade < 13)} on:click={() => {register()}}>
        <br>
        <small class="info">Please check to make sure that your credentials are valid! You must be between 9th and 12th grade and enter a valid password :)</small>
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

    .info{
        color:#F08626;
        font-weight: bold;
    }
</style>