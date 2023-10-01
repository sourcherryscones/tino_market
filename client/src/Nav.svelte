<script>
    import {push} from "svelte-spa-router"
    import Router, { link } from "svelte-spa-router";
    import { routes } from "./routes.js";
    import {onMount} from 'svelte'
    import { isloggedin } from "./stores.js"
    let isLoggedIn = false;
    let loginFlag = false;

    isloggedin.subscribe((val) => {
      isLoggedIn = val;
    })

    onMount(async () => {
        const res = await fetch('./getsession');
        const resp = await res.json();
        console.log("RESP IS")
        console.log(resp)
        loginFlag = resp['login']
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
                //showLogout = false;
                isloggedin.set(false)
                push('/login')
            }
        }))
    }
</script>

<main class="container">
    <nav class="nav">
      <ul>
        <strong><li><a class="brand" href="/">&#x267B;TINO EXCHANGE</a></li></strong>
      </ul>
      <ul>
        <li><a href="/register" use:link hidden={loginFlag}>Register</a></li>
        <li><a href="/login" use:link hidden={loginFlag}>Log In</a></li>
        <li><a href="/about" use:link>About</a></li>
        <li><a href="/feed" use:link hidden={!loginFlag}>Feed</a></li>
        <li><a href="/myitems" use:link hidden={!loginFlag}>My Items</a></li>
        <li><a href="/myposts" use:link hidden={!loginFlag}>My Posts</a></li>
        <li><a href="/feed" use:link hidden={!loginFlag} on:click={logout}>Log Out</li>
      </ul>
    </nav>
    <Router {routes}/>
  </main>