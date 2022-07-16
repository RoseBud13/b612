<template>
    <div class="nav-bar">
        <div class="nav-bar-container" :class="(dashboard? 'dashboard-shown' : '')">
            <div class="nav-bar-left">
                <port @goTo="toUniverse"></port>
            </div>
            <div class="nav-bar-mid">
                <div class="clock-box" @click="toggleDashboard(this.dashboard)">
                    <clock :blink="true" :displaySeconds="false" :twelveHour="false"></clock>
                </div>
            </div>
            <div class="nav-bar-right" :class="[theme]">
                <div class="menu-item">
                    <div class="menu-btn">
                        <i class="fas fa-cog"></i>
                    </div>
                    <ul class="menu-subitems">
                        <li @click="toggleHomeThemeWithPic(this.themeWithPic)">
                            <i v-if="theme === 'light'" class="fas fa-image"></i>
                            <i v-else-if="theme === 'dark'" class="fas fa-image"></i>
                            <i v-else class="fas fa-shapes"></i>
                        </li>
                        <li @click="toggleHomeTheme(this.icon)">
                            <i :class="['fas', `fa-${icon}`]"></i>
                        </li>
                    </ul>
                </div>
                <div class="menu-item">
                    <div class="menu-btn">
                        <i class="fas fa-user-circle"></i>
                    </div>
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

<style lang="scss" scoped>
ul {
  list-style: none;
}
.nav-bar {
    position: absolute;
    top: 0;
    z-index: 100;
    width: 100vw;
    height: 50px;
}
.nav-bar-container {
    width: 100%;
    height: 100%;
    font-size: 17px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.dashboard-shown {
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
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
.menu-item {
    position: relative;
    width: 40px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin: 0 10px 0 0;
    border-radius: 5px;
    cursor: pointer;
}
.menu-item:hover .menu-btn i {
    color: #49b1f5;
}
.menu-subitems {
  position: absolute;
  display: none;
  right: 0;
  width: 40px;
  box-shadow: 0 5px 20px -4px rgba(0, 0, 0, 0.5);
  background-color: #fff;
  animation: showsub 0.3s 0.1s ease both;
}
.menu-subitems i {
    color: #23373d;
    margin-top: 10px;
}
.menu-item:hover .menu-subitems {
  display: block;
}
.menu-subitems li:hover i {
    color: #49b1f5;
}
.dark .menu-btn i {
    color: #daf6ff;
}
.night .menu-btn i {
    color: #daf6ff;
}
.light .menu-btn i {
    color: #23373d;
}
.sunset .menu-btn i {
    color: #daf6ff;
}
@keyframes showsub {
  0% {
    opacity: 0;
    filter: alpha(opacity=0);
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    filter: none;
    transform: translateY(0);
  }
}
</style>
