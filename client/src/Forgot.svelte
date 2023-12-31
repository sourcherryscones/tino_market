<script>
    import {push} from 'svelte-spa-router'
    import Nav from './Nav.svelte';
    let showHint = false;
    let email = '';
    let hint = '';

    //on submit, if in database, then proceed, else flash message to go sign up :)

    function checkResetEmail(){
        const checkemail = fetch('./emailver', {
            method:'POST',
            body: JSON.stringify({'email': email}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let isindb = res['isindb']
            if (isindb){
                console.log("confirmed im in the db")
                    let emval = email;
                    push('/verify/'+emval+'/pwreset')
            } else {
                showHint = true;
                hint="Don't have an account? Sign up <a href='/#/register'>here</a> to get started.";
            }
        }))
    }

</script>

<main>
    <Nav/>
    <div class="container">
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

            <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        </head>
        <div class="verify">
            <h1>Forgot your password?</h1>
            <p>That's alright :) verify your email and we'll send you a reset link!</p>
            <label>
                Email:
                <input type="email" bind:value={email}>
            </label>
            <input class="btn" type="submit" value="Let's go!" on:click={() => {checkResetEmail()}}>
            <br>
            {#if (showHint == true)}
                <small class="info">{hint}</small>
            {/if}
        </div>
    </div>
</main>