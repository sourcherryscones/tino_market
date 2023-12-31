<script>
    let codeval = 0;
    let hint='';
    import {push} from 'svelte-spa-router'
    export let params = {};
    import Nav from './Nav.svelte';
    let showHint = false;

    //go from FE register to backend (create user, unverified, with code)
    // now from backend, send email with "https://tinomarket.org/#/verify/code?=john.doe@gmail.com"

    function verifyCode(){
        const verifycode = fetch('./verify', {
            method:'POST',
            body: JSON.stringify({'email': params.emailval, 'code': codeval, 'from': params.from}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let isverified = res['verified']
            if (isverified){
                codeval = 0;
                if (params.from == "newuser"){
                    push('/feed');
                } else{
                    push('/pwreset/'+params.emailval)
                }
            } else {
                showHint = true;
                if (res['error'] == 'WRONG CODE'){
                    hint = 'Hmm, that code looks wrong -- try again?';
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
            <h1>Verify email</h1>
            <label>
                Code:
                <input type="number" bind:value={codeval}>
            </label>
            <input class="btn" type="submit" value="Let's go!" on:click={() => {verifyCode()}}>
            <br>
            {#if (showHint == true)}
                <small class="info">{hint}</small>
            {/if}
        </div>
    </div>
</main>