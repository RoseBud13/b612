<template>
    <div class="nav-bar">
        <div class="nav-bar-container">
            <div class="nav-bar-left">
                <port @goTo="toUniverse"></port>
            </div>
            <div class="nav-bar-mid">
                <div class="clock-box" @click="toggleDashboard(this.dashboard)">
                    <clock :blink="true" :displaySeconds="false" :twelveHour="false"></clock>
                </div>
            </div>
            <div class="nav-bar-right">
                <div class="toggle-box" :class="[theme]" @click="toggleHomeThemeWithPic(this.themeWithPic)">
                    <i v-if="theme === 'light'" class="fas fa-image"></i>
                    <i v-else-if="theme === 'dark'" class="fas fa-image"></i>
                    <i v-else class="fas fa-shapes"></i>
                </div>
                <div class="toggle-box" :class="[theme]" @click="toggleHomeTheme(this.icon)">
                    <i :class="['fas', `fa-${icon}`]"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapMutations } from 'vuex';
import Port from './Port.vue';
import Clock from './Clock.vue';

export default defineComponent({
    components: {
        Port,
        Clock
    },
    data() {
        return {
            icon: this.$store.state.homeThemeIcon,
            dashboard: this.$store.state.showDashboard,
            theme: this.$store.state.homeTheme,
            themeWithPic: this.$store.state.isHomeThemeWithPic
        }
    },
    methods: {
        ...mapMutations(['toggleHomeTheme', 'toggleDashboard', 'toggleHomeThemeWithPic']),

        toUniverse() {
            this.$router.push({name: "universe"})
        },
    },
    watch: {
        '$store.state.homeThemeIcon'(newVal, oldVal) {
            this.icon = newVal
            // console.log(this.icon)
        },
        '$store.state.showDashboard'(newVal, oldVal) {
            this.dashboard = newVal
            // console.log(this.dashboard)
        },
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        },
        '$store.state.isHomeThemeWithPic'(newVal, oldVal) {
            this.themeWithPic = newVal
            // console.log(this.themeWithPic)
            // console.log(this.theme)
        }
    }
})
</script>

<style lang="scss">
.nav-bar {
    position: absolute;
    top: 0;
    z-index: 100;
}
.nav-bar-container {
    width: 100vw;
    height: 50px;
    // background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    // box-shadow: 0 2px 2px -2px rgba(0,0,0,.2);

    display: flex;
    align-items: center;
    justify-content: space-between;
}
.nav-bar-left {
    flex: 1;
    align-self: center;
}
.nav-bar-mid {
    flex: 2;
    align-self: center;
}
.nav-bar-right {
    flex: 1;
    align-self: center;
    display: flex;
    justify-content: flex-end;
}
.clock-box {
    margin: auto;
    width: 100%;
    height: 30px;
}
.toggle-box {
    // background: rgba(255, 255, 255, 0.5);
    // color: #000;
    width: 40px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin: 15px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    // margin-left: auto;
    // box-shadow: 0 2px 2px -2px rgba(0,0,0,.2);
}
.toggle-box:hover{
    background: #bbbaba;
}
.dark .fas {
    color: #daf6ff;
}
.night .fas {
    color: #daf6ff;
}
.light .fas {
    color: #23373d;
}
.sunset .fas {
    color: #daf6ff;
}
</style>
