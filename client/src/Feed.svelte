<script>
    //export let postdict = [];
    let booklist = [];
    import Nav from './Nav.svelte'
    import {link, push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import Card from './Card.svelte';
    import { isloggedin } from './stores';
    let showLogout = true;
    let liflag;
    let modal;
    let search_input='';
    let dialog;
    let header = "Feed"

    async function getSession(){
      const res = await fetch('./getsession');
      const resp = await res.json();
      console.log("RESP IS")
      console.log(resp)
      return resp['login']
    }

    onMount(async () => {
        liflag = await getSession()
        console.log(liflag)
        const res = await fetch('./allposts');
        const resp = await res.json();
        booklist = resp.reverse();
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
                isloggedin.set(false)
                push('/login')
            }
        }))
    }

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
            searchItem(search_input);
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

    async function searchItem(search_term){
        console.log("searchItem called!!")
        const res = await fetch('./search/' + search_term);
        const resp = await res.json();
        header = "Search results for " + search_term;
        booklist = resp;
    }

</script>

<svelte:window on:keydown={on_key_down} on:keyup={on_key_up}/>
<main>
    <head>
    </head>
    <Nav/>
    <div class="container">
        <input id = "srchbar" type="search" bind:value={search_input} placeholder="Search for an item!">
        <h1>{header}</h1>
        <a class="rtalign" role="button" href="/#/post">Create new post</a>
        <div class="grid">
            {#each booklist as book}
                <Card book={book} />
            {/each}
        </div>
    </div>
</main>

<style>
    @media only screen and (max-width:595px){ .grid{ grid-template-columns:repeat(1, 1fr); } }
    @media only screen and (min-width:600px){ .grid{ grid-template-columns:repeat(1, 1fr); } }
    @media only screen and (min-width:785px){ .grid{ grid-template-columns:repeat(2, 1fr); } }
    @media only screen and (min-width:890px){ .grid{ grid-template-columns:repeat(3, 1fr); } }

    #srchbar{
        width:30%;
    }
</style>
