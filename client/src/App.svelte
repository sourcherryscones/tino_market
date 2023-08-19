<script>
    import Router, { link } from "svelte-spa-router";
    import { routes } from "./routes.js";
</script>

<main class="container">
  <nav class="nav">
    <ul>
      <strong><li><a class="brand" href="/">&#x267B;TINO EXCHANGE</a></li></strong>
    </ul>
    <ul>
      <li><a href="/register" use:link>Register</a></li>
      <li><a href="/login" use:link>Log In</a></li>
      <li><a href="/about" use:link>About</a></li>
      <li><a href="/feed" use:link>Feed</a></li>
      <li><a href="/myitems" use:link>My Items</a></li>
    </ul>
  </nav>
  <!--
  <nav>
    <ul>
      <li><strong><li><a href="/">&#x267B;TINO EXCHANGE</a></li></strong></li>
    </ul>
    <ul>
      <li><li><a href="#">Link</a></li></li>
      <li><li><a href="#">Link</a></li></li>
      <li><li><a href="#" role="button">Button</a></li></li>
    </ul>
  </nav>
-->
    <Router {routes}/>
</main>

<!--

-->