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
    <div class="card">
        <img src={book['image']} align="center" class="card-img-top" alt="book"/>
        <div class="card-body">
            <h5 class="card-title">{book['title']}</h5>
            <h6 class="gbadge" style={(book['condition'] == "OK") ? "background-color:yellow" : "background-color: #76d279a1"}>{book['condition']}</h6>
            <p class="card-text">lorem ipsum dolor sit amet!!!</p>
            <button class="btn btn-primary btn-lg" disabled = {book['is_claimed']} on:click={claimItem(book)}>{book['is_claimed'] ? 'X' : '+'}</button>
        </div>
        
    </div>
</main>

<style>
    .lwrcs{
        text-transform: lowercase;
    }

    .card-img-top{
        height:300px;
        object-fit:cover
    }

    .btn{
        background-color:#43a047;
    }
</style>

<!--

    <h5 class="cardtitle">{book['title']}<span class="gbadge-container"><h6 class="gbadge" style={(book['condition'] == "OK") ? "background-color:yellow" : "background-color: #76d279a1"}>{book['condition']}</h6></span></h5>
        
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
-->