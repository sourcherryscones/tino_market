<script>
    //export let postdict = [];
    let booklist = [];
    import {link, push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import {isloggedin} from './stores';
    import Card from './Card.svelte';
    import Nav from './Nav.svelte';
    let showLogout = true;
    let liflag;

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
        const res = await fetch('./myitems');
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
                push('/')
            }
        }))
    }
</script>


<main>
    <Nav/>
    <div class="container">
        <head>
        </head>
        <h1>My items</h1>
        <p>Items that I've claimed on Tino Exchange</p>
        <div class="grid">
            {#each booklist as book}
                <Card book={book} />
            {/each}
        </div>
        <h2 role="button" class="outline"><a href="/post" use:link>Post a new item!</a></h2>
    </div>
</main>
