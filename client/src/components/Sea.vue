<template>
    <div class="sea" :class="{ dashboard: isDashboard }">

    </div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
    data() {
        return {
            startY: 0, // 触摸位置
            endY: 0, // 结束位置
            disY: 0, // 移动距离
            isDashboard: this.$store.state.showDashboard
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
                        this.toggleDashboard(this.isDashboard)
                    }
                }
            }
            this.startY = 0;
            this.endY = 0;
        });
    },
    methods: {
        ...mapMutations(['toggleDashboard']),
    },
    watch: {
        '$store.state.showDashboard'(newVal, oldVal) {
            this.isDashboard = newVal
            // console.log(this.isDashboard)
        },
    }
}
</script>

<style lang="scss">
.sea{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 30%;
    /* 背景模糊制造大海的感觉 */
    backdrop-filter: blur(100px);
    -webkit-backdrop-filter: blur(100px);
    // z-index: 7;

    transition: all 1.2s ease-in-out;
}

/* Dashboard */
.dashboard {
    height: 100%;
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
}

// @media (max-width: 480px) {
//     .sea {
//         height: 30%;
//     }
// }
</style>