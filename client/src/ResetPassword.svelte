<script>
    let codeval = 0;
    let hint='';
    let password='';
    let passwordconf='';
    import {push} from 'svelte-spa-router'
    export let params = {};
    import Nav from './Nav.svelte';
    let showHint = false;

    //go from FE register to backend (create user, unverified, with code)
    // now from backend, send email with "https://tinomarket.org/#/verify/code?=john.doe@gmail.com"

    function resetPassword(){
        const resetpw = fetch('./reset', {
            method:'POST',
            body: JSON.stringify({'email': params.emailval, 'newpw': passwordconf}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let wentThrough = res['successful_update']
            if (wentThrough){
                password = '';
                passwordconf = '';
                push('/login')
            } else {
                showHint = true;
                if (res['error'] == 'PASSWORDS DO NOT MATCH'){
                    hint = 'Passwords do not match D:';
                } else {
                    hint = 'lmao something is wrong';
                }
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
            <h1>Reset your password!</h1>
            <label>
                Password:
                <input type="password" bind:value={password}>
            </label>
            <label>
                Confirm password:
                <input type="password" bind:value={passwordconf}>
            </label>
            <input class="btn" type="submit" value="Let's go!" on:click={() => {resetPassword()}}>
            <br>
            {#if (showHint == true)}
                <small class="info">{hint}</small>
            {/if}
        </div>
    </div>
</main>