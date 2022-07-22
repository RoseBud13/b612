<template>
    <div>
        <space></space>
        <nav-bar></nav-bar>
    </div>
</template>

<script>
import { defineComponent, reactive, watch, getCurrentInstance, onMounted } from 'vue';
import Space from '../components/Space.vue'
import NavBar from "../components/NavBar.vue"

export default {
    components: {
        Space,
        NavBar
    },
}
</script>

<style lang="scss" scoped>

</style>