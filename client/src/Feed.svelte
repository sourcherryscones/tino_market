<script>
    //export let postdict = [];
    let booklist = [];
    import {link, push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import Card from './Card.svelte';
    let showLogout = true;

    onMount(async () => {
        const res = await fetch('./allposts');
        const resp = await res.json();
        booklist = resp;
    });

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
                showLogout = false;
                push('/login')
            }
        }))
    }
</script>


<main>
    <head>
    </head>
    <div class="grid">
        {#each booklist as book}
            <Card book={book} />
        {/each}
    </div>
    <button on:click = {() => {push('/post')}}>Create new post</button>
    {#if showLogout == true}
    <button class="outline" on:click = {logout}>Log out</button>
    {/if}
</main>
