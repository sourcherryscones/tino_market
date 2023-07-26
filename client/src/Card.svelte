<script>
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();
    export let bookitem;

    function claimItem(bk){
        const resp = fetch('./claim/' + bk['id'], {
            method: 'PUT',
            body: JSON.stringify(bk),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(data => {
                bk['is_claimed'] = data['is_claimed']
                bk['recip'] = data['recip'];
                alert('stuff happened!!');
                bk=bk;
                bookitem=bookitem
            }));
        });
    }
    //export let description = 'basically exactly what it sounds like lmfao';
</script>
<main>
    <div class='cardcont'>
        <img src='https://m.media-amazon.com/images/I/913AUm7VHhL._AC_UF1000,1000_QL80_.jpg' alt='image of princeton book'/>
        <h4 class="cardtitle">{bookitem['title']}</h4>
        <p>{bookitem['description']}</p>
        <h4>Posted by {bookitem['donor']}</h4>
        <button disabled = {bookitem['is_claimed']} on:click={claimItem(bookitem)}>{bookitem['is_claimed'] ? 'X' : '+'}</button>
        {#if bookitem['is_claimed'] == true}
            <p class="claimedby">(claimed by {bookitem['recip']})</p>
        {/if}
    </div>
</main>

<style>
    .cardtitle{
        text-align: center;
        color: #27214D;
        font-size: 20px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 800;
    }
    .cardcont{
        border: 2px solid;
		border-radius:20px;
		min-height: 250px;
        text-align: center;
        margin:10px;
    }

    img{
        width:92px;
        height:114px;
        margin:10px 0px;
    }
</style>