<template>
    <div class="home">
        <sun-moon></sun-moon>
        <nav-bar></nav-bar>
        <sea></sea>
    </div>
</template>

<script>
import SunMoon from "../components/SunMoon.vue"
import NavBar from "../components/NavBar.vue"
import Sea from "../components/Sea.vue"

export default {
    components: {
        SunMoon,
        NavBar,
        Sea
    }
}

</script>

<style>

</style>
