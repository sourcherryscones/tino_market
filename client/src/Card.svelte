<script>
    export let title = 'Barrons SAT Prep 2022';
    export let bookitem;
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
                bk['recip'] = data['recip'];
                recip = data['recip'];
                claimed = data['is_claimed'];
            }));
        });
    }
    //export let description = 'basically exactly what it sounds like lmfao';
</script>
<main>
    <div class='cardcont'>
        <img src='https://m.media-amazon.com/images/I/913AUm7VHhL._AC_UF1000,1000_QL80_.jpg' alt='image of princeton book'/>
        <h4 class="cardtitle">{title}</h4>
        <p>{description}</p>
        <h4>Posted by {donor}</h4>
        <button disabled = {claimed} on:click={claimItem(bookitem)}>{claimed ? 'X' : '+'}</button>
        {#if claimed == true}
            <p class="claimedby">(claimed by {recip})</p>
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