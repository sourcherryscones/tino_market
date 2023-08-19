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
        let tempbl = [];
        for (let i=0;i<booklist.length-3;i+=3){
            let miniarr = [];
            for (let j=i; j < i+3; j++){
                miniarr.push(booklist[j]);
            }
            tempbl.push(miniarr);
        }
        console.log(tempbl);
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
    {#if showLogout == true}
    <button class="button primary" on:click = {logout}>Log out</button>
    {/if}
    <button class="outline" href="/post">Post a new item!</button>
</main>
