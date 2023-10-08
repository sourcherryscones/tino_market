<script>
    import { push} from "svelte-spa-router";
    import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
    export let book;
    let modalVisible = false;

    function showModal(){
        modalVisible = true;
    }

    function hideModal(){
        modalVisible = false;
    }

    /*function claimItem(bk){
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
    */
    //export let description = 'basically exactly what it sounds like lmfao';

    function deleteBook(bk){
        const resp = fetch('./delete/' + bk['id'], {
            method: 'DELETE',
            body: JSON.stringify(bk),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => {
            console.log(resp.json().then(data => {
               let deleteSuccess = data['delbooksuccess'];
               console.log("MOMENT OF TRUTH DID IT GET DELETED?")
               console.log(data['delbooksuccess']);
               if (deleteSuccess){
                    dispatch('deleted_item', {
                        id: bk['id']
                    })
                    push('/myposts')
               }
            }));
        });
    }
</script>
<main>
    <div class="card">
        <div class="card-body text-center py-2" style="background-color:#dddddd;">
            <p class="card-text" style="background-color:#dddddd; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; font-weight: 300">{book['category']}</p>
          </div>
        <img src={book['image']} align="center" class="card-img-top" style="border-radius:0px;" alt="book"/>
        <div class="card-body">
            <h5 class="card-title">{book['title']}</h5>
            <h6 class="gbadge" style={(book['condition'] == "OK") ? "background-color:yellow" : "background-color: #76d279a1"}>{book['condition']}</h6>
            <br>
            <p class="card-text">{book['description']}</p>
            <button class="btn btn-primary btn-md" disabled = {book['is_claimed']} on:click={deleteBook(book)}>Delete item</button>
            <!--<button class="btn btn-primary" data-bs-target="">Show modal</button>-->
            {#if book.recip_email}
                <h6>Contact at <span class="lwrcs">{book['recip_email']}</span></h6>
            {/if}
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
        
-->