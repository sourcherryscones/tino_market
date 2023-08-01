import Login from './Login.svelte'
import Feed from './Feed.svelte'
import Register from './Register.svelte'
import Home from './Home.svelte'
import Post from './Post.svelte'
import MyFeed from './MyFeed.svelte'
import About from './About.svelte'

export const routes = {
    "/": Home,
    "/login": Login,
    "/register": Register,
    "/feed": Feed,
    "/post": Post,
    "/myitems": MyFeed,
    "/about": About
}