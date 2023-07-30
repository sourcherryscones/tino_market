<script>
    import {link} from 'svelte-spa-router';
</script>

<main>
    <h1><a href="/register" use:link>Register</a></h1>
    <h1><a href="/login" use:link>Log In</a></h1>
</main>

<style>
    h1 {
		color: #ff3e00;
		text-transform: lowercase;
		font-size: 4em;
		font-weight: 900;
		font-family: 'JetBrains Mono', monospace;
		text-transform: uppercase;
		text-align: center;
	}
</style>

<!--IDEA: create simple "/userstatus" route so that u can correctly display home or feed depending on whether or not user is logged in-->
