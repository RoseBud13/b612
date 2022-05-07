<template>
    <div class="home">
        <sun-moon></sun-moon>
        <nav-bar></nav-bar>
        <dashboard></dashboard>
    </div>
</template>

<script>
import SunMoon from "../components/SunMoon.vue"
import NavBar from "../components/NavBar.vue"
import Dashboard from "../components/Dashboard.vue"

export default {
    components: {
        SunMoon,
        NavBar,
        Dashboard
    }
}

</script>

<style>

</style>
