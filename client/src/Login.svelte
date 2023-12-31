<script>
    import { push } from "svelte-spa-router";
    import Card from "./Card.svelte"
    import Nav from './Nav.svelte'
    import { isloggedin } from "./stores";
    let username = '';
    let password = '';
    let showHint = false;
    let hintValue = '';

    let enter_key_is_down = false;

    function on_key_down(event){
        if (event.repeat) return;

        switch(event.key){
            case "Enter":
            enter_key_is_down = true;
            event.preventDefault();
            break;
        }

        if (enter_key_is_down){
            userLogin();
        }

    }

    function on_key_up(event){
        switch(event.key){
            case "Enter":
            enter_key_is_down = false;
            event.preventDefault();
            break;
        }

    }

    
    function userLogin(){
        const user = fetch('./login', {
            method: 'POST',
            body: JSON.stringify({'username': username, 'password': password}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let userFound = res['success'];
            if (userFound === true){
                username='';
                password='';
                isloggedin.set(true)
                push('/feed');
            } else{
                if (res['error'] == 'USER NOT FOUND'){
                    hintValue = "It doesn't look like that account exists; please register to continue!";
                } else if (res['error'] == 'INCORRECT PASSWORD'){
                    hintValue = "We don't remember that being your password; please try again!"
                } else {
                    hintValue = "Sorry, we couldn't log you in,. Try again?";
                }
                showHint=true;
            }
        }));
    }

    
</script>

<svelte:window
    on:keydown={on_key_down}
    on:keyup={on_key_up}
/>
<main class="container">
    <head>
    </head>
    <Nav/>
    <div class="login">
        <form>
            <h1>Log in!</h1>
            {#if showHint == true}
                <p class="errmess" style="color: #ff5e5e; font-weight: bold;">{hintValue}</p>
            {/if}
            <label>
                Username/email:
                <input type="text" bind:value={username}>
            </label>
            <label>
                Password:
                <input id = "pwfield" type="password" bind:value={password}>
            </label>
            <input class="btn" type="submit" id = "submitbtn" value="Let's go!" disabled={!(password && username)} on:click={() => {userLogin()}}>
            <small>Forgot your password? Reset it <a href="/#/forgot">here</a>!</small>
        </form>
    </div>    
        
</main>

