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
                bk['donor_email'] = data['donor_email'];
                //alert('stuff happened!!');
                bk=bk;
                book=book;
            }));
        });
    }
    //export let description = 'basically exactly what it sounds like lmfao';
</script>
<main>
    <article>
        <img src="https://m.media-amazon.com/images/I/913AUm7VHhL._AC_UF1000,1000_QL80_.jpg" align="center" class="cardimg" alt="book"/>
        <h5 class="cardtitle">{book['title']}</h5>
        <h6 class="gbadge">{book['condition']}</h6>
        <p>{book['description']}</p>
        <h4>Posted by {book['donor']}</h4>
        {#if book.donor_email != null}
            <h6>Contact at <span>{book['donor_email']}</span></h6>
        {/if}
        <div>
            <button disabled = {book['is_claimed']} on:click={claimItem(book)}>{book['is_claimed'] ? 'X' : '+'}</button>            
        </div>
        {#if book['is_claimed'] == true}
            <p class="claimedby">(claimed by {book['recip']})</p>
        {/if}
        {#if book.recip_email}
            <h6>Contact at <span class="lwrcs">{book['recip_email']}</span></h6>
        {/if}
    </article>
</main>

<style>
    .lwrcs{
        text-transform: lowercase;
    }
</style>