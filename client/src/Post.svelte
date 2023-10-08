<script>
    //import { push } from "svelte-spa-router";

    import Nav from "./Nav.svelte";

    let title = '';
    let description = '';
    let condition = '';
    let showHint = false;
    let category = '';
    

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
    <Nav/>
    <div class="container">
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
            <select name="category" bind:value={category}>
                <option value="PREP BOOK" selected>Prep book</option>
                <option value="TEXTBOOK">Textbook</option>
                <option value="OTHER">Other</option>
            </select>
            <input class="btn" type="submit" disabled={!(category != '' && title != '' && description != '' && condition != '')}>
            {#if showHint == true}
            <br>
            <small class="errmess">Please check to make sure that your post has all of the necessary elements!</small>
            {/if}
        </form>
    </div>
</main>



