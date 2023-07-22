<script>
    import Card from './Card.svelte';
</script>

<main>
	<Card />
	<Card title='Princeton Review APCSA 2021'/>
	<Card />
	<Card />
</main>

<style>
	main {
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: auto;
		gap: 30px;
		max-width: 960px;
		margin: auto;
	}
	@media (min-width: 600px) {
		main {
			grid-template-columns: 1fr 1fr 1fr;
			/*grid-template-rows: 250px 250px;*/
		}
		div {
			min-height: auto;
		}
	}
</style>