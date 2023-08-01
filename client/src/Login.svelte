<script>
    import { push } from "svelte-spa-router";

    let username = '';
    let password = '';
    let showHint = false;

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
        <input type="submit" value="Let's go!" on:click={() => {userLogin()}}>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your credentials were entered correctly!</small>
        {/if}
    </div>
</main>

