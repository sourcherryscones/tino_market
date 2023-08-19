<script>
    import { push } from "svelte-spa-router";
    import Card from "./Card.svelte"
    let username = '';
    let password = '';
    let showHint = false;
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
                push('/feed');
            } else{
                showHint=true;
            }
        }));
    }
</script>


<main class="container">
    <head>
    </head>
    <div class="login">
        
        <h1>Log in!</h1>
        <label>
            Username:
            <input type="text" bind:value={username}>
        </label>
        <label>
            Password:
            <input type="password" bind:value={password}>
        </label>
        <input class="btn" type="submit" value="Let's go!" disabled={!(password && username)} on:click={() => {userLogin()}}>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your credentials were entered correctly!</small>
        {/if}
    </div>
    
        
</main>

