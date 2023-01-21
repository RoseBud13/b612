<template>
    <div class="home">
        <background></background>
        <navbar></navbar>
        <foreground></foreground>
        <login></login>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import Background from "../components/HomeBackground.vue"
import Navbar from "../components/HomeNavbar.vue"
import Foreground from "../components/HomeForeground.vue"
import Login from '../components/modal/Login.vue'

export default defineComponent({
    components: {
        Background,
        Navbar,
        Foreground,
        Login
    }
})

</script>

<style>

</style>
