<script>
    export let postdict = [];
    import Card from './Card.svelte';
</script>


<main>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    {#each postdict as book}
        <Card book={book} />
    {/each}
</main>

<style>
    main {
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: auto;
		gap: 20px;
		max-width: 960px;
		margin: auto;
	}
	@media (min-width: 600px) {
		main {
			grid-template-columns: 1fr 1fr 1fr;
            text-align: left;
		}
	}
</style>