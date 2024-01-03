<script>
    //export let postdict = [];
    let booklist = [];
    import {link, push} from 'svelte-spa-router';
    import { onMount } from 'svelte';
    import {isloggedin} from './stores'
    import Nav from './Nav.svelte';
    import MyPostsCard from './MyPostsCard.svelte'
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
        const res = await fetch('./myposts');
        const resp = await res.json();
        booklist = resp.reverse();
        console.log("ON MOUNT, ELEMENTS ARE");
        console.log(booklist)
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

    function delItemHandler(ebent){
        let del_id = ebent.detail['id']
        let tbd = -3;
        for (let k = 0; k < booklist.length;k++){
            if (booklist[k]['id'] == del_id){
                console.log("K WAS "+k);
                tbd = k;
                break;
            }
        }
        
        if (tbd > -1) booklist.splice(tbd,1);
        booklist=booklist
        push('/myposts')
        
    }
</script>


<main>
    <Nav/>
    <div class="container">
        <head>
        </head>
        <h1>My Posts</h1>
        
        <p>Items that I've posted on Tino Exchange</p>
        <div class="grid">
            {#each booklist as book}
                <MyPostsCard book={book} on:deleted_item={delItemHandler} />
            {/each}
        </div>
        <h2 role="button" class="outline"><a href="/post" use:link>Post a new item!</a></h2>
    </div>
</main>

<style>
</style>
