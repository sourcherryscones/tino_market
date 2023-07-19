<script>
    export let postdict = [];
    //[{'id': 8, 'title': 'The Great Gatsby', 'description': 'Stolen from an ALH classroom', 'condition': 'TRAUMATIZED'}]
</script>


<main> <!--hi-->
    <div class="container">
    {#each postdict as book}
    <div id = "card">
        <h1>{book['title']}</h1>
        <h3>{book['description']}</h3>
    </div>
    {/each}
    </div>
</main>

<style>
    .container{
        display:grid;
        grid-template-columns: 2;
    }

    #card{
        background-color: #197288;
        color:#fff;
        border-radius:20px;
        padding: 10px;
        margin: 20px 0px;
    }
</style>