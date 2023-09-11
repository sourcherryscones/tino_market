<script>
    //import { push } from "svelte-spa-router";

    let title = '';
    let description = '';
    let condition = '';
    let showHint = false;
    

    /*function addPost(){
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
    */

</script>


<main>
    <head>
    </head>
    <form class="post" action="/postsquared" method="post" enctype="multipart/form-data">
        <h1>Create new post</h1>
        <input type="text" name="title" bind:value={title} placeholder="Item title">
        <input type="text" name="description" bind:value={description} placeholder="Item description">
        <select name="condition" bind:value={condition}>
            <option value="GOOD" selected>Good</option>
            <option value="OK">OK</option>
        </select>
		<input name="postimg" type="file" accept="image/*">
        <input class="btn" type="submit">
        {#if showHint == true}
        <br>
        <small class="errmess">Please check to make sure that your post has all of the necessary elements!</small>
        {/if}
    </form>
</main>



