<template>
    <div class="home">
        <sun-moon></sun-moon>
        <nav-bar></nav-bar>
        <sea></sea>
        <login></login>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import SunMoon from "../components/SunMoon.vue"
import NavBar from "../components/NavBar.vue"
import Sea from "../components/Sea.vue"
import Login from '../components/Login.vue'

export default defineComponent({
    components: {
        SunMoon,
        NavBar,
        Sea,
        Login
    }
})

</script>

<style>

</style>
