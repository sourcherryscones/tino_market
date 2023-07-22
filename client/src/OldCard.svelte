<script>
    export let bookitem;
    export let title;
    export let description;
    export let donor;
    export let claimed;
    export let recip;

    function claimItem(bk){
        console.log(bk);
        console.log('the id of this item is ' + bk['id']);
        const resp = fetch('./claim/' + bk['id'], {
            method: 'PUT',
            body: JSON.stringify(bk),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => {
            console.log(resp.json().then(data => {
                bk['is_claimed'] = data['is_claimed']
                bk['recip'] = data['recip']
                bk=bk;
            }));
    });
    }
</script>

<main>
    <div id = "card">
        <h1>{title}</h1>
        <h3>{description}</h3>
        <h4>Posted by {donor}</h4>
        <button disabled = {claimed} on:click={claimItem(bookitem)}>i want this!</button>
        {#if claimed == true}
            <h4>claimed by {recip}</h4>
        {/if}
    </div>
</main>

<style>
    #card{
        background-color: #0d6f82;
    }
</style>