<template>
    <div class="port">
        <div class="port-btn" @click="$emit('goTo')" v-show="this.$route.meta.showPort || this.show === 'show' ">
            <!-- <ion-icon name="planet-outline"></ion-icon> -->
            <img src="../assets/img/planet-outline.svg" alt="planet">
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    data() {
        return {
            show: ''
        }
    },
    methods: {
        setShow() {
            let width = Math.max(window.screen.width, window.innerWidth);
            if (width > '480') {
                this.show = 'show'
            } else {
                this.show = 'hide'
            }
        }
    },
    mounted() {
        this.setShow()
    }
})
</script>

<style lang="scss">
.port {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 7;
}
.port-btn {
    background: rgba(255, 255, 255, 0.5);
    color: #000;
    width: 40px;
    height: 30px;
    line-height: 35px;
    text-align: center;
    margin: 10px 15px;
    font-size: 15px;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 2px 2px -2px rgba(0,0,0,.2);
}
.port-btn img {
    width: 19px;
}
.port-btn:hover {
    background: #e1e1e1;
}
</style>
