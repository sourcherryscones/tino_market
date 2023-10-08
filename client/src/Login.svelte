<script>
    import { push } from "svelte-spa-router";
    import Card from "./Card.svelte"
    import Nav from './Nav.svelte'
    import { isloggedin } from "./stores";
    let username = '';
    let password = '';
    let showHint = false;
    let showNotFound = false;
    //TO BE DELETED
    let bk = {"title": "The Greatest of Gatsbies", "description": "ALH required reading, pretty good condition", "condition": "GOOD"};
    let bkarr = [];
    for (let i=0; i < 10; i++){
        bkarr.push(bk);
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
                    showNotFound = true;
                }
                showHint=true;
            }
        }));
    }
</script>


<main class="container">
    <head>
    </head>
    <Nav/>
    <div class="login">
        
        <h1>Log in!</h1>
        {#if showNotFound == true}
            <p class="errmess" style="color: #ff5e5e; font-weight: bold;">It doesn't look like that account exists; please <a href="/#/register">sign up</a> to continue!</p>
        {/if}
        <label>
            Username:
            <input type="text" bind:value={username}>
        </label>
        <label>
            Password:
            <input type="password" bind:value={password}>
        </label>
        <input class="btn" type="submit" value="Let's go!" disabled={!(password && username)} on:click={() => {userLogin()}}>
        <small>Don't have an account? Sign up <a href="/#/register">here</a>!</small>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your credentials were entered correctly!</small>
        {/if}
    </div>
    
        
</main>

