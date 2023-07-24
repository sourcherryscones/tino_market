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
    <div class = "cardcont">
        <img src="https://m.media-amazon.com/images/I/913AUm7VHhL._AC_UF1000,1000_QL80_.jpg"/>
        <h1 class="cardtitle">{book['title']}</h1>
        <p>{book['description']}</p>
        <h4>Posted by {book['donor']}</h4>
        <button disabled = {book['is_claimed']} on:click={claimItem(book)}>{book['is_claimed'] ? 'X' : '+'}</button>
        {#if book['is_claimed'] == true}
            <p class="claimedby">(claimed by {book['recip']})</p>
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
        margin:3px;
    }

    img{
        width:92px;
        height:114px;
        margin:10px 0px;
    }

    button{
        background-color: #FFF2E7;
        color:#f08626;
        border-radius: 100px;
        font-size: 30px;
        font-weight: 700;
        height:40px;
        padding:0px 40px;
        transition:0.4s;
    }

    button:hover{
        background-color: rgb(255, 209, 172);
    }

    button:disabled{
        background-color: rgb(198, 176, 149);
        color:#9a5718;
    }
</style>