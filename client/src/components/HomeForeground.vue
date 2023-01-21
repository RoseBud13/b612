<template>
    <div class="home-foreground" :class="[{ dashboardMode: isDashboard }, theme]">
        <dashboard></dashboard>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapMutations } from 'vuex';
import Dashboard from "./Dashboard.vue"

export default defineComponent({
    components: {
        Dashboard
    },
    data() {
        return {
            startY: 0, // 触摸位置
            endY: 0, // 结束位置
            disY: 0, // 移动距离
            isDashboard: this.$store.state.showDashboard,
            theme: this.$store.state.homeTheme
        }
    },
    mounted () {
        this.$el.addEventListener('touchstart', evt => {
            this.startY = evt.targetTouches[0].clientY;
        });
        this.$el.addEventListener('touchmove', evt => {
            this.endY = evt.targetTouches[0].clientY;
        });
        this.$el.addEventListener('touchend', () => {
            this.disY = this.endY - this.startY;

            if (this.startY != Math.abs(this.disY)) {
                //在滑动的距离超过屏幕高度的20%时，做某种操作
                // console.log('滑动',Math.abs(distanceY))
                if (Math.abs(this.disY) > 20) {
                    // console.log(this.disY)
                    //向下滑实行函数someAction1，向上滑实行函数someAction2
                    if (this.disY < 0) {
                        if (this.isDashboard === false) {
                            this.toggleDashboard(this.isDashboard)
                        }
                    }
                }
            }
            this.startY = 0;
            this.endY = 0;
        });
        this.getDeviceHeight()
    },
    methods: {
        ...mapMutations(['toggleDashboard']),
        getDeviceHeight() {
            // Update the element's size
            let vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        }
    },
    watch: {
        '$store.state.showDashboard'(newVal, oldVal) {
            this.isDashboard = newVal
            // console.log(this.isDashboard)
        },
        '$store.state.homeTheme'(newVal, oldVal) {
            this.theme = newVal
            // console.log(this.theme)
        },
    }
})
</script>

<style lang="scss" scoped>
.home-foreground{
    position: absolute;
    bottom: 0;
    width: 100vw;
    height: 30vh;
    /* 背景模糊制造大海的感觉 */
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    // z-index: 7;

    transition: all 1.2s ease-in-out;
}

/** Theme with pic */
.night {
    height: 10vh;
}
.sunset {
    height: 10vh;
}

/* Dashboard */
.dashboardMode {
    height: calc(var(--vh, 1vh) * 100 - 50px);
    z-index: 100;
}

// @media (max-width: 480px) {
//     .sea {
//         height: 30%;
//     }
// }
</style>