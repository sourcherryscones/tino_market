<script>
    import { push } from "svelte-spa-router";
    import Nav from './Nav.svelte'
    let username = '';
    let grade = 9;
    let email = '';
    let password = '';
    let passwordconf = ''
    let indicator=false;
    let conftext = '';
    let hidden = false;
    let showHint = false;
    let hint = '';
    function register(){
        console.log("button clicked!")
        console.log("is the email from fuhsd??")
        console.log(email.endsWith('fuhsd.org'))
        const reg = fetch('./reg', {
            method:'POST',
            body: JSON.stringify({'username': username, 'email': email,'password': password, 'pwconf': passwordconf, 'grade': grade}),
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
                push('/verify/'+email+'/newuser');
            } else {
                showHint = true;
                if (res['error'] == 'USER ALREADY EXISTS'){
                    hint = 'Looks like that email/username is already taken; please log in instead or use a different one!';
                } else {
                    hint = 'Please check to make sure that your credentials are valid! You must use your FUHSD email, be between 9th and 12th grade, and enter a valid password :)';
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
        {#if hidden==false}
        <div class="register">
            <h1>Register</h1>
            <label>
                Username:
                <input type="text" bind:value={username}>
            </label>
            <label>
                Email:
                <input type="text" bind:value={email}>
            </label>
            <label>
                Grade:
                <input type="number" bind:value={grade}>
            </label>
            <label>
                Password:
                <input type="password" bind:value={password}>
            </label>
            <label>
                Confirm password:
                <input type="password" bind:value={passwordconf}>
            </label>
            <input class="btn" type="submit" value="Let's go!" disabled = {!(password === passwordconf && password != '' && grade > 8 && grade < 13 && email.endsWith('fuhsd.org'))} on:click={() => {register()}}>
            <br>
            {#if (showHint == true)}
                <small class="info">{hint}</small>
            {/if}
        </div>
        {/if}
    </div>
</main>

