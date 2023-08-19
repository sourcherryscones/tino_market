<script>
    import Router, { link } from "svelte-spa-router";
    import { routes } from "./routes.js";
</script>

<main class="container">
    <nav>
        <ul>
          <li><strong><a href="/" use:link>&#x267B;TINO EXCHANGE</strong></li>
        </ul>
        <ul>
          <li><a href="/register" use:link>Register</a></li>
          <li><a href="/login" use:link>Log In</a></li>
          <li><a href="/about" use:link>About</a></li>
          <li><a href="/feed" use:link>Feed</a></li>
          <li><a href="/myitems" use:link>My Items</a></li>
        </ul>
      </nav>

    <Router {routes}/>
</main>
