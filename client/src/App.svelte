<script>
	let dflt = [];
	let showButton = true;
	let showLogout = false;
	let showReg = false;
	import Login from './Login.svelte'
	import Feed from './Feed.svelte'
	import Register from './Register.svelte'
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
		showLogout = true;
	} else{
		dflt=[]
		showLogout = false;
	}};
</script>

<main>
	<h1>tino exchange.</h1>
	<Login bind:indicator={loginSuccess}/>
	<button on:click={() => {showReg = true}}>New user? Register here!</button>
	{#if showReg}
		<Register bind:indicator={showReg}/>
	{/if}
	<Feed postdict={dflt}/>
	</main>

<style>
	main{
		/*margin-left: 20px;*/
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