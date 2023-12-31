import Login from './Login.svelte'
import Feed from './Feed.svelte'
import Register from './Register.svelte'
import Home from './Home.svelte'
import Post from './Post.svelte'
import MyFeed from './MyFeed.svelte'
import About from './About.svelte'
import TestUpload from './TestUpload.svelte'
import MyPosts from './MyPosts.svelte'
import Verify from './Verify.svelte'
import Forgot from './Forgot.svelte'
import ResetPassword from './ResetPassword.svelte'
import { wrap } from 'svelte-spa-router/wrap'

export const routes = {
    "/": Home,
    "/login": Login,
    "/register": Register,
    "/feed": Feed,
    "/post": Post,
    "/myitems": MyFeed,
    "/about": About,
    "/testupload": TestUpload,
    "/myposts": MyPosts,
    "/verify/:emailval/:from": Verify,
    "/forgot": Forgot,
    "/pwreset/:emailval": ResetPassword
}