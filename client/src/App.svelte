<script>
    import Router, { link } from "svelte-spa-router";
    import { routes } from "./routes.js";
</script>

<main>
    <h1>tino exchange.</h1>
    <h1><a href="/" use:link>Home</a></h1>
    <Router {routes}/>
</main>

<style>
	/*p{
		font-family: 'Barlow', sans-serif;
		text-align: center;
	}*/

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