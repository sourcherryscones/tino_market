<script>
	let dflt = [{'id': 4, 'title': 'The Greatest of Gatsbies', 'description': 'Genuinely wonder what this book is about sometimes', 'posted_by': 1, 'is_claimed': false}];
	let showButton = true;
	import Feed from './Feed.svelte'
	import FeedCopy from './FeedCopy.svelte'
	//import AltFeed from './AltFeed.svelte'

	function getBooks(){
		fetch("./allposts")
		.then(resp => resp.json().then(data => {
			//print("DATA IS", data);
			//print(typeof(data));
			dflt=data;
		}
		));
		showButton = false;
	}

</script>

<main>
	<h1>tino exchange.</h1>
	<p>search for items below :D</p>
	<FeedCopy postdict={dflt}/>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	{#if showButton==true}
		<button on:click={getBooks}>Load books!</button>
	{/if}

	<!--<AltFeed/>-->
	</main>

<style>
	main{
		margin-left: 20px;
	}
	h1 {
		color: #ff3e00;
		text-transform: lowercase;
		font-size: 4em;
		font-weight: 900;
		font-family: 'JetBrains Mono', monospace;
		text-transform: uppercase;
	}
	
	body{
		font-family: 'Barlow', sans-serif;
	}

</style>