<script>
    import { push } from "svelte-spa-router";

    let title = '';
    let description = '';
    let condition = '';
    let showHint = false;
    

    function addPost(){
        const post = fetch('./postsquared', {
            method: 'POST',
            body: JSON.stringify({'title': title, 'description': description, 'condition': condition}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(resp => resp.json().then(res => {
            let id = res['id'];
            if (id){
                title='';
                description='';
                condition = '';
                push('/feed');
            } else{
                showHint=true;
            }
        }));
    }
</script>


<main>
    <head>
    </head>
    <div class="post">
        <h1>Create new post</h1>
        <input type="text" bind:value={title} placeholder="Item title">
        <input type="text" bind:value={description} placeholder="Item description">
        <input name="postimg" type="file" accept="image/jpeg, image/png, image/jpg">
        <select bind:value={condition}>
            <option value="GOOD" selected>Good</option>
            <option value="OK">OK</option>
        </select>
        <input id = "submitbtn" class="btn" type="submit" on:click={() => {addPost()}}>
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your post has all of the necessary elements!</small>
        {/if}
    </div>
</main>



