<template>
    <div class="universe">
        <sun-moon></sun-moon>
        <nav-bar></nav-bar>
    </div>
</template>

<script>
import SunMoon from "../components/SunMoon.vue"
import NavBar from "../components/NavBar.vue"

export default {
    components: {
        SunMoon,
        NavBar
    }
}

</script>

<style>

</style>
