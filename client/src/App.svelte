<script>
	let dflt = [];
	let showButton = true;
	import Login from './Login.svelte'
	import Feed from './Feed.svelte'
	let loginSuccess = false;
	function getBooks(){
		fetch("./allposts")
		.then(resp => resp.json().then(data => {
			dflt=data;
			return data;
		}
		));
		showButton = false;
	}
	$: {if(loginSuccess){
		getBooks()
	} else{
		dflt=[]
	}};
</script>

<main>
	<h1>tino exchange.</h1>
	<Login bind:indicator={loginSuccess}/>
	<Feed postdict={dflt}/>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
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
		text-align: center;
	}
	
	p{
		font-family: 'Barlow', sans-serif;
		text-align: center;
	}

</style>