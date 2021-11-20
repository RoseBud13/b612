<template>
    <div class="home">
        <space></space>
        <planet></planet>
        <continent-detail></continent-detail>
    </div>
</template>

<script>
import Space from '../components/Space.vue'
// import Planet from '../components/xPlanet.vue'
import Planet from '../components/Planet.vue'
import ContinentDetail from '../components/ContinentDetail.vue'

export default {
    components: {
        Space,
        Planet,
        ContinentDetail
    }
}

</script>

<style>

</style>