<script>
    export let book;

    function claimItem(bk){
        console.log("CLAIM ITEM S GETTING CALLEDDDD");
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
                bk['recip'] = data['recip'];
                //alert('stuff happened!!');
                bk=bk;
                book=book;
            }));
        });
    }
    //export let description = 'basically exactly what it sounds like lmfao';
</script>
<main>
    <article class="minwid">
        <img src="https://m.media-amazon.com/images/I/913AUm7VHhL._AC_UF1000,1000_QL80_.jpg" align="center" class="cardimg"/>
        <h1 class="cardtitle">{book['title']}</h1>
        <h6 class="gbadge">{book['condition']}</h6>
        <p>{book['description']}</p>
        <h4>Posted by {book['donor']}</h4>
        <div class="grid">
            <button disabled = {book['is_claimed']} on:click={claimItem(book)}>{book['is_claimed'] ? 'X' : '+'}</button>            
        </div>
        {#if book['is_claimed'] == true}
            <p class="claimedby">(claimed by {book['recip']})</p>
        {/if}
    </article>
</main>
